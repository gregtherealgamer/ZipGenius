import unittest
from decompressor import decompress_zip, decompress_gzip
import os

class TestDecompressMethods(unittest.TestCase):
    def test_zip_decompression(self):
        input_file = "tests/test_output.zip"
        output_dir = "tests/test_output"
        decompress_zip(input_file, output_dir)
        self.assertTrue(os.path.exists(output_dir))

    def test_gzip_decompression(self):
        input_file = "tests/test_output.gz"
        output_file = "tests/test_output.txt"
        decompress_gzip(input_file, output_file)
        self.assertTrue(os.path.exists(output_file))

if __name__ == '__main__':
    unittest.main()
