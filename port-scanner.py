import pyfiglet
import sys
import socket
from datetime import datetime
import argparse
from concurrent.futures import ThreadPoolExecutor

def print_banner():
    # Added banner using pyfiglet for better visual presentation
    ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
    print(ascii_banner)

def get_arguments():
    # Improved command-line argument handling using argparse
    parser = argparse.ArgumentParser(description="A simple port scanner")
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("-p", "--ports", help="Port range, e.g., 1-65535", default="1-1000")
    parser.add_argument("-t", "--threads", help="Number of threads", type=int, default=100)
    parser.add_argument("-o", "--output", help="Output file", default=None)
    return parser.parse_args()

def scan_port(target, port):
    try:
        # Implemented port scanning logic
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            try:
                # Added service name resolution for open ports
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            print(f"Port {port} is open ({service})")
            return port, service
        s.close()
    except Exception as e:
        return None

def scan_ports(target, start_port, end_port, num_threads, output_file):
    print("-" * 50)
    print(f"Scanning Target: {target}")
    print("Scanning started at: " + str(datetime.now()))
    print("-" * 50)
    
    open_ports = []

    # Added multithreading to speed up the scanning process
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(scan_port, target, port) for port in range(start_port, end_port + 1)]
        for future in futures:
            result = future.result()
            if result:
                open_ports.append(result)

    if output_file:
        # Added functionality to log results to a file
        with open(output_file, "w") as f:
            for port, service in open_ports:
                f.write(f"Port {port} is open ({service})\n")
        print(f"Results saved to {output_file}")

    print("-" * 50)
    print("Scanning finished at: " + str(datetime.now()))
    print("-" * 50)

if __name__ == "__main__":
    print_banner()
    # Enhanced argument handling
    args = get_arguments()
    target = socket.gethostbyname(args.target)
    # Allowed specification of custom port ranges
    start_port, end_port = map(int, args.ports.split('-'))
    # Added multithreading and output file handling
    scan_ports(target, start_port, end_port, args.threads, args.output)
