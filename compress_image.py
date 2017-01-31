from PIL import Image
import os


def get_file_size(image_location):
    try:
        return os.stat(image_location).st_size
    except FileNotFoundError:
        return 0


def compress(image):
    if
    if get_file_size("/tmp/tmp_img.jpg") > 200000:
        image = Image.open("/tmp/tmp_img.jpg")
        image.save("/tmp/tmp_img.jpg",optimize=True,quality=95)
        compress("/tmp/tmp_img.jpg")
    else:
        image = Image.open("/tmp/tmp_img.jpg")
        image.save("/tmp/tmp_img.jpg",optimize=True,quality=95)


def make(arg):
    pass


image_location = "blog_fast-01.jpg"
image = Image.open(image_location)
quality = get_compression_quality_factor(image_location)
print(image.size)
# I downsize the image with an ANTIALIAS filter (gives the highest quality)
# foo = foo.resize((160,300),Image.ANTIALIAS
image.save("image_scaled.jpg",quality=95)
# The saved downsized image size is 24.8kb
image.save("image_scaled_opt.jpg",optimize=True,quality=quality)
# The saved downsized image size is 22.9kb
