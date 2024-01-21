from compressor import compress_zip, compress_gzip
from decompressor import decompress_zip, decompress_gzip

# Example usage:
input_file = "examples/example1.txt"
output_zip = "examples/output.zip"
output_gzip = "examples/output.gz"
output_dir = "examples/output_dir"
output_txt = "examples/output.txt"

# Compress using ZIP
compress_zip(input_file, output_zip)

# Decompress using ZIP
decompress_zip(output_zip, output_dir)

# Compress using GZIP
compress_gzip(input_file, output_gzip)

# Decompress using GZIP
decompress_gzip(output_gzip, output_txt)

print("Compression and decompression completed successfully.")
