# Port Scanner

A simple and efficient port scanner built in Python, using multithreading for fast scanning. This tool is intended for educational purposes and should only be used on systems you have explicit permission to scan.

## Features
- Multithreading for fast scanning
- Customizable port ranges
- Logs results to a file
- Resolves service names for open ports

## Original Project
This project is based on a guided project from the Udemy course "Python Coding Projects Build a Port Scanner" by MMZ Academy. The original code provided the foundation for this enhanced version.

## Improvements Made
- Added multithreading for faster scanning
- Improved command-line argument handling with `argparse`
- Allowed custom port ranges
- Included logging of results to a file
- Added service name resolution for open ports
- Improved error handling and user feedback

## Usage

### Prerequisites
- Python 3.x
- Required Python packages: `pyfiglet`, `argparse`

### Running the Scanner
To run the scanner, use the following command:
python port_scanner.py target [options]
