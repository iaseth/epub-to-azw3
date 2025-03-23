# epub-to-azw3

A simple Python script to convert all `.epub` files in a directory to `.azw3` format using Calibre's `ebook-convert` command.

## Features
- Converts `.epub` files to `.azw3` using Calibre.
- Skips conversion if the `.azw3` file already exists and is newer than the `.epub`.
- Takes the directory path as a command-line argument.

## Requirements
- **Calibre** must be installed and `ebook-convert` should be accessible from the command line.
- Python 3.x

## Installation
Clone the repository:
```sh
git clone https://github.com/iaseth/epub-to-azw3.git
cd epub-to-azw3
```

## Usage
Run the script with:
```sh
python epub-to-azw3.py /path/to/directory
```

### Example:
```sh
python epub-to-azw3.py ~/ebooks
```

On Unix-based systems, you can make the script executable:
```sh
chmod +x epub-to-azw3.py
./epub-to-azw3.py /path/to/directory
```

## Author
**Ankur Seth** ([GitHub: @iaseth](https://github.com/iaseth))

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

