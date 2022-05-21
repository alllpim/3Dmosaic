import os
from typing import Callable, Any

from PIL.Image import Image
from PySide6 import QtCore
from PySide6.QtCore import QThreadPool, QEvent, Signal, QTimer, Qt, QPointF
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QMainWindow, QFileDialog, QButtonGroup, QMessageBox, QSlider
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from stl import Mesh

from Worker import Worker
from cube_mesh_generator import create_many_cube_arrays, save_meshes
from image_processor import open_image, create_mosaic_from_image_1, create_mosaic_from_image_2, \
    create_mosaic_from_image_3, create_mosaic_from_image_with_palette_2, create_mosaic_from_image_with_palette_1, \
    add_grid_to_mosaic, add_numbers_to_mosaic, add_grid_and_numbers_to_mosaic, add_raw_grid_and_numbers_to_mosaic, \
    get_colors_distribution, colors_palette_from_hex_colors, save_image, save_colors_distribution, rgb_to_hex
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    main_thread_signal: Signal = Signal(object)

    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("3DMosaic")

        icon = QIcon("icon.ico")
        if not os.path.isfile("icon.ico"):
            icon = QIcon("Program/icon.ico")
        self.setWindowIcon(icon)

        self.mesh_canvas: FigureCanvas | None = None
        self.mesh_plot: Axes3D | None = None

        self.setup_radio_button_groups()
        self.setup_sliders()
        self.setup_signal_slots()
        self.setup_mesh_plot()

        self.ui.image_scroll_area_widget.installEventFilter(self)

        # noinspection PyUnresolvedReferences
        self.main_thread_signal.connect(self.run)

        self.threadpool: QThreadPool = QThreadPool.globalInstance()

        self.mosaic_debounce: QTimer = QTimer()
        self.mosaic_debounce.setInterval(400)
        self.mosaic_debounce.setSingleShot(True)
        # noinspection PyUnresolvedReferences
        self.mosaic_debounce.timeout.connect(self.create_and_show_mosaic)

        self.mesh_debounce: QTimer = QTimer()
        self.mesh_debounce.setInterval(300)
        self.mesh_debounce.setSingleShot(True)
        # noinspection PyUnresolvedReferences
        self.mesh_debounce.timeout.connect(self.create_and_show_mesh)

        self.imported_image: Image | None = None
        self.mosaic_image: Image | None = None
        self.mosaic_parameters: dict | None = None
        self.used_mosaic_parameters: dict | None = None

        self.mesh: list[Mesh] | None = None
        self.imported_mesh: Mesh | None = None
        self.mesh_parameters: dict | None = None
        self.used_mesh_parameters: dict | None = None
        self.current_mesh_file_index: int = 1

        self.original_image_viewport_width: int | None = None
        self.original_image_viewport_height: int | None = None

        self.current_image: QPixmap | None = None
        self.image_scale_factor: float = 1.0

    @staticmethod
    def run(function: Callable) -> None:
        """
        A method for simply running a function

        """
        function()

    def run_on_main_thread(self, function: Callable) -> None:
        """
        Method for starting a function in the main thread

        """
        # noinspection PyUnresolvedReferences
        self.main_thread_signal.emit(function)

    def run_on_background(self, function: Callable) -> None:
        """
        Method for running a function in a background thread

        """
        worker = Worker(function)
        self.threadpool.start(worker)

    def setup_sliders(self) -> None:
        for slider in self.ui.__dict__.values():
            if isinstance(slider, QSlider):
                slider.installEventFilter(self)

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if event.type() == QEvent.Wheel:
            # noinspection PyTypeChecker
            result = self.wheel_event_filter(watched, event)
            if result is not None:
                return result

        return QMainWindow.eventFilter(self, watched, event)

    def wheel_event_filter(self, watched: QtCore.QObject, event: QtCore.QEvent.Wheel) -> bool | None:
        if isinstance(watched, QSlider):
            event.ignore()
            return True
        elif watched == self.ui.image_scroll_area_widget and event.modifiers() & Qt.ControlModifier == Qt.ControlModifier:
            if event.angleDelta().y() > 0:
                self.scale_image(1.1, event.scenePosition())
            else:
                self.scale_image(0.95, event.scenePosition())
            event.accept()
            return True
        return None

    def setup_radio_button_groups(self) -> None:
        self.ui.coloring_method_group = QButtonGroup()
        self.ui.coloring_method_group.addButton(self.ui.colors_count_method_radio_button)
        self.ui.coloring_method_group.addButton(self.ui.color_palette_method_radio_button)
        self.ui.colors_count_method_radio_button.setChecked(True)

        self.ui.colors_count_methods_group = QButtonGroup()
        self.ui.colors_count_methods_group.addButton(self.ui.first_colors_count_method_radio_button)
        self.ui.colors_count_methods_group.addButton(self.ui.second_colors_count_method_radio_button)
        self.ui.colors_count_methods_group.addButton(self.ui.third_colors_count_method_radio_button)
        self.ui.first_colors_count_method_radio_button.setChecked(True)

        self.ui.color_palette_methods_group = QButtonGroup()
        self.ui.color_palette_methods_group.addButton(self.ui.first_color_palette_method_radio_button)
        self.ui.color_palette_methods_group.addButton(self.ui.second_color_palette_method_radio_button)
        self.ui.first_color_palette_method_radio_button.setChecked(True)

        self.ui.overlay_group = QButtonGroup()
        self.ui.overlay_group.addButton(self.ui.no_overlay_radio_button)
        self.ui.overlay_group.addButton(self.ui.grid_radio_button)
        self.ui.overlay_group.addButton(self.ui.numbers_radio_button)
        self.ui.overlay_group.addButton(self.ui.grid_and_numbers_radio_button)
        self.ui.overlay_group.addButton(self.ui.grid_and_numbers_with_white_background_radio_button)
        self.ui.no_overlay_radio_button.setChecked(True)

    def setup_signal_slots(self) -> None:
        self.ui.configuration_tab_widget.currentChanged.connect(self.on_tab_click)

        self.ui.import_image_button.clicked.connect(self.import_image)
        self.ui.show_imported_image_button.clicked.connect(self.show_imported_image)

        self.ui.preserving_proportions_check_box.toggled.connect(self.on_proportions_check_box_change)
        self.ui.width_slider.valueChanged.connect(self.on_width_change)
        self.ui.height_slider.valueChanged.connect(self.on_height_change)
        self.ui.multiplier_slider.valueChanged.connect(self.on_multiplier_change)

        self.ui.colors_count_method_radio_button.toggled.connect(self.show_colors_count_settings)
        self.ui.color_palette_method_radio_button.toggled.connect(self.show_color_palette_settings)

        self.ui.colors_count_slider.valueChanged.connect(self.on_colors_count_change)

        self.ui.first_colors_count_method_radio_button.toggled.connect(self.create_and_show_mosaic_live)
        self.ui.second_colors_count_method_radio_button.toggled.connect(self.create_and_show_mosaic_live)
        self.ui.third_colors_count_method_radio_button.toggled.connect(self.create_and_show_mosaic_live)

        self.ui.first_color_palette_method_radio_button.toggled.connect(self.create_and_show_mosaic_live)
        self.ui.second_color_palette_method_radio_button.toggled.connect(self.create_and_show_mosaic_live)

        self.ui.no_overlay_radio_button.toggled.connect(self.create_and_show_mosaic_live)
        self.ui.grid_radio_button.toggled.connect(self.create_and_show_mosaic_live)
        self.ui.numbers_radio_button.toggled.connect(self.create_and_show_mosaic_live)
        self.ui.grid_and_numbers_radio_button.toggled.connect(self.create_and_show_mosaic_live)
        self.ui.grid_and_numbers_with_white_background_radio_button.toggled.connect(self.create_and_show_mosaic_live)

        self.ui.numbers_size_slider.valueChanged.connect(self.on_numbers_size_change)

        self.ui.create_mosaic_live_check_box.toggled.connect(self.on_mosaic_live_check_box)
        self.ui.create_mosaic_button.clicked.connect(self.create_and_show_mosaic)

        self.ui.open_and_show_mesh_button.clicked.connect(self.import_mesh)

        self.ui.show_frame_check_box.toggled.connect(self.on_show_frame)
        self.ui.same_axis_scale_check_box.toggled.connect(self.on_same_axis_scale)

        self.ui.same_count_by_axis_check_box.toggled.connect(self.on_same_count_axis)
        self.ui.axis_x_count_slider.valueChanged.connect(self.on_axis_x_count)
        self.ui.axis_y_count_slider.valueChanged.connect(self.on_axis_y_count)
        self.ui.same_multiplier_by_axis_check_box.toggled.connect(self.on_same_multiplier_axis)
        self.ui.axis_x_multiplier_slider.valueChanged.connect(self.on_axis_x_multiplier)
        self.ui.axis_y_multiplier_slider.valueChanged.connect(self.on_axis_y_multiplier)
        self.ui.axis_z_multiplier_slider.valueChanged.connect(self.on_axis_z_multiplier)
        self.ui.same_offset_by_axis_check_box.toggled.connect(self.on_same_offset_axis)
        self.ui.axis_x_offset_slider.valueChanged.connect(self.on_axis_x_offset)
        self.ui.axis_y_offset_slider.valueChanged.connect(self.on_axis_y_offset)
        self.ui.total_count_slider.valueChanged.connect(self.on_total_count)
        self.ui.file_number_slider.valueChanged.connect(self.on_file_number)

        self.ui.create_mesh_live_check_box.toggled.connect(self.on_mesh_live_check_box)
        self.ui.create_mesh_button.clicked.connect(self.create_and_show_mesh)

        self.ui.save_mosaic_button.clicked.connect(self.save_mosaic)
        self.ui.save_mosaic_palette_button.clicked.connect(self.save_mosaic_palette)
        self.ui.save_mosaic_mesh_button.clicked.connect(self.save_mosaic_mesh)

    def on_tab_click(self, index: int) -> None:
        if index == 1:
            self.ui.show_stacked_widget.setCurrentIndex(1)
        else:
            self.ui.show_stacked_widget.setCurrentIndex(0)

    def import_mesh(self) -> None:
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Файл сетки (*.stl)")
        if dialog.exec():
            file_names = dialog.selectedFiles()
            if len(file_names) > 0:
                try:
                    self.imported_mesh = Mesh.from_file(file_names[0])
                    self.draw_mesh(self.imported_mesh)
                except:
                    self.show_warning("Ошибка", "Выбранный файл не является файлом, содержащим сетку")
                    return

    def import_image(self) -> None:
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Изображения (*.png *.jpg *.jpeg *.gif)")
        if dialog.exec():
            file_names = dialog.selectedFiles()
            if len(file_names) > 0:
                try:
                    self.imported_image = open_image(file_names[0], folder="")
                except:
                    self.show_warning("Ошибка", "Выбранный файл не является изображением")
                    return
                self.ui.show_imported_image_button.setEnabled(True)
                self.ui.create_mosaic_live_check_box.setChecked(False)
                self.ui.create_mosaic_live_check_box.setEnabled(True)
                self.ui.create_mosaic_button.setEnabled(True)
                self.on_proportions_check_box_change(self.ui.preserving_proportions_check_box.isChecked())
                self.ui.width_slider.setValue(min(50, self.imported_image.width))
                self.ui.height_slider.setValue(min(50, self.imported_image.height))
                self.run_on_main_thread(lambda: self.ui.save_mosaic_button.setEnabled(False))
                self.run_on_main_thread(lambda: self.ui.save_mosaic_palette_button.setEnabled(False))
                self.run_on_main_thread(lambda: self.ui.save_mosaic_mesh_button.setEnabled(False))
                self.show_image(self.imported_image)

    def show_imported_image(self) -> None:
        self.show_image(self.imported_image)
        self.used_mosaic_parameters = None
        self.ui.create_mosaic_live_check_box.setChecked(False)
        self.run_on_main_thread(lambda: self.ui.save_mosaic_button.setEnabled(False))
        self.run_on_main_thread(lambda: self.ui.save_mosaic_palette_button.setEnabled(False))
        self.run_on_main_thread(lambda: self.ui.save_mosaic_mesh_button.setEnabled(False))

    def show_image(self, image: Image) -> None:
        self.image_scale_factor = 1.0
        self.current_image = image.toqpixmap()
        self.run_on_main_thread(lambda: self.internal_show_image(image))

    def internal_show_image(self, image: Image) -> None:
        self.ui.image_label.clear()
        self.original_image_viewport_width = min(self.ui.image_scroll_area.width(), image.width)
        self.original_image_viewport_height = min(self.ui.image_scroll_area.height(), image.height)
        self.ui.image_label.setPixmap(
            image.toqpixmap().scaled(self.original_image_viewport_width, self.original_image_viewport_height,
                                     QtCore.Qt.KeepAspectRatio))

    def on_proportions_check_box_change(self, value: bool) -> None:
        if self.imported_image is None:
            return

        if value:
            proportions = self.imported_image.width / self.imported_image.height
            if self.imported_image.width > self.imported_image.height:
                width = min(200, int(self.imported_image.width * proportions))
                height = int(min(200 / proportions, self.imported_image.height / proportions))
            else:
                width = int(min(200 * proportions, self.imported_image.width * proportions))
                height = min(200, int(self.imported_image.height / proportions))

            self.ui.width_slider.setMaximum(width)
            self.ui.height_slider.setMaximum(height)
            self.on_width_change(self.ui.width_slider.value())
        else:
            self.ui.width_slider.setMaximum(min(200, self.imported_image.width))
            self.ui.height_slider.setMaximum(min(200, self.imported_image.height))

    def on_width_change(self, value: int) -> None:
        self.ui.width_slider_value_label.setText(str(value))
        if self.ui.preserving_proportions_check_box.isChecked():
            self.ui.height_slider.blockSignals(True)
            height_value = max(1, int(value / (self.imported_image.width / self.imported_image.height)))
            self.ui.height_slider.setValue(height_value)
            self.ui.height_slider_value_label.setText(str(height_value))
            self.ui.height_slider.blockSignals(False)
        self.create_and_show_mosaic_live()

    def on_height_change(self, value: int) -> None:
        self.ui.height_slider_value_label.setText(str(value))
        if self.ui.preserving_proportions_check_box.isChecked():
            self.ui.width_slider.blockSignals(True)
            width_value = max(1, int(value * (self.imported_image.width / self.imported_image.height)))
            self.ui.width_slider.setValue(width_value)
            self.ui.width_slider_value_label.setText(str(width_value))
            self.ui.width_slider.blockSignals(False)
        self.create_and_show_mosaic_live()

    def on_multiplier_change(self, value: int) -> None:
        self.ui.multiplier_slider_value_label.setText(str(value))
        self.create_and_show_mosaic_live()

    def on_colors_count_change(self, value: int) -> None:
        self.ui.colors_count_value_label.setText(str(value))
        self.create_and_show_mosaic_live()

    def on_numbers_size_change(self, value: int) -> None:
        self.ui.numbers_size_slider_value_label.setText(str(value))
        self.create_and_show_mosaic_live()

    def show_colors_count_settings(self) -> None:
        self.ui.coloring_method_stacked_widget.setCurrentIndex(0)

    def show_color_palette_settings(self) -> None:
        self.ui.coloring_method_stacked_widget.setCurrentIndex(1)
        self.ui.create_mosaic_live_check_box.setChecked(False)

    # noinspection PyTypedDict
    def get_mosaic_parameters(self) -> dict[str, Any | None] | None:
        parameters = {"width": self.ui.width_slider.value(), "height": self.ui.height_slider.value(),
                      "multiplier": self.ui.multiplier_slider.value(), "colors": None, "coloring_function": None,
                      "overlay_function": None, "numbers_size": None}

        if self.ui.colors_count_method_radio_button.isChecked():
            parameters["colors"] = self.ui.colors_count_slider.value()
            if self.ui.first_colors_count_method_radio_button.isChecked():
                parameters["coloring_function"] = create_mosaic_from_image_1
            elif self.ui.second_colors_count_method_radio_button.isChecked():
                parameters["coloring_function"] = create_mosaic_from_image_2
            elif self.ui.third_colors_count_method_radio_button.isChecked():
                parameters["coloring_function"] = create_mosaic_from_image_3
        elif self.ui.color_palette_method_radio_button.isChecked():
            colors_text = self.ui.colors_palette_edit.toPlainText()
            color_lines = [color_line.strip() for color_line in colors_text.split("#") if
                           len(color_line) != 0 and not color_line.isspace()]

            try:
                parameters["colors"] = colors_palette_from_hex_colors(color_lines)
            except:
                self.show_warning("Ошибка", "Некорректный ввод цветов")
                return None

            if len(parameters["colors"]) < 2:
                self.show_warning("Ошибка", "Недостаточное количество цветов")
                return None

            if self.ui.first_color_palette_method_radio_button.isChecked():
                parameters["coloring_function"] = create_mosaic_from_image_with_palette_1
            elif self.ui.second_color_palette_method_radio_button.isChecked():
                parameters["coloring_function"] = create_mosaic_from_image_with_palette_2

        if self.ui.no_overlay_radio_button.isChecked():
            parameters["overlay_function"] = None
            parameters["numbers_size"] = None
        elif self.ui.grid_radio_button.isChecked():
            parameters["overlay_function"] = add_grid_to_mosaic
            parameters["numbers_size"] = None
        elif self.ui.numbers_radio_button.isChecked():
            parameters["overlay_function"] = add_numbers_to_mosaic
            parameters["numbers_size"] = self.ui.numbers_size_slider.value()
        elif self.ui.grid_and_numbers_radio_button.isChecked():
            parameters["overlay_function"] = add_grid_and_numbers_to_mosaic
            parameters["numbers_size"] = self.ui.numbers_size_slider.value()
        elif self.ui.grid_and_numbers_with_white_background_radio_button.isChecked():
            parameters["overlay_function"] = add_raw_grid_and_numbers_to_mosaic
            parameters["numbers_size"] = self.ui.numbers_size_slider.value()

        return parameters

    def show_warning(self, title: str, text: str) -> None:
        self.run_on_main_thread(lambda: self._internal_show_warning(title, text))

    def _internal_show_warning(self, title: str, text: str) -> None:
        message_box = QMessageBox(self)
        message_box.setWindowTitle(title)
        message_box.setText(text)
        message_box.setIcon(QMessageBox.Warning)
        message_box.exec()

    @staticmethod
    def create_mosaic(image: Image, parameters: dict[str, Any]) -> Image:
        mosaic = parameters["coloring_function"](image, parameters["colors"], parameters["width"], parameters["height"],
                                                 parameters["multiplier"])
        colors_distribution = get_colors_distribution(mosaic, parameters["multiplier"])
        if parameters["overlay_function"] is not None:
            return parameters["overlay_function"](mosaic, colors_distribution, parameters["multiplier"],
                                                  numbers_size=parameters["numbers_size"])
        else:
            return mosaic

    def create_and_show_mosaic(self) -> None:
        self.mosaic_parameters = self.get_mosaic_parameters()
        self.run_on_background(lambda: self._internal_create_and_show_mosaic())

    def _internal_create_and_show_mosaic(self) -> None:
        if self.mosaic_parameters is not None:
            if self.used_mosaic_parameters != self.mosaic_parameters:
                self.disable_all_ui()
                self.mosaic_image = self.create_mosaic(self.imported_image, self.mosaic_parameters)
                self.used_mosaic_parameters = self.mosaic_parameters
                self.show_image(self.mosaic_image)
                self.run_on_main_thread(lambda: self.ui.save_mosaic_button.setEnabled(True))
                self.run_on_main_thread(lambda: self.ui.save_mosaic_palette_button.setEnabled(True))
                self.run_on_main_thread(lambda: self.ui.save_mosaic_mesh_button.setEnabled(True))
                self.enable_all_ui()

    def enable_all_ui(self) -> None:
        self.run_on_main_thread(lambda: self.ui.image_scroll_area.setAttribute(Qt.WA_TransparentForMouseEvents, False))
        self.run_on_main_thread(lambda: self.ui.configuration_tab_widget.setEnabled(True))

    def disable_all_ui(self) -> None:
        self.run_on_main_thread(lambda: self.ui.image_scroll_area.setAttribute(Qt.WA_TransparentForMouseEvents, True))
        self.run_on_main_thread(lambda: self.ui.configuration_tab_widget.setEnabled(False))

    def on_mosaic_live_check_box(self, value: bool) -> None:
        self.ui.create_mosaic_button.setEnabled(not value)
        self.create_and_show_mosaic_live(value)

    def create_and_show_mosaic_live(self, value: bool = True) -> None:
        if value and self.ui.create_mosaic_live_check_box.isChecked():
            self.mosaic_debounce.start()

    def scale_image(self, factor: float, relative_cursor_position: QPointF) -> None:
        if self.original_image_viewport_width is None:
            return

        image_scale_factor_temp = self.image_scale_factor
        self.image_scale_factor *= factor
        self.image_scale_factor = max(0.05, min(25.0, self.image_scale_factor))

        if image_scale_factor_temp == self.image_scale_factor:
            return

        self.run_on_background(lambda: self.internal_scale_image(factor, relative_cursor_position))

    def internal_scale_image(self, factor: float, relative_cursor_position: QPointF) -> None:
        scaled_image = self.current_image.scaled(self.image_scale_factor * self.original_image_viewport_width,
                                                 self.image_scale_factor * self.original_image_viewport_height,
                                                 QtCore.Qt.KeepAspectRatio)

        self.run_on_main_thread(lambda: self.internal_after_scale_image(scaled_image, factor, relative_cursor_position))

    def internal_after_scale_image(self, scaled_image: QPixmap, factor: float,
                                   relative_cursor_position: QPointF) -> None:
        self.ui.image_label.setPixmap(scaled_image)

        self.ui.image_scroll_area.horizontalScrollBar().setValue(
            relative_cursor_position.x() * factor - self.ui.image_scroll_area.horizontalScrollBar().pageStep() * 0.5)
        self.ui.image_scroll_area.verticalScrollBar().setValue(
            relative_cursor_position.y() * factor - self.ui.image_scroll_area.verticalScrollBar().pageStep() * 0.5)

    def draw_mesh(self, mesh: Mesh) -> None:
        self.mesh_plot.cla()

        if self.ui.show_frame_check_box.isChecked():
            self.mesh_plot.add_collection3d(
                Poly3DCollection(mesh.vectors, facecolors="w", edgecolors="k", linewidths=0.3))
        else:
            self.mesh_plot.add_collection3d(Poly3DCollection(mesh.vectors, facecolors="w"))

        points = mesh.points.flatten()
        if self.ui.same_axis_scale_check_box.isChecked():
            self.mesh_plot.auto_scale_xyz(points, points, points)
        else:
            self.mesh_plot.auto_scale_xyz(points[0::3], points[1::3], points[2::3])

        self.mesh_canvas.figure.tight_layout()
        self.mesh_canvas.figure.canvas.draw()

    def create_and_show_mesh(self) -> None:
        self.mesh_parameters = self.get_mesh_parameters()
        file_number = self.ui.file_number_slider.value()
        self.run_on_background(lambda: self._internal_create_and_show_mesh(file_number))

    def _internal_create_and_show_mesh(self, file_number: int) -> None:
        if self.mesh_parameters is not None:
            if self.used_mesh_parameters != self.mesh_parameters:
                self.disable_all_ui()
                self.imported_mesh = None
                self.mesh = create_many_cube_arrays(
                    [self.mesh_parameters["total_count"]],
                    (self.mesh_parameters["multiplier_x"], self.mesh_parameters["multiplier_y"],
                     self.mesh_parameters["multiplier_z"]),
                    (self.mesh_parameters["offset_x"], self.mesh_parameters["offset_y"], 0),
                    (self.mesh_parameters["count_x"], self.mesh_parameters["count_y"], 1)
                )[0]
                self.used_mesh_parameters = self.mesh_parameters
                self.run_on_main_thread(lambda: self.ui.file_number_slider.setMaximum(len(self.mesh)))
                self.current_mesh_file_index = min(file_number, len(self.mesh)) - 1
                self.run_on_main_thread(lambda: self.draw_mesh(self.mesh[self.current_mesh_file_index]))
                self.enable_all_ui()
            elif self.current_mesh_file_index != file_number - 1 or self.imported_mesh is not None:
                self.disable_all_ui()
                self.imported_mesh = None
                self.current_mesh_file_index = file_number - 1
                self.run_on_main_thread(lambda: self.draw_mesh(self.mesh[self.current_mesh_file_index]))
                self.enable_all_ui()

    def on_show_frame(self) -> None:
        if self.imported_mesh is not None:
            self.draw_mesh(self.imported_mesh)
        elif self.mesh is not None:
            self.draw_mesh(self.mesh[self.current_mesh_file_index])

    def on_same_axis_scale(self) -> None:
        if self.imported_mesh is not None:
            self.draw_mesh(self.imported_mesh)
        elif self.mesh is not None:
            self.draw_mesh(self.mesh[self.current_mesh_file_index])

    def on_same_count_axis(self, value: bool) -> None:
        if value:
            self.on_axis_x_count(self.ui.axis_x_count_slider.value())
            self.create_and_show_mesh_live()

    def on_axis_x_count(self, value: int) -> None:
        self.ui.axis_x_count_slider_value_label.setText(str(value))
        if self.ui.same_count_by_axis_check_box.isChecked():
            self.ui.axis_y_count_slider.blockSignals(True)
            self.ui.axis_y_count_slider.setValue(value)
            self.ui.axis_y_count_slider_value_label.setText(str(value))
            self.ui.axis_y_count_slider.blockSignals(False)
        self.create_and_show_mesh_live()

    def on_axis_y_count(self, value: int) -> None:
        self.ui.axis_y_count_slider_value_label.setText(str(value))
        if self.ui.same_count_by_axis_check_box.isChecked():
            self.ui.axis_x_count_slider.blockSignals(True)
            self.ui.axis_x_count_slider.setValue(value)
            self.ui.axis_x_count_slider_value_label.setText(str(value))
            self.ui.axis_x_count_slider.blockSignals(False)
        self.create_and_show_mesh_live()

    def on_same_multiplier_axis(self, value: bool) -> None:
        if value:
            self.on_axis_x_multiplier(self.ui.axis_x_multiplier_slider.value())
            self.create_and_show_mesh_live()

    def on_axis_x_multiplier(self, value: int) -> None:
        self.ui.axis_x_multiplier_slider_value_label.setText(str(value))
        self.ui.axis_x_offset_slider.setMaximum(value * 10)
        if self.ui.same_multiplier_by_axis_check_box.isChecked():
            self.ui.axis_y_offset_slider.setMaximum(value * 10)
            self.ui.axis_y_multiplier_slider.blockSignals(True)
            self.ui.axis_y_multiplier_slider.setValue(value)
            self.ui.axis_y_multiplier_slider_value_label.setText(str(value))
            self.ui.axis_y_multiplier_slider.blockSignals(False)
            self.ui.axis_z_multiplier_slider.blockSignals(True)
            self.ui.axis_z_multiplier_slider.setValue(value)
            self.ui.axis_z_multiplier_slider_value_label.setText(str(value))
            self.ui.axis_z_multiplier_slider.blockSignals(False)
        self.create_and_show_mesh_live()

    def on_axis_y_multiplier(self, value: int) -> None:
        self.ui.axis_y_multiplier_slider_value_label.setText(str(value))
        self.ui.axis_y_offset_slider.setMaximum(value * 10)
        if self.ui.same_multiplier_by_axis_check_box.isChecked():
            self.ui.axis_x_multiplier_slider.blockSignals(True)
            self.ui.axis_x_multiplier_slider.setValue(value)
            self.ui.axis_x_multiplier_slider_value_label.setText(str(value))
            self.ui.axis_x_multiplier_slider.blockSignals(False)
            self.ui.axis_z_multiplier_slider.blockSignals(True)
            self.ui.axis_z_multiplier_slider.setValue(value)
            self.ui.axis_z_multiplier_slider_value_label.setText(str(value))
            self.ui.axis_z_multiplier_slider.blockSignals(False)
        self.create_and_show_mesh_live()

    def on_axis_z_multiplier(self, value: int) -> None:
        self.ui.axis_z_multiplier_slider_value_label.setText(str(value))
        if self.ui.same_multiplier_by_axis_check_box.isChecked():
            self.ui.axis_x_multiplier_slider.blockSignals(True)
            self.ui.axis_x_multiplier_slider.setValue(value)
            self.ui.axis_x_multiplier_slider_value_label.setText(str(value))
            self.ui.axis_x_multiplier_slider.blockSignals(False)
            self.ui.axis_y_multiplier_slider.blockSignals(True)
            self.ui.axis_y_multiplier_slider.setValue(value)
            self.ui.axis_y_multiplier_slider_value_label.setText(str(value))
            self.ui.axis_y_multiplier_slider.blockSignals(False)
        self.create_and_show_mesh_live()

    def on_same_offset_axis(self, value: bool) -> None:
        if value:
            self.on_axis_x_offset(self.ui.axis_x_offset_slider.value())
            self.create_and_show_mesh_live()

    def on_axis_x_offset(self, value: int) -> None:
        self.ui.axis_x_offset_slider_value_label.setText(str(value))
        if self.ui.same_offset_by_axis_check_box.isChecked():
            self.ui.axis_y_offset_slider.blockSignals(True)
            self.ui.axis_y_offset_slider.setValue(value)
            self.ui.axis_y_offset_slider_value_label.setText(str(value))
            self.ui.axis_y_offset_slider.blockSignals(False)
        self.create_and_show_mesh_live()

    def on_axis_y_offset(self, value: int) -> None:
        self.ui.axis_y_offset_slider_value_label.setText(str(value))
        if self.ui.same_offset_by_axis_check_box.isChecked():
            self.ui.axis_x_offset_slider.blockSignals(True)
            self.ui.axis_x_offset_slider.setValue(value)
            self.ui.axis_x_offset_slider_value_label.setText(str(value))
            self.ui.axis_x_offset_slider.blockSignals(False)
        self.create_and_show_mesh_live()

    def on_total_count(self, value: int) -> None:
        self.ui.total_count_slider_value_label.setText(str(value))
        self.create_and_show_mesh_live()

    def on_file_number(self, value: int) -> None:
        self.ui.file_number_slider_value_label.setText(str(value))
        self.create_and_show_mesh_live()

    def on_mesh_live_check_box(self, value: bool) -> None:
        self.ui.create_mesh_button.setEnabled(not value)
        self.create_and_show_mesh_live(value)

    def setup_mesh_plot(self) -> None:
        self.mesh_canvas = FigureCanvas(Figure(figsize=(10, 10)))
        self.mesh_plot = self.mesh_canvas.figure.add_subplot(projection="3d")
        self.ui.mesh_page_layout.addWidget(self.mesh_canvas)

    def create_and_show_mesh_live(self, value: bool = True) -> None:
        if value and self.ui.create_mesh_live_check_box.isChecked():
            self.mesh_debounce.start()

    def get_mesh_parameters(self) -> dict[str, int]:
        return {
            "count_x": self.ui.axis_x_count_slider.value(),
            "count_y": self.ui.axis_y_count_slider.value(),
            "multiplier_x": self.ui.axis_x_multiplier_slider.value(),
            "multiplier_y": self.ui.axis_y_multiplier_slider.value(),
            "multiplier_z": self.ui.axis_z_multiplier_slider.value(),
            "offset_x": self.ui.axis_x_offset_slider.value(),
            "offset_y": self.ui.axis_y_offset_slider.value(),
            "total_count": self.ui.total_count_slider.value()
        }

    def save_mosaic(self) -> None:
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setNameFilter("Изображение (*.png)")
        if dialog.exec():
            file_names = dialog.selectedFiles()
            if len(file_names) > 0:
                try:
                    save_image(self.current_image, file_names[0], folder="")
                except:
                    self.show_warning("Ошибка", "Ошибка сохранения мозаики")

    def save_mosaic_palette(self) -> None:
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setNameFilter("Текстовый файл (*.txt)")
        if dialog.exec():
            file_names = dialog.selectedFiles()
            if len(file_names) > 0:
                self.run_on_background(lambda: self._internal_save_mosaic_palette(file_names[0]))

    def _internal_save_mosaic_palette(self, filename: str) -> None:
        try:
            self.disable_all_ui()
            colors_distribution = get_colors_distribution(self.mosaic_image, self.used_mosaic_parameters["multiplier"])
            save_colors_distribution(filename, colors_distribution, folder="")
        except:
            self.show_warning("Ошибка", "Ошибка сохранения палитры цветов")
        finally:
            self.enable_all_ui()

    def save_mosaic_mesh(self) -> None:
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec():
            folder_names = dialog.selectedFiles()
            if len(folder_names) > 0:
                self.run_on_background(lambda: self._internal_save_mosaic_mesh(folder_names[0]))

    def _internal_save_mosaic_mesh(self, folder: str) -> None:
        try:
            self.disable_all_ui()
            self.used_mesh_parameters = self.used_mesh_parameters if self.used_mesh_parameters is not None else self.get_mesh_parameters()
            colors_distribution = get_colors_distribution(self.mosaic_image, self.used_mosaic_parameters["multiplier"])
            meshes = create_many_cube_arrays(list(colors_distribution.values()),
                                             (self.used_mesh_parameters["multiplier_x"],
                                              self.used_mesh_parameters["multiplier_y"],
                                              self.used_mesh_parameters["multiplier_z"]),
                                             (self.used_mesh_parameters["offset_x"],
                                              self.used_mesh_parameters["offset_y"], 0),
                                             (self.used_mesh_parameters["count_x"],
                                              self.used_mesh_parameters["count_y"], 1))
            save_meshes(meshes, list(map(lambda rgb: rgb_to_hex(rgb), list(colors_distribution.keys()))), folder)
        except:
            self.show_warning("Ошибка", "Ошибка сохранения файлов сетки")
        finally:
            self.enable_all_ui()
