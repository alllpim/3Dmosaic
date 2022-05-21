# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QCheckBox, QFrame, QGridLayout,
                               QHBoxLayout, QLabel, QPlainTextEdit,
                               QPushButton, QRadioButton, QScrollArea, QSizePolicy,
                               QSlider, QSpacerItem, QStackedWidget, QTabWidget,
                               QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QSize(1000, 600))
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.horizontalLayout = QHBoxLayout(self.central_widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_layout = QHBoxLayout()
        self.central_layout.setSpacing(10)
        self.central_layout.setObjectName(u"central_layout")
        self.central_layout.setContentsMargins(10, 10, 10, 10)
        self.show_layout = QHBoxLayout()
        self.show_layout.setSpacing(0)
        self.show_layout.setObjectName(u"show_layout")
        self.show_stacked_widget = QStackedWidget(self.central_widget)
        self.show_stacked_widget.setObjectName(u"show_stacked_widget")
        self.image_page = QWidget()
        self.image_page.setObjectName(u"image_page")
        self.verticalLayout_9 = QVBoxLayout(self.image_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.image_scroll_area = QScrollArea(self.image_page)
        self.image_scroll_area.setObjectName(u"image_scroll_area")
        self.image_scroll_area.setFrameShape(QFrame.NoFrame)
        self.image_scroll_area.setWidgetResizable(True)
        self.image_scroll_area.setAlignment(Qt.AlignCenter)
        self.image_scroll_area_widget = QWidget()
        self.image_scroll_area_widget.setObjectName(u"image_scroll_area_widget")
        self.image_scroll_area_widget.setGeometry(QRect(0, 0, 562, 578))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_scroll_area_widget.sizePolicy().hasHeightForWidth())
        self.image_scroll_area_widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.image_scroll_area_widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.image_label = QLabel(self.image_scroll_area_widget)
        self.image_label.setObjectName(u"image_label")
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setLineWidth(0)
        self.image_label.setTextFormat(Qt.PlainText)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_4.addWidget(self.image_label)

        self.image_scroll_area.setWidget(self.image_scroll_area_widget)

        self.verticalLayout_9.addWidget(self.image_scroll_area)

        self.show_stacked_widget.addWidget(self.image_page)
        self.mesh_page = QWidget()
        self.mesh_page.setObjectName(u"mesh_page")
        self.mesh_page_layout = QVBoxLayout(self.mesh_page)
        self.mesh_page_layout.setObjectName(u"mesh_page_layout")
        self.mesh_page_layout.setContentsMargins(0, 0, 0, 0)
        self.show_stacked_widget.addWidget(self.mesh_page)

        self.show_layout.addWidget(self.show_stacked_widget)

        self.central_layout.addLayout(self.show_layout)

        self.configuration_tab_widget = QTabWidget(self.central_widget)
        self.configuration_tab_widget.setObjectName(u"configuration_tab_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.configuration_tab_widget.sizePolicy().hasHeightForWidth())
        self.configuration_tab_widget.setSizePolicy(sizePolicy1)
        self.configuration_tab_widget.setMaximumSize(QSize(768, 16777215))
        self.configuration_tab_widget.setTabBarAutoHide(True)
        self.mosaic_configurator = QWidget()
        self.mosaic_configurator.setObjectName(u"mosaic_configurator")
        sizePolicy.setHeightForWidth(self.mosaic_configurator.sizePolicy().hasHeightForWidth())
        self.mosaic_configurator.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.mosaic_configurator)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mosaic_configurator_scroll_area = QScrollArea(self.mosaic_configurator)
        self.mosaic_configurator_scroll_area.setObjectName(u"mosaic_configurator_scroll_area")
        sizePolicy.setHeightForWidth(self.mosaic_configurator_scroll_area.sizePolicy().hasHeightForWidth())
        self.mosaic_configurator_scroll_area.setSizePolicy(sizePolicy)
        self.mosaic_configurator_scroll_area.setFrameShape(QFrame.NoFrame)
        self.mosaic_configurator_scroll_area.setLineWidth(0)
        self.mosaic_configurator_scroll_area.setWidgetResizable(True)
        self.mosaic_configurator_scroll_area.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.mosaic_configurator_scroll_area_widget = QWidget()
        self.mosaic_configurator_scroll_area_widget.setObjectName(u"mosaic_configurator_scroll_area_widget")
        self.mosaic_configurator_scroll_area_widget.setGeometry(QRect(0, -371, 383, 1180))
        sizePolicy.setHeightForWidth(self.mosaic_configurator_scroll_area_widget.sizePolicy().hasHeightForWidth())
        self.mosaic_configurator_scroll_area_widget.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.mosaic_configurator_scroll_area_widget)
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.overlay_label = QLabel(self.mosaic_configurator_scroll_area_widget)
        self.overlay_label.setObjectName(u"overlay_label")
        font = QFont()
        font.setPointSize(10)
        self.overlay_label.setFont(font)
        self.overlay_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.overlay_label)

        self.no_overlay_radio_button = QRadioButton(self.mosaic_configurator_scroll_area_widget)
        self.no_overlay_radio_button.setObjectName(u"no_overlay_radio_button")
        self.no_overlay_radio_button.setChecked(True)

        self.verticalLayout.addWidget(self.no_overlay_radio_button)

        self.grid_radio_button = QRadioButton(self.mosaic_configurator_scroll_area_widget)
        self.grid_radio_button.setObjectName(u"grid_radio_button")

        self.verticalLayout.addWidget(self.grid_radio_button)

        self.numbers_radio_button = QRadioButton(self.mosaic_configurator_scroll_area_widget)
        self.numbers_radio_button.setObjectName(u"numbers_radio_button")

        self.verticalLayout.addWidget(self.numbers_radio_button)

        self.grid_and_numbers_radio_button = QRadioButton(self.mosaic_configurator_scroll_area_widget)
        self.grid_and_numbers_radio_button.setObjectName(u"grid_and_numbers_radio_button")

        self.verticalLayout.addWidget(self.grid_and_numbers_radio_button)

        self.grid_and_numbers_with_white_background_radio_button = QRadioButton(
            self.mosaic_configurator_scroll_area_widget)
        self.grid_and_numbers_with_white_background_radio_button.setObjectName(
            u"grid_and_numbers_with_white_background_radio_button")

        self.verticalLayout.addWidget(self.grid_and_numbers_with_white_background_radio_button)

        self.gridLayout_3.addLayout(self.verticalLayout, 23, 0, 1, 3)

        self.height_label = QLabel(self.mosaic_configurator_scroll_area_widget)
        self.height_label.setObjectName(u"height_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.height_label.sizePolicy().hasHeightForWidth())
        self.height_label.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.height_label, 12, 0, 1, 2)

        self.multiplier_slider_value_label = QLabel(self.mosaic_configurator_scroll_area_widget)
        self.multiplier_slider_value_label.setObjectName(u"multiplier_slider_value_label")
        self.multiplier_slider_value_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.multiplier_slider_value_label, 15, 2, 1, 1)

        self.numbers_size_label = QLabel(self.mosaic_configurator_scroll_area_widget)
        self.numbers_size_label.setObjectName(u"numbers_size_label")

        self.gridLayout_3.addWidget(self.numbers_size_label, 25, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.colors_count_method_radio_button = QRadioButton(self.mosaic_configurator_scroll_area_widget)
        self.colors_count_method_radio_button.setObjectName(u"colors_count_method_radio_button")
        self.colors_count_method_radio_button.setChecked(True)

        self.horizontalLayout_3.addWidget(self.colors_count_method_radio_button)

        self.color_palette_method_radio_button = QRadioButton(self.mosaic_configurator_scroll_area_widget)
        self.color_palette_method_radio_button.setObjectName(u"color_palette_method_radio_button")

        self.horizontalLayout_3.addWidget(self.color_palette_method_radio_button)

        self.gridLayout_3.addLayout(self.horizontalLayout_3, 19, 0, 1, 3)

        self.coloring_method_label = QLabel(self.mosaic_configurator_scroll_area_widget)
        self.coloring_method_label.setObjectName(u"coloring_method_label")
        self.coloring_method_label.setFont(font)
        self.coloring_method_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.coloring_method_label, 18, 0, 1, 3)

        self.import_image_button = QPushButton(self.mosaic_configurator_scroll_area_widget)
        self.import_image_button.setObjectName(u"import_image_button")
        sizePolicy1.setHeightForWidth(self.import_image_button.sizePolicy().hasHeightForWidth())
        self.import_image_button.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.import_image_button, 1, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 27, 0, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 0, 0, 1, 3)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 17, 0, 1, 3)

        self.width_label = QLabel(self.mosaic_configurator_scroll_area_widget)
        self.width_label.setObjectName(u"width_label")
        sizePolicy2.setHeightForWidth(self.width_label.sizePolicy().hasHeightForWidth())
        self.width_label.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.width_label, 7, 0, 1, 2)

        self.width_slider_value_label = QLabel(self.mosaic_configurator_scroll_area_widget)
        self.width_slider_value_label.setObjectName(u"width_slider_value_label")
        self.width_slider_value_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.width_slider_value_label, 7, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout_3.addItem(self.verticalSpacer_8, 30, 0, 1, 3)

        self.numbers_size_slider = QSlider(self.mosaic_configurator_scroll_area_widget)
        self.numbers_size_slider.setObjectName(u"numbers_size_slider")
        self.numbers_size_slider.setMinimum(1)
        self.numbers_size_slider.setMaximum(100)
        self.numbers_size_slider.setPageStep(1)
        self.numbers_size_slider.setValue(12)
        self.numbers_size_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.numbers_size_slider, 26, 0, 1, 3)

        self.multiplier_label = QLabel(self.mosaic_configurator_scroll_area_widget)
        self.multiplier_label.setObjectName(u"multiplier_label")
        sizePolicy2.setHeightForWidth(self.multiplier_label.sizePolicy().hasHeightForWidth())
        self.multiplier_label.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.multiplier_label, 15, 0, 1, 2)

        self.show_imported_image_button = QPushButton(self.mosaic_configurator_scroll_area_widget)
        self.show_imported_image_button.setObjectName(u"show_imported_image_button")
        self.show_imported_image_button.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.show_imported_image_button.sizePolicy().hasHeightForWidth())
        self.show_imported_image_button.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.show_imported_image_button, 3, 1, 1, 1)

        self.height_slider = QSlider(self.mosaic_configurator_scroll_area_widget)
        self.height_slider.setObjectName(u"height_slider")
        self.height_slider.setMinimum(1)
        self.height_slider.setMaximum(1)
        self.height_slider.setPageStep(1)
        self.height_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.height_slider, 13, 0, 1, 3)

        self.numbers_size_slider_value_label = QLabel(self.mosaic_configurator_scroll_area_widget)
        self.numbers_size_slider_value_label.setObjectName(u"numbers_size_slider_value_label")
        self.numbers_size_slider_value_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.numbers_size_slider_value_label, 25, 2, 1, 1)

        self.height_slider_value_label = QLabel(self.mosaic_configurator_scroll_area_widget)
        self.height_slider_value_label.setObjectName(u"height_slider_value_label")
        sizePolicy1.setHeightForWidth(self.height_slider_value_label.sizePolicy().hasHeightForWidth())
        self.height_slider_value_label.setSizePolicy(sizePolicy1)
        self.height_slider_value_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.height_slider_value_label, 12, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 21, 0, 1, 3)

        self.coloring_method_stacked_widget = QStackedWidget(self.mosaic_configurator_scroll_area_widget)
        self.coloring_method_stacked_widget.setObjectName(u"coloring_method_stacked_widget")
        sizePolicy.setHeightForWidth(self.coloring_method_stacked_widget.sizePolicy().hasHeightForWidth())
        self.coloring_method_stacked_widget.setSizePolicy(sizePolicy)
        self.coloring_method_stacked_widget.setLineWidth(1)
        self.color_numbers_coloring_method_page = QWidget()
        self.color_numbers_coloring_method_page.setObjectName(u"color_numbers_coloring_method_page")
        sizePolicy.setHeightForWidth(self.color_numbers_coloring_method_page.sizePolicy().hasHeightForWidth())
        self.color_numbers_coloring_method_page.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.color_numbers_coloring_method_page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(4, -1, 0, -1)
        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 2, 0, 1, 3)

        self.colors_count_label = QLabel(self.color_numbers_coloring_method_page)
        self.colors_count_label.setObjectName(u"colors_count_label")
        sizePolicy2.setHeightForWidth(self.colors_count_label.sizePolicy().hasHeightForWidth())
        self.colors_count_label.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.colors_count_label, 0, 0, 1, 2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.colors_count_methods_label = QLabel(self.color_numbers_coloring_method_page)
        self.colors_count_methods_label.setObjectName(u"colors_count_methods_label")
        sizePolicy2.setHeightForWidth(self.colors_count_methods_label.sizePolicy().hasHeightForWidth())
        self.colors_count_methods_label.setSizePolicy(sizePolicy2)
        self.colors_count_methods_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.colors_count_methods_label)

        self.first_colors_count_method_radio_button = QRadioButton(self.color_numbers_coloring_method_page)
        self.first_colors_count_method_radio_button.setObjectName(u"first_colors_count_method_radio_button")
        self.first_colors_count_method_radio_button.setChecked(True)

        self.verticalLayout_3.addWidget(self.first_colors_count_method_radio_button)

        self.second_colors_count_method_radio_button = QRadioButton(self.color_numbers_coloring_method_page)
        self.second_colors_count_method_radio_button.setObjectName(u"second_colors_count_method_radio_button")

        self.verticalLayout_3.addWidget(self.second_colors_count_method_radio_button)

        self.third_colors_count_method_radio_button = QRadioButton(self.color_numbers_coloring_method_page)
        self.third_colors_count_method_radio_button.setObjectName(u"third_colors_count_method_radio_button")

        self.verticalLayout_3.addWidget(self.third_colors_count_method_radio_button)

        self.gridLayout_2.addLayout(self.verticalLayout_3, 3, 0, 1, 3)

        self.colors_count_slider = QSlider(self.color_numbers_coloring_method_page)
        self.colors_count_slider.setObjectName(u"colors_count_slider")
        self.colors_count_slider.setMinimum(2)
        self.colors_count_slider.setMaximum(255)
        self.colors_count_slider.setPageStep(1)
        self.colors_count_slider.setValue(10)
        self.colors_count_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.colors_count_slider, 1, 0, 1, 3)

        self.colors_count_value_label = QLabel(self.color_numbers_coloring_method_page)
        self.colors_count_value_label.setObjectName(u"colors_count_value_label")
        self.colors_count_value_label.setTextFormat(Qt.PlainText)
        self.colors_count_value_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.colors_count_value_label, 0, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 9)
        self.gridLayout_2.setColumnStretch(1, 9)
        self.gridLayout_2.setColumnStretch(2, 4)

        self.verticalLayout_5.addLayout(self.gridLayout_2)

        self.coloring_method_stacked_widget.addWidget(self.color_numbers_coloring_method_page)
        self.color_palette_coloring_method_page = QWidget()
        self.color_palette_coloring_method_page.setObjectName(u"color_palette_coloring_method_page")
        sizePolicy.setHeightForWidth(self.color_palette_coloring_method_page.sizePolicy().hasHeightForWidth())
        self.color_palette_coloring_method_page.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.color_palette_coloring_method_page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.color_palette_methods_label = QLabel(self.color_palette_coloring_method_page)
        self.color_palette_methods_label.setObjectName(u"color_palette_methods_label")
        sizePolicy2.setHeightForWidth(self.color_palette_methods_label.sizePolicy().hasHeightForWidth())
        self.color_palette_methods_label.setSizePolicy(sizePolicy2)
        self.color_palette_methods_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.color_palette_methods_label)

        self.first_color_palette_method_radio_button = QRadioButton(self.color_palette_coloring_method_page)
        self.first_color_palette_method_radio_button.setObjectName(u"first_color_palette_method_radio_button")
        self.first_color_palette_method_radio_button.setChecked(True)

        self.verticalLayout_4.addWidget(self.first_color_palette_method_radio_button)

        self.second_color_palette_method_radio_button = QRadioButton(self.color_palette_coloring_method_page)
        self.second_color_palette_method_radio_button.setObjectName(u"second_color_palette_method_radio_button")

        self.verticalLayout_4.addWidget(self.second_color_palette_method_radio_button)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_4.addItem(self.verticalSpacer_9)

        self.gridLayout_4.addLayout(self.verticalLayout_4, 4, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 3, 0, 1, 1)

        self.colors_palette_label = QLabel(self.color_palette_coloring_method_page)
        self.colors_palette_label.setObjectName(u"colors_palette_label")
        sizePolicy2.setHeightForWidth(self.colors_palette_label.sizePolicy().hasHeightForWidth())
        self.colors_palette_label.setSizePolicy(sizePolicy2)
        self.colors_palette_label.setFont(font)

        self.gridLayout_4.addWidget(self.colors_palette_label, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, -1, 16, -1)
        self.colors_palette_edit = QPlainTextEdit(self.color_palette_coloring_method_page)
        self.colors_palette_edit.setObjectName(u"colors_palette_edit")
        sizePolicy1.setHeightForWidth(self.colors_palette_edit.sizePolicy().hasHeightForWidth())
        self.colors_palette_edit.setSizePolicy(sizePolicy1)
        self.colors_palette_edit.setMinimumSize(QSize(0, 150))
        self.colors_palette_edit.setDocumentTitle(u"")

        self.horizontalLayout_2.addWidget(self.colors_palette_edit)

        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.verticalLayout_6.addLayout(self.gridLayout_4)

        self.coloring_method_stacked_widget.addWidget(self.color_palette_coloring_method_page)

        self.gridLayout_3.addWidget(self.coloring_method_stacked_widget, 20, 0, 1, 3)

        self.width_slider = QSlider(self.mosaic_configurator_scroll_area_widget)
        self.width_slider.setObjectName(u"width_slider")
        sizePolicy2.setHeightForWidth(self.width_slider.sizePolicy().hasHeightForWidth())
        self.width_slider.setSizePolicy(sizePolicy2)
        self.width_slider.setMinimum(1)
        self.width_slider.setMaximum(1)
        self.width_slider.setPageStep(1)
        self.width_slider.setOrientation(Qt.Horizontal)
        self.width_slider.setTickPosition(QSlider.NoTicks)

        self.gridLayout_3.addWidget(self.width_slider, 8, 0, 1, 3)

        self.preserving_proportions_check_box = QCheckBox(self.mosaic_configurator_scroll_area_widget)
        self.preserving_proportions_check_box.setObjectName(u"preserving_proportions_check_box")
        self.preserving_proportions_check_box.setChecked(True)

        self.gridLayout_3.addWidget(self.preserving_proportions_check_box, 6, 0, 1, 3)

        self.sizes_label = QLabel(self.mosaic_configurator_scroll_area_widget)
        self.sizes_label.setObjectName(u"sizes_label")
        self.sizes_label.setFont(font)
        self.sizes_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.sizes_label, 5, 1, 1, 1)

        self.multiplier_slider = QSlider(self.mosaic_configurator_scroll_area_widget)
        self.multiplier_slider.setObjectName(u"multiplier_slider")
        self.multiplier_slider.setMinimum(1)
        self.multiplier_slider.setMaximum(100)
        self.multiplier_slider.setPageStep(1)
        self.multiplier_slider.setValue(10)
        self.multiplier_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.multiplier_slider, 16, 0, 1, 3)

        self.verticalSpacer_11 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_11, 24, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer, 4, 0, 1, 3)

        self.verticalSpacer_10 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_10, 2, 1, 1, 1)

        self.create_mosaic_button = QPushButton(self.mosaic_configurator_scroll_area_widget)
        self.create_mosaic_button.setObjectName(u"create_mosaic_button")
        self.create_mosaic_button.setEnabled(False)

        self.gridLayout_3.addWidget(self.create_mosaic_button, 29, 1, 1, 1)

        self.create_mosaic_live_check_box = QCheckBox(self.mosaic_configurator_scroll_area_widget)
        self.create_mosaic_live_check_box.setObjectName(u"create_mosaic_live_check_box")
        self.create_mosaic_live_check_box.setEnabled(False)

        self.gridLayout_3.addWidget(self.create_mosaic_live_check_box, 28, 1, 1, 1)

        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 3)
        self.gridLayout_3.setColumnStretch(2, 1)
        self.mosaic_configurator_scroll_area.setWidget(self.mosaic_configurator_scroll_area_widget)

        self.verticalLayout_2.addWidget(self.mosaic_configurator_scroll_area)

        self.configuration_tab_widget.addTab(self.mosaic_configurator, "")
        self.mesh_configurator = QWidget()
        self.mesh_configurator.setObjectName(u"mesh_configurator")
        self.verticalLayout_8 = QVBoxLayout(self.mesh_configurator)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.mesh_configurator_scroll_area = QScrollArea(self.mesh_configurator)
        self.mesh_configurator_scroll_area.setObjectName(u"mesh_configurator_scroll_area")
        self.mesh_configurator_scroll_area.setFrameShape(QFrame.NoFrame)
        self.mesh_configurator_scroll_area.setLineWidth(0)
        self.mesh_configurator_scroll_area.setWidgetResizable(True)
        self.mesh_configurator_scroll_area_widget = QWidget()
        self.mesh_configurator_scroll_area_widget.setObjectName(u"mesh_configurator_scroll_area_widget")
        self.mesh_configurator_scroll_area_widget.setGeometry(QRect(0, -7, 383, 982))
        self.gridLayout_5 = QGridLayout(self.mesh_configurator_scroll_area_widget)
        self.gridLayout_5.setSpacing(10)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(4, 4, 4, 4)
        self.axis_y_count_slider = QSlider(self.mesh_configurator_scroll_area_widget)
        self.axis_y_count_slider.setObjectName(u"axis_y_count_slider")
        self.axis_y_count_slider.setMinimum(1)
        self.axis_y_count_slider.setMaximum(100)
        self.axis_y_count_slider.setSingleStep(5)
        self.axis_y_count_slider.setPageStep(1)
        self.axis_y_count_slider.setValue(5)
        self.axis_y_count_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.axis_y_count_slider, 11, 0, 1, 3)

        self.axis_z_multiplier_slider_value_label = QLabel(self.mesh_configurator_scroll_area_widget)
        self.axis_z_multiplier_slider_value_label.setObjectName(u"axis_z_multiplier_slider_value_label")
        self.axis_z_multiplier_slider_value_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.axis_z_multiplier_slider_value_label, 18, 2, 1, 1)

        self.open_and_show_mesh_button = QPushButton(self.mesh_configurator_scroll_area_widget)
        self.open_and_show_mesh_button.setObjectName(u"open_and_show_mesh_button")

        self.gridLayout_5.addWidget(self.open_and_show_mesh_button, 1, 1, 1, 1)

        self.axis_y_count_label = QLabel(self.mesh_configurator_scroll_area_widget)
        self.axis_y_count_label.setObjectName(u"axis_y_count_label")

        self.gridLayout_5.addWidget(self.axis_y_count_label, 10, 0, 1, 2)

        self.verticalSpacer_22 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_22, 6, 0, 1, 3)

        self.axis_x_offset_slider_value_label = QLabel(self.mesh_configurator_scroll_area_widget)
        self.axis_x_offset_slider_value_label.setObjectName(u"axis_x_offset_slider_value_label")
        self.axis_x_offset_slider_value_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.axis_x_offset_slider_value_label, 22, 2, 1, 1)

        self.axis_x_offset_label = QLabel(self.mesh_configurator_scroll_area_widget)
        self.axis_x_offset_label.setObjectName(u"axis_x_offset_label")

        self.gridLayout_5.addWidget(self.axis_x_offset_label, 22, 0, 1, 2)

        self.axis_y_offset_slider = QSlider(self.mesh_configurator_scroll_area_widget)
        self.axis_y_offset_slider.setObjectName(u"axis_y_offset_slider")
        self.axis_y_offset_slider.setMinimum(0)
        self.axis_y_offset_slider.setMaximum(100)
        self.axis_y_offset_slider.setPageStep(1)
        self.axis_y_offset_slider.setValue(15)
        self.axis_y_offset_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.axis_y_offset_slider, 25, 0, 1, 3)

        self.verticalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_16, 20, 0, 1, 3)

        self.same_offset_by_axis_check_box = QCheckBox(self.mesh_configurator_scroll_area_widget)
        self.same_offset_by_axis_check_box.setObjectName(u"same_offset_by_axis_check_box")
        self.same_offset_by_axis_check_box.setChecked(True)

        self.gridLayout_5.addWidget(self.same_offset_by_axis_check_box, 21, 0, 1, 3)

        self.axis_y_multiplier_slider = QSlider(self.mesh_configurator_scroll_area_widget)
        self.axis_y_multiplier_slider.setObjectName(u"axis_y_multiplier_slider")
        self.axis_y_multiplier_slider.setMinimum(1)
        self.axis_y_multiplier_slider.setMaximum(100)
        self.axis_y_multiplier_slider.setPageStep(1)
        self.axis_y_multiplier_slider.setValue(10)
        self.axis_y_multiplier_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.axis_y_multiplier_slider, 17, 0, 1, 3)

        self.file_number_slider = QSlider(self.mesh_configurator_scroll_area_widget)
        self.file_number_slider.setObjectName(u"file_number_slider")
        self.file_number_slider.setMinimum(1)
        self.file_number_slider.setMaximum(1)
        self.file_number_slider.setPageStep(1)
        self.file_number_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.file_number_slider, 31, 0, 1, 3)

        self.verticalSpacer_17 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_17, 26, 0, 1, 3)

        self.verticalSpacer_19 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_19, 32, 0, 1, 3)

        self.same_count_by_axis_check_box = QCheckBox(self.mesh_configurator_scroll_area_widget)
        self.same_count_by_axis_check_box.setObjectName(u"same_count_by_axis_check_box")
        self.same_count_by_axis_check_box.setChecked(True)

        self.gridLayout_5.addWidget(self.same_count_by_axis_check_box, 7, 0, 1, 3)

        self.verticalSpacer_18 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_18, 29, 0, 1, 3)

        self.axis_x_multiplier_slider = QSlider(self.mesh_configurator_scroll_area_widget)
        self.axis_x_multiplier_slider.setObjectName(u"axis_x_multiplier_slider")
        self.axis_x_multiplier_slider.setMinimum(1)
        self.axis_x_multiplier_slider.setMaximum(100)
        self.axis_x_multiplier_slider.setPageStep(1)
        self.axis_x_multiplier_slider.setValue(10)
        self.axis_x_multiplier_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.axis_x_multiplier_slider, 15, 0, 1, 3)

        self.create_mesh_live_check_box = QCheckBox(self.mesh_configurator_scroll_area_widget)
        self.create_mesh_live_check_box.setObjectName(u"create_mesh_live_check_box")

        self.gridLayout_5.addWidget(self.create_mesh_live_check_box, 33, 1, 1, 1)

        self.show_frame_check_box = QCheckBox(self.mesh_configurator_scroll_area_widget)
        self.show_frame_check_box.setObjectName(u"show_frame_check_box")

        self.gridLayout_5.addWidget(self.show_frame_check_box, 4, 0, 1, 3)

        self.total_count_slider_value_label = QLabel(self.mesh_configurator_scroll_area_widget)
        self.total_count_slider_value_label.setObjectName(u"total_count_slider_value_label")
        self.total_count_slider_value_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.total_count_slider_value_label, 27, 2, 1, 1)

        self.axis_y_count_slider_value_label = QLabel(self.mesh_configurator_scroll_area_widget)
        self.axis_y_count_slider_value_label.setObjectName(u"axis_y_count_slider_value_label")
        self.axis_y_count_slider_value_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.axis_y_count_slider_value_label, 10, 2, 1, 1)

        self.axis_z_multiplier_label = QLabel(self.mesh_configurator_scroll_area_widget)
        self.axis_z_multiplier_label.setObjectName(u"axis_z_multiplier_label")

        self.gridLayout_5.addWidget(self.axis_z_multiplier_label, 18, 0, 1, 2)

        self.create_mesh_button = QPushButton(self.mesh_configurator_scroll_area_widget)
        self.create_mesh_button.setObjectName(u"create_mesh_button")

        self.gridLayout_5.addWidget(self.create_mesh_button, 34, 1, 1, 1)

        self.file_number_label = QLabel(self.mesh_configurator_scroll_area_widget)
        self.file_number_label.setObjectName(u"file_number_label")

        self.gridLayout_5.addWidget(self.file_number_label, 30, 0, 1, 2)

        self.verticalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_15, 12, 0, 1, 3)

        self.axis_y_multiplier_label = QLabel(self.mesh_configurator_scroll_area_widget)
        self.axis_y_multiplier_label.setObjectName(u"axis_y_multiplier_label")

        self.gridLayout_5.addWidget(self.axis_y_multiplier_label, 16, 0, 1, 2)

        self.axis_y_offset_label = QLabel(self.mesh_configurator_scroll_area_widget)
        self.axis_y_offset_label.setObjectName(u"axis_y_offset_label")

        self.gridLayout_5.addWidget(self.axis_y_offset_label, 24, 0, 1, 2)

        self.axis_x_multiplier_slider_value_label = QLabel(self.mesh_configurator_scroll_area_widget)
        self.axis_x_multiplier_slider_value_label.setObjectName(u"axis_x_multiplier_slider_value_label")
        self.axis_x_multiplier_slider_value_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.axis_x_multiplier_slider_value_label, 14, 2, 1, 1)

        self.axis_x_offset_slider = QSlider(self.mesh_configurator_scroll_area_widget)
        self.axis_x_offset_slider.setObjectName(u"axis_x_offset_slider")
        self.axis_x_offset_slider.setMinimum(0)
        self.axis_x_offset_slider.setMaximum(100)
        self.axis_x_offset_slider.setPageStep(1)
        self.axis_x_offset_slider.setValue(15)
        self.axis_x_offset_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.axis_x_offset_slider, 23, 0, 1, 3)

        self.verticalSpacer_20 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout_5.addItem(self.verticalSpacer_20, 35, 1, 1, 1)

        self.total_count_label = QLabel(self.mesh_configurator_scroll_area_widget)
        self.total_count_label.setObjectName(u"total_count_label")

        self.gridLayout_5.addWidget(self.total_count_label, 27, 0, 1, 2)

        self.axis_x_count_label = QLabel(self.mesh_configurator_scroll_area_widget)
        self.axis_x_count_label.setObjectName(u"axis_x_count_label")

        self.gridLayout_5.addWidget(self.axis_x_count_label, 8, 0, 1, 2)

        self.axis_z_multiplier_slider = QSlider(self.mesh_configurator_scroll_area_widget)
        self.axis_z_multiplier_slider.setObjectName(u"axis_z_multiplier_slider")
        self.axis_z_multiplier_slider.setMinimum(1)
        self.axis_z_multiplier_slider.setMaximum(100)
        self.axis_z_multiplier_slider.setPageStep(1)
        self.axis_z_multiplier_slider.setValue(10)
        self.axis_z_multiplier_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.axis_z_multiplier_slider, 19, 0, 1, 3)

        self.axis_x_multiplier_label = QLabel(self.mesh_configurator_scroll_area_widget)
        self.axis_x_multiplier_label.setObjectName(u"axis_x_multiplier_label")

        self.gridLayout_5.addWidget(self.axis_x_multiplier_label, 14, 0, 1, 2)

        self.file_number_slider_value_label = QLabel(self.mesh_configurator_scroll_area_widget)
        self.file_number_slider_value_label.setObjectName(u"file_number_slider_value_label")
        self.file_number_slider_value_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.file_number_slider_value_label, 30, 2, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_21, 0, 0, 1, 3)

        self.same_multiplier_by_axis_check_box = QCheckBox(self.mesh_configurator_scroll_area_widget)
        self.same_multiplier_by_axis_check_box.setObjectName(u"same_multiplier_by_axis_check_box")
        self.same_multiplier_by_axis_check_box.setChecked(True)

        self.gridLayout_5.addWidget(self.same_multiplier_by_axis_check_box, 13, 0, 1, 3)

        self.axis_y_multiplier_slider_value_label = QLabel(self.mesh_configurator_scroll_area_widget)
        self.axis_y_multiplier_slider_value_label.setObjectName(u"axis_y_multiplier_slider_value_label")
        self.axis_y_multiplier_slider_value_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.axis_y_multiplier_slider_value_label, 16, 2, 1, 1)

        self.axis_x_count_slider = QSlider(self.mesh_configurator_scroll_area_widget)
        self.axis_x_count_slider.setObjectName(u"axis_x_count_slider")
        self.axis_x_count_slider.setMinimum(1)
        self.axis_x_count_slider.setMaximum(100)
        self.axis_x_count_slider.setPageStep(1)
        self.axis_x_count_slider.setValue(5)
        self.axis_x_count_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.axis_x_count_slider, 9, 0, 1, 3)

        self.total_count_slider = QSlider(self.mesh_configurator_scroll_area_widget)
        self.total_count_slider.setObjectName(u"total_count_slider")
        self.total_count_slider.setMinimum(1)
        self.total_count_slider.setMaximum(1000)
        self.total_count_slider.setPageStep(1)
        self.total_count_slider.setValue(15)
        self.total_count_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.total_count_slider, 28, 0, 1, 3)

        self.verticalSpacer_14 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_14, 2, 0, 1, 3)

        self.axis_x_count_slider_value_label = QLabel(self.mesh_configurator_scroll_area_widget)
        self.axis_x_count_slider_value_label.setObjectName(u"axis_x_count_slider_value_label")
        self.axis_x_count_slider_value_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.axis_x_count_slider_value_label, 8, 2, 1, 1)

        self.axis_y_offset_slider_value_label = QLabel(self.mesh_configurator_scroll_area_widget)
        self.axis_y_offset_slider_value_label.setObjectName(u"axis_y_offset_slider_value_label")
        self.axis_y_offset_slider_value_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.axis_y_offset_slider_value_label, 24, 2, 1, 1)

        self.same_axis_scale_check_box = QCheckBox(self.mesh_configurator_scroll_area_widget)
        self.same_axis_scale_check_box.setObjectName(u"same_axis_scale_check_box")
        self.same_axis_scale_check_box.setChecked(True)

        self.gridLayout_5.addWidget(self.same_axis_scale_check_box, 5, 0, 1, 3)

        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 3)
        self.gridLayout_5.setColumnStretch(2, 1)
        self.mesh_configurator_scroll_area.setWidget(self.mesh_configurator_scroll_area_widget)

        self.verticalLayout_8.addWidget(self.mesh_configurator_scroll_area)

        self.configuration_tab_widget.addTab(self.mesh_configurator, "")
        self.export_configurator = QWidget()
        self.export_configurator.setObjectName(u"export_configurator")
        self.verticalLayout_7 = QVBoxLayout(self.export_configurator)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.export_configurator_scroll_area = QScrollArea(self.export_configurator)
        self.export_configurator_scroll_area.setObjectName(u"export_configurator_scroll_area")
        self.export_configurator_scroll_area.setFrameShape(QFrame.NoFrame)
        self.export_configurator_scroll_area.setLineWidth(0)
        self.export_configurator_scroll_area.setWidgetResizable(True)
        self.export_configurator_scroll_area_widget = QWidget()
        self.export_configurator_scroll_area_widget.setObjectName(u"export_configurator_scroll_area_widget")
        self.export_configurator_scroll_area_widget.setGeometry(QRect(0, 0, 400, 551))
        self.gridLayout = QGridLayout(self.export_configurator_scroll_area_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.save_mosaic_mesh_button = QPushButton(self.export_configurator_scroll_area_widget)
        self.save_mosaic_mesh_button.setObjectName(u"save_mosaic_mesh_button")
        self.save_mosaic_mesh_button.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.save_mosaic_mesh_button.sizePolicy().hasHeightForWidth())
        self.save_mosaic_mesh_button.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.save_mosaic_mesh_button, 3, 1, 1, 1)

        self.save_mosaic_palette_button = QPushButton(self.export_configurator_scroll_area_widget)
        self.save_mosaic_palette_button.setObjectName(u"save_mosaic_palette_button")
        self.save_mosaic_palette_button.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.save_mosaic_palette_button.sizePolicy().hasHeightForWidth())
        self.save_mosaic_palette_button.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.save_mosaic_palette_button, 2, 1, 1, 1)

        self.save_mosaic_button = QPushButton(self.export_configurator_scroll_area_widget)
        self.save_mosaic_button.setObjectName(u"save_mosaic_button")
        self.save_mosaic_button.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.save_mosaic_button.sizePolicy().hasHeightForWidth())
        self.save_mosaic_button.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.save_mosaic_button, 1, 1, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_13, 4, 0, 1, 3)

        self.verticalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_12, 0, 0, 1, 3)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)
        self.export_configurator_scroll_area.setWidget(self.export_configurator_scroll_area_widget)

        self.verticalLayout_7.addWidget(self.export_configurator_scroll_area)

        self.configuration_tab_widget.addTab(self.export_configurator, "")

        self.central_layout.addWidget(self.configuration_tab_widget)

        self.central_layout.setStretch(0, 64)
        self.central_layout.setStretch(1, 46)

        self.horizontalLayout.addLayout(self.central_layout)

        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)

        self.show_stacked_widget.setCurrentIndex(0)
        self.configuration_tab_widget.setCurrentIndex(0)
        self.coloring_method_stacked_widget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.image_label.setText("")
        self.overlay_label.setText(
            QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.no_overlay_radio_button.setText(QCoreApplication.translate("MainWindow",
                                                                        u"\u0411\u0435\u0437 \u043d\u0430\u043b\u043e\u0436\u0435\u043d\u0438\u044f",
                                                                        None))
        self.grid_radio_button.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0442\u043a\u0430", None))
        self.numbers_radio_button.setText(QCoreApplication.translate("MainWindow",
                                                                     u"\u041d\u043e\u043c\u0435\u0440\u0430 \u0446\u0432\u0435\u0442\u043e\u0432",
                                                                     None))
        self.grid_and_numbers_radio_button.setText(QCoreApplication.translate("MainWindow",
                                                                              u"\u0421\u0435\u0442\u043a\u0430 \u0438 \u043d\u043e\u043c\u0435\u0440\u0430 \u0446\u0432\u0435\u0442\u043e\u0432",
                                                                              None))
        self.grid_and_numbers_with_white_background_radio_button.setText(QCoreApplication.translate("MainWindow",
                                                                                                    u"\u0421\u0435\u0442\u043a\u0430 \u0438 \u043d\u043e\u043c\u0435\u0440\u0430 \u0446\u0432\u0435\u0442\u043e\u0432 \u0441 \u0431\u0435\u043b\u044b\u043c \u0444\u043e\u043d\u043e\u043c",
                                                                                                    None))
        self.height_label.setText(QCoreApplication.translate("MainWindow",
                                                             u"\u0412\u044b\u0441\u043e\u0442\u0430 \u043c\u043e\u0437\u0430\u0438\u043a\u0438 (\u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0438\u043a\u0441\u0435\u043b\u0435\u0439)",
                                                             None))
        self.multiplier_slider_value_label.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.numbers_size_label.setText(QCoreApplication.translate("MainWindow",
                                                                   u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 \u043d\u043e\u043c\u0435\u0440\u043e\u0432",
                                                                   None))
        self.colors_count_method_radio_button.setText(QCoreApplication.translate("MainWindow",
                                                                                 u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0446\u0432\u0435\u0442\u043e\u0432",
                                                                                 None))
        self.color_palette_method_radio_button.setText(QCoreApplication.translate("MainWindow",
                                                                                  u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 \u043f\u0430\u043b\u0438\u0442\u0440\u044b \u0446\u0432\u0435\u0442\u043e\u0432",
                                                                                  None))
        self.coloring_method_label.setText(QCoreApplication.translate("MainWindow",
                                                                      u"\u0421\u043f\u043e\u0441\u043e\u0431 \u0440\u0430\u0441\u043a\u0440\u0430\u0441\u043a\u0438",
                                                                      None))
        self.import_image_button.setText(QCoreApplication.translate("MainWindow",
                                                                    u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f",
                                                                    None))
        self.width_label.setText(QCoreApplication.translate("MainWindow",
                                                            u"\u0428\u0438\u0440\u0438\u043d\u0430 \u043c\u043e\u0437\u0430\u0438\u043a\u0438 (\u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0438\u043a\u0441\u0435\u043b\u0435\u0439)",
                                                            None))
        self.width_slider_value_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.multiplier_label.setText(QCoreApplication.translate("MainWindow",
                                                                 u"\u041c\u0443\u043b\u044c\u0442\u0438\u043f\u043b\u0438\u043a\u0430\u0442\u043e\u0440\n"
                                                                 "(\u0441\u043e\u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u0435 \u043f\u0438\u043a\u0441\u0435\u043b\u0435\u0439 \u043c\u043e\u0437\u0430\u0438\u043a\u0438 \u043a\n"
                                                                 "\u043f\u0438\u043a\u0441\u0435\u043b\u044f\u043c \u044d\u0441\u043f\u043e\u0440\u0442\u0438\u0440\u0443\u0435\u043c\u043e\u0433\u043e \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f)",
                                                                 None))
        self.show_imported_image_button.setText(QCoreApplication.translate("MainWindow",
                                                                           u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435",
                                                                           None))
        self.numbers_size_slider_value_label.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.height_slider_value_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.colors_count_label.setText(QCoreApplication.translate("MainWindow",
                                                                   u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0446\u0432\u0435\u0442\u043e\u0432",
                                                                   None))
        self.colors_count_methods_label.setText(QCoreApplication.translate("MainWindow",
                                                                           u"\u0421\u043f\u043e\u0441\u043e\u0431 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u043c\u043e\u0437\u0430\u0438\u043a\u0438",
                                                                           None))
        self.first_colors_count_method_radio_button.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043f\u043e\u0441\u043e\u0431 \u21161", None))
        self.second_colors_count_method_radio_button.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043f\u043e\u0441\u043e\u0431 \u21162", None))
        self.third_colors_count_method_radio_button.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043f\u043e\u0441\u043e\u0431 \u21163", None))
        self.colors_count_value_label.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.color_palette_methods_label.setText(QCoreApplication.translate("MainWindow",
                                                                            u"\u0421\u043f\u043e\u0441\u043e\u0431 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u043c\u043e\u0437\u0430\u0438\u043a\u0438",
                                                                            None))
        self.first_color_palette_method_radio_button.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043f\u043e\u0441\u043e\u0431 \u21161", None))
        self.second_color_palette_method_radio_button.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043f\u043e\u0441\u043e\u0431 \u21162", None))
        self.colors_palette_label.setText(QCoreApplication.translate("MainWindow",
                                                                     u"\u0412\u0432\u043e\u0434 \u043f\u0430\u043b\u0438\u0442\u0440\u044b \u0446\u0432\u0435\u0442\u043e\u0432 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 hex.\n"
                                                                     "\u041e\u0434\u043d\u0430 \u0441\u0442\u0440\u043e\u043a\u0430 - \u043e\u0434\u0438\u043d \u0446\u0432\u0435\u0442 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 #RRGGBB",
                                                                     None))
        self.colors_palette_edit.setPlainText(QCoreApplication.translate("MainWindow", u"#FFAAAA\n"
                                                                                       "#FFFFFF\n"
                                                                                       "#000000\n"
                                                                                       "#FF00FF\n"
                                                                                       "#00FFFF\n"
                                                                                       "#00FF00\n"
                                                                                       "#0E0E0E", None))
        self.preserving_proportions_check_box.setText(QCoreApplication.translate("MainWindow",
                                                                                 u"\u0421\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435 \u043f\u0440\u043e\u043f\u043e\u0440\u0446\u0438\u0439",
                                                                                 None))
        self.sizes_label.setText(
            QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440\u044b", None))
        self.create_mosaic_button.setText(QCoreApplication.translate("MainWindow",
                                                                     u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043c\u043e\u0437\u0430\u0438\u043a\u0443",
                                                                     None))
        self.create_mosaic_live_check_box.setText(QCoreApplication.translate("MainWindow",
                                                                             u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043c\u043e\u0437\u0430\u0438\u043a\u0438",
                                                                             None))
        self.configuration_tab_widget.setTabText(self.configuration_tab_widget.indexOf(self.mosaic_configurator),
                                                 QCoreApplication.translate("MainWindow",
                                                                            u"\u041c\u043e\u0437\u0430\u0438\u043a\u0430",
                                                                            None))
        self.axis_z_multiplier_slider_value_label.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.open_and_show_mesh_button.setText(QCoreApplication.translate("MainWindow",
                                                                          u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b \u0441\u0435\u0442\u043a\u0438 \u0438 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u044c",
                                                                          None))
        self.axis_y_count_label.setText(QCoreApplication.translate("MainWindow",
                                                                   u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u043f\u043e \u043e\u0441\u0438 Y",
                                                                   None))
        self.axis_x_offset_slider_value_label.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.axis_x_offset_label.setText(QCoreApplication.translate("MainWindow",
                                                                    u"\u0421\u0434\u0432\u0438\u0433 \u043f\u043e \u043e\u0441\u0438 X",
                                                                    None))
        self.same_offset_by_axis_check_box.setText(QCoreApplication.translate("MainWindow",
                                                                              u"\u0421\u0434\u0432\u0438\u0433 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u043e\u0434\u0438\u043d\u0430\u043a\u043e\u0432 \u043f\u043e \u043e\u0431\u043e\u0438\u043c \u043e\u0441\u044f\u043c",
                                                                              None))
        self.same_count_by_axis_check_box.setText(QCoreApplication.translate("MainWindow",
                                                                             u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u043e\u0434\u0438\u043d\u0430\u043a\u043e\u0432\u043e \u043f\u043e \u043e\u0431\u043e\u0438\u043c \u043e\u0441\u044f\u043c",
                                                                             None))
        self.create_mesh_live_check_box.setText(QCoreApplication.translate("MainWindow",
                                                                           u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0441\u0435\u0442\u043a\u0438",
                                                                           None))
        self.show_frame_check_box.setText(QCoreApplication.translate("MainWindow",
                                                                     u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043a\u0430\u0440\u043a\u0430\u0441\u0430",
                                                                     None))
        self.total_count_slider_value_label.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.axis_y_count_slider_value_label.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.axis_z_multiplier_label.setText(QCoreApplication.translate("MainWindow",
                                                                        u"\u041c\u0443\u043b\u044c\u0442\u0438\u043f\u043b\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043e \u043e\u0441\u0438 Z",
                                                                        None))
        self.create_mesh_button.setText(QCoreApplication.translate("MainWindow",
                                                                   u"\u041e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u044c \u0441\u0435\u0442\u043a\u0443",
                                                                   None))
        self.file_number_label.setText(QCoreApplication.translate("MainWindow",
                                                                  u"\u0412\u044b\u0431\u043e\u0440 \u043d\u043e\u043c\u0435\u0440\u0430 \u0444\u0430\u0439\u043b\u0430 \u0434\u043b\u044f \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f",
                                                                  None))
        self.axis_y_multiplier_label.setText(QCoreApplication.translate("MainWindow",
                                                                        u"\u041c\u0443\u043b\u044c\u0442\u0438\u043f\u043b\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043e \u043e\u0441\u0438 Y",
                                                                        None))
        self.axis_y_offset_label.setText(QCoreApplication.translate("MainWindow",
                                                                    u"\u0421\u0434\u0432\u0438\u0433 \u043f\u043e \u043e\u0441\u0438 Y",
                                                                    None))
        self.axis_x_multiplier_slider_value_label.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.total_count_label.setText(QCoreApplication.translate("MainWindow",
                                                                  u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432",
                                                                  None))
        self.axis_x_count_label.setText(QCoreApplication.translate("MainWindow",
                                                                   u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 \u043f\u043e \u043e\u0441\u0438 X",
                                                                   None))
        self.axis_x_multiplier_label.setText(QCoreApplication.translate("MainWindow",
                                                                        u"\u041c\u0443\u043b\u044c\u0442\u0438\u043f\u043b\u0438\u043a\u0430\u0442\u043e\u0440 \u043f\u043e \u043e\u0441\u0438 X",
                                                                        None))
        self.file_number_slider_value_label.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.same_multiplier_by_axis_check_box.setText(QCoreApplication.translate("MainWindow",
                                                                                  u"\u041c\u0443\u043b\u044c\u0442\u0438\u043f\u043b\u0438\u043a\u0430\u0442\u043e\u0440 \u043e\u0434\u0438\u043d\u0430\u043a\u043e\u0432 \u043f\u043e \u0432\u0441\u0435\u043c \u043e\u0441\u044f\u043c",
                                                                                  None))
        self.axis_y_multiplier_slider_value_label.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.axis_x_count_slider_value_label.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.axis_y_offset_slider_value_label.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.same_axis_scale_check_box.setText(QCoreApplication.translate("MainWindow",
                                                                          u"\u041e\u0434\u0438\u043d\u0430\u043a\u043e\u0432\u0430\u044f \u0448\u043a\u0430\u043b\u0430 \u043f\u043e \u0432\u0441\u0435\u043c \u043e\u0441\u044f\u043c",
                                                                          None))
        self.configuration_tab_widget.setTabText(self.configuration_tab_widget.indexOf(self.mesh_configurator),
                                                 QCoreApplication.translate("MainWindow",
                                                                            u"\u0421\u0435\u0442\u043a\u0430", None))
        self.save_mosaic_mesh_button.setText(QCoreApplication.translate("MainWindow",
                                                                        u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b \u0441\u0435\u0442\u043a\u0438 \u043c\u043e\u0437\u0430\u0438\u043a\u0438",
                                                                        None))
        self.save_mosaic_palette_button.setText(QCoreApplication.translate("MainWindow",
                                                                           u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043f\u0430\u043b\u0438\u0442\u0440\u0443 \u0446\u0432\u0435\u0442\u043e\u0432 \u043c\u043e\u0437\u0430\u0438\u043a\u0438",
                                                                           None))
        self.save_mosaic_button.setText(QCoreApplication.translate("MainWindow",
                                                                   u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043c\u043e\u0437\u0430\u0438\u043a\u0443",
                                                                   None))
        self.configuration_tab_widget.setTabText(self.configuration_tab_widget.indexOf(self.export_configurator),
                                                 QCoreApplication.translate("MainWindow",
                                                                            u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442",
                                                                            None))
    # retranslateUi
