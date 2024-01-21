import argparse
import zipfile
import gzip
from tqdm import tqdm  # Import tqdm for the progress bar

# Define a function for tracking progress
def track_progress(iterable, desc, total):
    return tqdm(iterable, desc=desc, total=total, unit='B', unit_scale=True)

def compress_zip(input_file, output_file):
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        with open(input_file, 'rb') as f_in:
            file_size = len(f_in.read())
            f_in.seek(0)
            with track_progress(iterable=f_in, desc='Compressing', total=file_size) as progress_bar:
                zipf.write(input_file, arcname=input_file)

def decompress_zip(input_file, output_file):
    with zipfile.ZipFile(input_file, 'r') as zipf:
        file_size = sum([file.file_size for file in zipf.filelist])
        with track_progress(iterable=zipf.filelist, desc='Decompressing', total=file_size) as progress_bar:
            zipf.extractall(output_file)

def compress_gzip(input_file, output_file):
    with open(input_file, 'rb') as f_in, gzip.open(output_file, 'wb') as f_out:
        file_size = len(f_in.read())
        f_in.seek(0)
        with track_progress(iterable=f_in, desc='Compressing', total=file_size) as progress_bar:
            f_out.writelines(f_in)

def decompress_gzip(input_file, output_file):
    with gzip.open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        file_size = len(f_in.read())
        f_in.seek(0)
        with track_progress(iterable=f_in, desc='Decompressing', total=file_size) as progress_bar:
            f_out.writelines(f_in)

def main():
    parser = argparse.ArgumentParser(description="File Compression Tool")
    parser.add_argument("input_file", help="Input file to compress/decompress")
    parser.add_argument("output_file", help="Output file after compression/decompression")
    parser.add_argument("--algorithm", choices=["zip", "gzip"], default="zip", help="Compression algorithm (default: zip)")
    parser.add_argument("--decompress", action="store_true", help="Decompress the input file")

    args = parser.parse_args()

    if args.decompress:
        if args.algorithm == "zip":
            decompress_zip(args.input_file, args.output_file)
        elif args.algorithm == "gzip":
            decompress_gzip(args.input_file, args.output_file)
    else:
        if args.algorithm == "zip":
            compress_zip(args.input_file, args.output_file)
        elif args.algorithm == "gzip":
            compress_gzip(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
