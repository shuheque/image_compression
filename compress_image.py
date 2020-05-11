from PIL import Image
import os
import os.path as opth
import sys


def img_file(image_location):
    try:
        image = Image.open(image_location)
        size_in_bytes = os.stat(image_location).st_size
        return (image, size_in_bytes)
    except FileNotFoundError:
        return (None, 0)


def get_compressed_file_name(file_location):
    file_location = file_location.lower()
    if "compressed" in file_location:
        return file_location
    else:
        strip_extension = file_location.replace(".jpg", "")
        strip_extension = strip_extension.replace(".png", "")
        strip_extension = strip_extension.replace(".jpeg", "")
        compressed_file_name = "%s%s" % (strip_extension.replace(".jpg", ""),
                                         "compressed.jpg")
        return compressed_file_name


def compress(max_size, file_location):
    file_location = file_location.lower()
    compressed_img_file_loc = get_compressed_file_name(file_location)
    image, size = img_file(file_location)
    image.save(compressed_img_file_loc,optimize=True,quality=90)
    if size > max_size:
        compress(max_size, compressed_img_file_loc)


def main1():
    max_size = int(sys.argv[1])
    files = sys.argv[2:]
    for file_loc in files:
        print("%s will be compressed to %s" % (file_loc,
            get_compressed_file_name(file_loc)))
        compress(max_size, file_loc)
    print("All file compressed.")

def main():
    try:
        max_size = int(sys.argv[1])
    except:
        max_size = 538000
    for file_loc in os.listdir(os.getcwd()):
        if opth.isfile(file_loc):
            print("%s will be compressed to %s" % (file_loc,
                get_compressed_file_name(file_loc)))
            compress(max_size, file_loc)
    print("All file compressed.")
    

if __name__ == '__main__':
    main()
