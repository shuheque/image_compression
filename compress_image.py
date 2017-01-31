from PIL import Image
import os


import time

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
        compressed_file_name = "%s%s" % (file_location.replace(".jpg", ""), "compressed.jpg")
        return compressed_file_name


def compress(file_location):
    compressed_img_file_loc = "compressed_img.jpg"
    image, size = img_file(file_location)
    image.save(compressed_img_file_loc,optimize=True,quality=85)
    if size > 200000:
        compress(compressed_img_file_loc)


def main():
    compress("blog_fast-01.jpg")

if __name__ == '__main__':
    main()


# image_location = "blog_fast-01.jpg"
# image = Image.open(image_location)
# quality = get_compression_quality_factor(image_location)
# print(image.size)
# # I downsize the image with an ANTIALIAS filter (gives the highest quality)
# # foo = foo.resize((160,300),Image.ANTIALIAS
# image.save("image_scaled.jpg",quality=95)
# # The saved downsized image size is 24.8kb
# image.save("image_scaled_opt.jpg",optimize=True,quality=quality)
# The saved downsized image size is 22.9kb
