import unittest

from compress_image import get_compressed_file_name

class CompressionTest(unittest.TestCase):

    def test_get_compressed_file_name(self):
        self.assertEqual(get_compressed_file_name("abc"),
            "abccompressed.jpg",
            'add abccompressed.jpgcompress string to the name')

    def test_get_compressed_file_name_dont(self):
        self.assertEqual(get_compressed_file_name("abccompressed.jpg"),
            "abccompressed.jpg",
            'file name is already compressed')


if __name__ == '__main__':
    unittest.main()
