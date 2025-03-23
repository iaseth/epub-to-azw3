#!/usr/bin/env python3

import os
import sys
import argparse
import subprocess



def get_size(path):
	if not os.path.isfile(path):
		return "NULL"

	size = os.path.getsize(path)  # Get file size in bytes

	for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
		if size < 1024:
			return f"{size:.2f} {unit}"
		size /= 1024

	return f"{size:.2f} PB"  # Handle extremely large files


def _colorize(color_code, *args, sep=' '):
	text = sep.join(map(str, args))
	return f"\033[{color_code}m{text}\033[0m"

def red(*args, sep=' '):
	return _colorize(31, *args, sep=sep)

def green(*args, sep=' '):
	return _colorize(32, *args, sep=sep)

def yellow(*args, sep=' '):
	return _colorize(33, *args, sep=sep)

def blue(*args, sep=' '):
	return _colorize(34, *args, sep=sep)


class EpubEbook:
	def __init__(self, root, filename, app):
		self.root = root
		self.filename = filename
		self.idx = app.count
		self.app = app
		self.epub_path = os.path.join(root, filename)
		self.azw3_path = os.path.join(root, os.path.splitext(filename)[0] + ".azw3")

	def azw3_exists(self):
		if os.path.exists(self.azw3_path) and os.path.getmtime(self.azw3_path) > os.path.getmtime(self.epub_path):
			return True
		return False

	def convert_epub_to_azw3(self, force=False):
		print(f"({self.idx+1} / {self.app.count}) {blue(self.epub_path)} ({yellow(get_size(self.epub_path))})")
		if not force and self.azw3_exists():
			# Skip conversion if AZW3 exists and is newer than EPUB
			print(f"\tSkipping {green(self.azw3_path)} ({yellow(get_size(self.azw3_path))}), AZW3 is up-to-date."); return

		print(f"\tConverting {yellow(self.filename)} to AZW3...")
		subprocess.run(["ebook-convert", self.epub_path, self.azw3_path], check=True)
		print(f"\tConversion completed: {green(self.azw3_path)} ({yellow(get_size(self.azw3_path))})")


class ConvertApp:
	def __init__(self, directory):
		self.directory = directory
		self.setup_epubs()

	@property
	def count(self):
		return len(self.epubs)

	def setup_epubs(self):
		self.epubs = []
		for root, _, files in os.walk(self.directory):
			for filename in files:
				if filename.lower().endswith(".epub"):
					epub = EpubEbook(root, filename, self)
					self.epubs.append(epub)

	def convert_epub_to_azw3(self):
		for epub in self.epubs:
			epub.convert_epub_to_azw3()


def main():
	parser = argparse.ArgumentParser(description="Convert all EPUB files in a directory to AZW3 using Calibre's ebook-convert.")
	parser.add_argument("directory", metavar="DIR", type=str, help="Path to the directory containing EPUB files")
	args = parser.parse_args()

	app = ConvertApp(args.directory)
	app.convert_epub_to_azw3()


if __name__ == "__main__":
	main()
