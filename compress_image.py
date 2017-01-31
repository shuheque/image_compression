from PIL import Image
import os


def img_file(image_location):
    try:
        image = Image.open(image_location)
        size_in_bytes = os.stat(image_location).st_size
        return (image, size_in_bytes)
    except FileNotFoundError:
        return (None, 0)


def get_compressed_file_name(file_location):
    if "compressed" in file_location:
        return file_location
    else:
        compressed_file_name = "%s%s" % (file_location.replace(".jpg", ""),
                                         "compressed.jpg")
        return compressed_file_name


def compress(max_size, file_location):
    compressed_img_file_loc = get_compressed_file_name(file_location)
    image, size = img_file(file_location)
    image.save(compressed_img_file_loc,optimize=True,quality=85)
    if size > max_size:
        compress(max_size, compressed_img_file_loc)


def main():
    compress(200000, "blog_fast-01.jpg")


if __name__ == '__main__':
    main()
