#!/usr/bin/env python3

import os
import argparse
import subprocess



def convert_epub_to_azw3(directory):
	"""Convert all EPUB files in the directory to AZW3 using Calibre's ebook-convert."""
	for filename in os.listdir(directory):
		if filename.lower().endswith(".epub"):
			epub_path = os.path.join(directory, filename)
			azw3_path = os.path.join(directory, os.path.splitext(filename)[0] + ".azw3")

			# Skip conversion if AZW3 exists and is newer than EPUB
			if os.path.exists(azw3_path) and os.path.getmtime(azw3_path) > os.path.getmtime(epub_path):
				print(f"Skipping {filename}, AZW3 is up-to-date.")
				continue

			print(f"Converting {filename} to AZW3...")
			subprocess.run(["ebook-convert", epub_path, azw3_path], check=True)
			print(f"Conversion completed: {azw3_path}")


def main():
	parser = argparse.ArgumentParser(description="Convert all EPUB files in a directory to AZW3 using Calibre's ebook-convert.")
	parser.add_argument("directory", metavar="DIR", type=str, help="Path to the directory containing EPUB files")
	args = parser.parse_args()

	convert_epub_to_azw3(args.directory)


if __name__ == "__main__":
	main()
