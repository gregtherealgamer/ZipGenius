import zipfile
import gzip

def decompress_zip(input_file, output_file):
    with zipfile.ZipFile(input_file, 'r') as zipf:
        zipf.extractall(output_file)

def decompress_gzip(input_file, output_file):
    with gzip.open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        f_out.writelines(f_in)