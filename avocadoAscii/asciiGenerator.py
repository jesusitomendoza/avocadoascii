from PIL import Image, ImageDraw, ImageFont
import math

aschar = ["@", "#", "&", "!", "*", "?", ";", ":", ",", "."]


def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * .55)
    return image.resize((new_width, new_height))


def convert_to_grayscale(image):
    return image.convert("L")


def map_pixels_to_ascii(image, aschar):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += aschar[pixel // 25]
    return ascii_str


def image_to_ascii(image_path, new_width=75):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path} Error: {e}")
        return


    image = resize_image(image, new_width)
    image = convert_to_grayscale(image)

    ascii_str = map_pixels_to_ascii(image, aschar)

    ascii_lines = []

    for i in range(0, len(ascii_str), new_width):
        line = ascii_str[i:i + new_width]
        ascii_lines.append(line)

    ascii_image = "\n".join(ascii_lines)
    return ascii_image


def save_ascii_image(ascii_image, output_file):
    with open(output_file) as f:
        f.write(ascii_image)


def main(image_path, output_file="ascii_image.txt", width=100):
    ascii_image = image_to_ascii(image_path, width)
    if ascii_image:
        save_ascii_image(ascii_image, output_file)
        print(f"ASCII art saved to {output_file}")


if __name__ == "__main__":
    image_path = 'spidermanEmblem.png'
    ascii_image = image_to_ascii(image_path)
    if ascii_image:
        print (ascii_image)


