import unittest

from compress_image import get_compressed_file_name
from compress_image import img_file

class CompressionTest(unittest.TestCase):

    def test_get_compressed_file_name(self):
        self.assertEqual(get_compressed_file_name("abc"),
            "abccompressed.jpg",
            'add abccompressed.jpgcompress string to the name')

    def test_get_compressed_file_name_dont(self):
        self.assertEqual(get_compressed_file_name("abccompressed.jpg"),
            "abccompressed.jpg",
            'file name is already compressed')

    def test_img_file_invalidFile(self):
        self.assertEqual(img_file("abc"),
            (None, 0),
            'non existent file')


if __name__ == '__main__':
    unittest.main()
