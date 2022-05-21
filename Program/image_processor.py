import math
import os.path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from PIL.Image import BOX
from pyxelate import Pyx, Pal


# -------------- utils function --------------

def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return f"{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"


def hex_to_rgb(hex: str) -> tuple[int, int, int]:
    hex = hex.replace("#", "")
    return int(hex[0:2], 16), int(hex[2:4], 16), int(hex[4:6], 16)


def is_light_color(rgb: tuple[int, int, int]) -> bool:
    return math.sqrt(0.299 * rgb[0] ** 2 + 0.587 * rgb[1] ** 2 + 0.114 * rgb[2] ** 2) > 127.5


def colors_palette_from_image(image: Image) -> list[tuple[int, int, int]]:
    colors = set()
    for x in range(image.width):
        for y in range(image.height):
            colors.add(image.getpixel((x, y)))
    return list(colors)


# палитра цветов из изображения с палитрой
def colors_palette_from_image_with_palette(image: Image) -> list | None:
    if image.getpalette() is not None:
        original_palette = image.getpalette()
        return [(original_palette[i], original_palette[i + 1], original_palette[i + 2]) for i in
                range(0, len(original_palette), 3)]
    return None


# палитра определённого количества цветов из изображения pyxelate
def colors_palette_from_image_pyxelate(image: Image, colors: int) -> list[tuple[int]]:
    pyx = Pyx(palette=colors).fit(np.array(image))
    return [tuple(color[0]) for color in pyx.colors]


# конвертация hex цветов в список rgb int цветов
def colors_palette_from_hex_colors(hex_colors: list[str]) -> list[tuple[int, int, int]]:
    # hex_colors = ["#FFAAAA", "#FFFFFF", "#000000", "#FF00FF", "#00FFFF", "#00FF00", "#0E0E0E"]
    return [hex_to_rgb(color) for color in hex_colors]


# конвертация из плоского списка в rgb int список
def colors_palette_from_flat_colors_list(flat_colors: list[int]) -> list[tuple[int, int, int]]:
    # flat_colors = [255, 0, 0, 0, 255, 0, 0, 0, 255, 255, 165, 0, 255, 255, 0]
    return [(flat_colors[i], flat_colors[i + 1], flat_colors[i + 2]) for i in range(0, len(flat_colors), 3)]


# конвертация rgb int в плоский список
def flat_colors_list_from_colors_palette(colors_palette: tuple[tuple[int, int, int]]) -> tuple[int]:
    # colors_palette = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 165, 0), (255, 255, 0)]
    return tuple([color for color_tuple in colors_palette for color in color_tuple])


# -------------- main functions --------------

def open_image(full_image_name: str, folder: str = "images/") -> Image:
    return Image.open(os.path.join(folder, full_image_name)).convert("RGB")


def save_image(image: Image, image_name: str, postfix: str = "", folder: str = "outputs/") -> None:
    image.save(os.path.join(folder, image_name + "_" + postfix + ".png"))


def quantize_image(image: Image, colors: int) -> Image:
    return image.quantize(colors=colors)


def resize_image(image: Image, width: int, height: int) -> Image:
    return image.resize((width, height))


def reresize_image(image: Image, width: int, height: int, multiplier: int) -> Image:
    return image.resize((width * multiplier, height * multiplier), resample=BOX).convert("RGB")


def palette_from_image(image: Image) -> Image:
    original_palette = image.getpalette()
    palette = []
    for i in range(0, len(original_palette), 3):
        palette.append((original_palette[i], original_palette[i + 1], original_palette[i + 2]))
    return palette


def colors_distribution(image: Image, palette) -> dict[tuple[int, int, int], int]:
    each_color_count = [0] * palette
    for i in range(image.width):
        for j in range(image.height):
            each_color_count[image.getpixel((i, j))] += 1

    return {color: count for (color, count) in zip(palette, each_color_count)}


def save_colors_distribution(distribution_file_name: str, each_color_palette: dict[tuple[int, int, int], int],
                             folder: str = "outputs/"):
    with open(os.path.join(folder, distribution_file_name), "w", encoding="utf-8") as file:
        file.write("№     #RRGGBB   Count\n")
        for (number, (color, count)) in enumerate(each_color_palette.items()):
            file.write(f"{number + 1:<5} #{color[0]:02X}{color[1]:02X}{color[2]:02X}   {count}\n")


def save_colors_distribution_for_image(image_name: str, each_color_palette: dict[tuple[int, int, int], int],
                                       folder: str = "outputs/") -> None:
    with open(os.path.join(folder, f"{image_name}_colors.txt"), "w", encoding="utf-8") as file:
        file.write("№     #RRGGBB   Count\n")
        for (number, (color, count)) in enumerate(each_color_palette.items()):
            file.write(f"{number + 1:<5} #{color[0]:02X}{color[1]:02X}{color[2]:02X}   {count}\n")


def save_colors_distribution_to_color_images(image_name: str, each_color_palette: dict[tuple[int, int, int], int],
                                             width: int, height: int, folder: str = "outputs/colors/") -> None:
    for (number, (color, count)) in enumerate(each_color_palette.items()):
        Image.new("RGB", (width, height), color=color).save(
            os.path.join(folder, f"{image_name} - {number + 1} {color[0]:02X}{color[1]:02X}{color[2]:02X} {count}.png"))


def create_image_with_numbers(image: Image, palette: list[tuple[int, int, int]], width: int, height: int,
                              multiplier: int,
                              numbers_size: int) -> Image:
    image_with_numbers = image.copy()
    image_with_numbers_draw = ImageDraw.Draw(image_with_numbers)
    for x in range(0, width, multiplier):
        for y in range(0, height, multiplier):
            xy = (x + multiplier * 0.5, y + multiplier * 0.5)
            color = image.getpixel(xy)
            image_with_numbers_draw.text(xy, str(palette.index(color) + 1),
                                         fill="black" if is_light_color(color) else "white",
                                         anchor="mm", font=ImageFont.truetype("arial.ttf", numbers_size))
    return image_with_numbers


def create_image_with_grid(image: Image, width: int, height: int, multiplier: int) -> Image:
    image_with_grid = image.copy()
    image_with_grid_draw = ImageDraw.Draw(image_with_grid)
    for x in range(0, width, multiplier):
        for y in range(0, height, multiplier):
            w = x + multiplier
            h = y + multiplier
            if x == width - multiplier and y == height - multiplier:
                image_with_grid_draw.rectangle(((x, y), (w - 1, h - 1)), outline="black")
            elif x == width - multiplier:
                image_with_grid_draw.rectangle(((x, y), (w - 1, h)), outline="black")
            elif y == height - multiplier:
                image_with_grid_draw.rectangle(((x, y), (w, h - 1)), outline="black")
            else:
                image_with_grid_draw.rectangle(((x, y), (w, h)), outline="black")

    return image_with_grid


def create_image_with_numbers_and_grid(image: Image, palette: list[tuple[int, int, int]], width: int, height: int,
                                       multiplier: int,
                                       numbers_size: int) -> Image:
    image_with_numbers_and_grid = image.copy()
    image_with_numbers_and_grid_draw = ImageDraw.Draw(image_with_numbers_and_grid)
    for x in range(0, width, multiplier):
        for y in range(0, height, multiplier):
            w = x + multiplier
            h = y + multiplier
            if x == width - multiplier and y == height - multiplier:
                image_with_numbers_and_grid_draw.rectangle(((x, y), (w - 1, h - 1)), outline="black")
            elif x == width - multiplier:
                image_with_numbers_and_grid_draw.rectangle(((x, y), (w - 1, h)), outline="black")
            elif y == height - multiplier:
                image_with_numbers_and_grid_draw.rectangle(((x, y), (w, h - 1)), outline="black")
            else:
                image_with_numbers_and_grid_draw.rectangle(((x, y), (w, h)), outline="black")

            color = image.getpixel((x, y))
            image_with_numbers_and_grid_draw.text((x + multiplier * 0.5, y + multiplier * 0.5),
                                                  str(palette.index(color) + 1),
                                                  fill="black" if is_light_color(color) else "white",
                                                  anchor="mm", font=ImageFont.truetype("arial.ttf", numbers_size))

    return image_with_numbers_and_grid


def create_image_with_numbers_and_grid_without_color(image: Image, palette: list[tuple[int, int, int]], width: int,
                                                     height: int, multiplier: int,
                                                     numbers_size: int) -> Image:
    image_with_numbers_and_grid_without_color = Image.new("RGB", (image.width, image.height), "white")
    image_with_numbers_and_grid_without_color_draq = ImageDraw.Draw(image_with_numbers_and_grid_without_color)
    for x in range(0, width, multiplier):
        for y in range(0, height, multiplier):
            w = x + multiplier
            h = y + multiplier
            if x == width - multiplier and y == height - multiplier:
                image_with_numbers_and_grid_without_color_draq.rectangle(((x, y), (w - 1, h - 1)), outline="black")
            elif x == width - multiplier:
                image_with_numbers_and_grid_without_color_draq.rectangle(((x, y), (w - 1, h)), outline="black")
            elif y == height - multiplier:
                image_with_numbers_and_grid_without_color_draq.rectangle(((x, y), (w, h - 1)), outline="black")
            else:
                image_with_numbers_and_grid_without_color_draq.rectangle(((x, y), (w, h)), outline="black")

            image_with_numbers_and_grid_without_color_draq.text((x + multiplier * 0.5, y + multiplier * 0.5),
                                                                str(palette.index(image.getpixel((x, y))) + 1),
                                                                fill="black", anchor="mm",
                                                                font=ImageFont.truetype("arial.ttf", numbers_size))

    return image_with_numbers_and_grid_without_color


def create_image_with_palette(image: Image, palette: tuple[int], width: int, height: int, multiplier: int) -> Image:
    if len(palette) % 3 != 0:
        raise ValueError("palette % 3 must be zero")
    palette_image = Image.new("P", (1, 1))
    if len(palette) < 255:
        palette = palette + (0, 0, 0) * (255 - len(palette))
    palette_image.putpalette(palette)
    return image.quantize(palette=palette_image).resize((width, height)).resize(
        (width * multiplier, height * multiplier), resample=BOX).convert("RGB")


def quantize_image_pyxelate(image: Image, colors: int) -> Image:
    return Image.fromarray(Pyx(palette=colors).fit_transform(np.array(image)))


def quantize_and_resize_image_pyxelate(image: Image, colors: int, width: int, height: int) -> Image:
    return Image.fromarray(Pyx(palette=colors, width=width, height=height).fit_transform(np.array(image)))


def quantize_and_reresize_image_pyxelate(image: Image, colors: int, width: int, height: int, multiplier: int) -> Image:
    return Image.fromarray(Pyx(palette=colors, width=width, height=height).fit_transform(np.array(image))).resize(
        (width * multiplier, height * multiplier), resample=BOX).convert("RGB")


def create_image_with_palette_pyxelate(image: Image, palette: tuple[int]) -> Image:
    return Image.fromarray(Pyx(palette=Pal.from_rgb(palette)).fit_transform(np.array(image)))


def create_and_resize_image_with_palette_pyxelate(image: Image, palette: tuple[int], width: int, height: int) -> Image:
    return Image.fromarray(
        Pyx(palette=Pal.from_rgb(palette), width=width, height=height).fit_transform(np.array(image)))


def create_and_reresize_image_with_palette_pyxelate(image: Image, palette: tuple[int], width: int, height: int,
                                                    multiplier: int) -> Image:
    return Image.fromarray(
        Pyx(palette=Pal.from_rgb(palette), width=width, height=height).fit_transform(np.array(image))).resize(
        (width * multiplier, height * multiplier), resample=BOX).convert("RGB")


# -------------- combined functions --------------
def create_mosaic_from_image_1(image: Image, colors: int, width: int, height: int, multiplier: int) -> Image:
    return reresize_image(quantize_image(resize_image(image, width, height), colors), width, height, multiplier)


def create_mosaic_from_image_2(image: Image, colors: int, width: int, height: int, multiplier: int) -> Image:
    return reresize_image(resize_image(quantize_image(image, colors), width, height), width, height, multiplier)


def create_mosaic_from_image_3(image: Image, colors: int, width: int, height: int, multiplier: int) -> Image:
    return quantize_and_reresize_image_pyxelate(image, colors, width, height, multiplier)


def create_mosaic_from_image_with_palette_1(image: Image, palette: tuple[tuple[int, int, int]], width: int,
                                            height: int, multiplier: int) -> Image:
    return create_image_with_palette(image, flat_colors_list_from_colors_palette(palette), width, height, multiplier)


def create_mosaic_from_image_with_palette_2(image: Image, palette: tuple[int], width: int,
                                            height: int, multiplier: int) -> Image:
    return create_and_reresize_image_with_palette_pyxelate(image, palette, width, height, multiplier)


def get_colors_distribution(image: Image, multiplier: int) -> dict[tuple[int, int, int], int]:
    distribution = {}
    for x in range(0, image.width, multiplier):
        for y in range(0, image.height, multiplier):
            color = image.getpixel((x, y))
            if color in distribution:
                distribution[color] += 1
            else:
                distribution[color] = 1
    return distribution


def add_grid_to_mosaic(mosaic: Image, _: dict[tuple[int, int, int], int], multiplier: int, **kwargs: dict) -> Image:
    return create_image_with_grid(mosaic, mosaic.width, mosaic.height, multiplier)


def add_numbers_to_mosaic(mosaic: Image, colors_distribution: dict[tuple[int, int, int], int],
                          multiplier: int, **kwargs: dict) -> Image:
    numbers_size = kwargs["numbers_size"]
    if numbers_size is None:
        numbers_size = 12
    return create_image_with_numbers(mosaic, list(colors_distribution.keys()), mosaic.width, mosaic.height, multiplier,
                                     numbers_size)


def add_grid_and_numbers_to_mosaic(mosaic: Image, colors_distribution: dict[tuple[int, int, int], int],
                                   multiplier: int, **kwargs) -> Image:
    numbers_size = kwargs["numbers_size"]
    if numbers_size is None:
        numbers_size = 12
    return create_image_with_numbers_and_grid(mosaic, list(colors_distribution.keys()), mosaic.width, mosaic.height,
                                              multiplier, numbers_size)


def add_raw_grid_and_numbers_to_mosaic(mosaic: Image, colors_distribution: dict[tuple[int, int, int], int],
                                       multiplier: int, **kwargs) -> Image:
    numbers_size = kwargs["numbers_size"]
    if numbers_size is None:
        numbers_size = 12
    return create_image_with_numbers_and_grid_without_color(mosaic, list(colors_distribution.keys()), mosaic.width,
                                                            mosaic.height, multiplier, numbers_size)


if __name__ == "__main__":
    pass

    # images_folder = "images"
    # image_name = "image_1"
    # image_extension = "jpg"
    # full_image_name = image_name + "." + image_extension
    #
    # image = open_image(full_image_name, folder=images_folder)
    #
    # if image.width != image.height:
    #     raise ValueError("width != height")
    #
    # colors = 6
    # width = 25
    # height = 25
    # multiplier = 20
    #
    # palette = ((255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 165, 0), (255, 255, 0), (0, 0, 0))
    #
    # image_1 = create_mosaic_from_image_1(image, colors, width, height, multiplier)
    # save_image(image_1, image_name, "1")
    # image_2 = create_mosaic_from_image_2(image, colors, width, height, multiplier)
    # save_image(image_2, image_name, "2")
    # image_3 = create_mosaic_from_image_3(image, colors, width, height, multiplier)
    # save_image(image_3, image_name, "3")
    # image_4 = create_mosaic_from_image_with_palette_1(image, palette, width, height, multiplier)
    # save_image(image_4, image_name, "4")
    # image_5 = create_mosaic_from_image_with_palette_2(image, palette, width, height, multiplier)
    # save_image(image_5, image_name, "5")
    #
    # images = [image_1, image_2, image_3, image_4, image_5]
    #
    # for i, im in enumerate(images):
    #     colors_distribution = get_colors_distribution(im, multiplier)
    #     save_image(add_grid_to_mosaic(im, colors_distribution, multiplier), image_name, str(i + 1) + "g")
    #     save_image(add_numbers_to_mosaic(im, colors_distribution, multiplier), image_name, str(i + 1) + "n")
    #     save_image(add_grid_and_numbers_to_mosaic(im, colors_distribution, multiplier), image_name, str(i + 1) + "gn")
    #     save_image(add_raw_grid_and_numbers_to_mosaic(im, colors_distribution, multiplier), image_name,
    #                str(i + 1) + "rgn")
    #     save_colors_distribution_for_image(image_name + "_" + str(i + 1), colors_distribution)
