#!/usr/bin/env python3

import os
import argparse
import subprocess



class EpubEbook:
	def __init__(self, root, filename):
		self.root = root
		self.filename = filename
		self.epub_path = os.path.join(root, filename)
		self.azw3_path = os.path.join(root, os.path.splitext(filename)[0] + ".azw3")

	def azw3_exists(self):
		if os.path.exists(self.azw3_path) and os.path.getmtime(self.azw3_path) > os.path.getmtime(self.epub_path):
			return True
		return False

	def convert_epub_to_azw3(self, force=False):
		if not force and self.azw3_exists():
			# Skip conversion if AZW3 exists and is newer than EPUB
			print(f"Skipping {self.filename}, AZW3 is up-to-date."); return

		print(f"Converting {self.filename} to AZW3...")
		subprocess.run(["ebook-convert", self.epub_path, self.azw3_path], check=True)
		print(f"Conversion completed: {self.azw3_path}")


def convert_epub_to_azw3(directory):
	"""Convert all EPUB files in the directory to AZW3 using Calibre's ebook-convert."""
	for root, _, files in os.walk(directory):
		for filename in files:
			if filename.lower().endswith(".epub"):
				epub = EpubEbook(root, filename)
				epub.convert_epub_to_azw3()


def main():
	parser = argparse.ArgumentParser(description="Convert all EPUB files in a directory to AZW3 using Calibre's ebook-convert.")
	parser.add_argument("directory", metavar="DIR", type=str, help="Path to the directory containing EPUB files")
	args = parser.parse_args()

	convert_epub_to_azw3(args.directory)


if __name__ == "__main__":
	main()
