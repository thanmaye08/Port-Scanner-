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
##### options
- target: The IP address or hostname of the target you want to scan (required).
- -p, --ports: The port range you want to scan, in the format start-end (default is 1-1000).
- -t, --threads: The number of threads to use for scanning (default is 100).
- -o, --output: The file to which the scan results should be saved (optional).


## Disclaimer 
This tool is intended for educational purposes only. The author is not responsible for any misuse or damage caused by this tool. Users should ensure they have explicit permission to scan any network or system before using this tool. Unauthorized scanning of networks or systems is illegal and unethical.

## Ethical Usage
Please adhere to the following ethical guidelines when using this port scanner:
- Obtain Permission: Always obtain explicit permission from the owner of the network or system before scanning.
- Respect Privacy: Do not scan networks or systems without proper authorization.
- Legal Compliance: Ensure that your actions comply with all applicable laws and regulations.
- Report Responsibly: If you discover vulnerabilities, report them responsibly to the system owner.


