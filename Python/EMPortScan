import socket
import re


def get_top_100_ports():
    """Retrieve the top 100 most commonly used ports from nmap-services file."""
    top_100_ports = []
    try:
        with open('/etc/services', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if not line.startswith('#') and not line.strip() == '':
                    port = line.split()[1].split('/')[0]
                    if port.isdigit():
                        top_100_ports.append(int(port))
                if len(top_100_ports) == 100:
                    break
    except FileNotFoundError:
        print("[ERROR] nmap-services file not found. Using default top 100 ports.")
        top_100_ports = list(range(1, 101))
    return top_100_ports


def get_top_1000_ports():
    """Retrieve the top 1000 most commonly used ports from nmap-services file."""
    top_1000_ports = []
    try:
        with open('/etc/services', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if not line.startswith('#') and not line.strip() == '':
                    port = line.split()[1].split('/')[0]
                    if port.isdigit():
                        top_1000_ports.append(int(port))
                if len(top_1000_ports) == 1000:
                    break
    except FileNotFoundError:
        print("[ERROR] nmap-services file not found. Using default top 1000 ports.")
        top_1000_ports = list(range(1, 1001))
    return top_1000_ports


def get_top_10000_ports():
    """Retrieve the top 10000 most commonly used ports from nmap-services file."""
    top_10000_ports = []
    try:
        with open('/etc/services', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if not line.startswith('#') and not line.strip() == '':
                    port = line.split()[1].split('/')[0]
                    if port.isdigit():
                        top_10000_ports.append(int(port))
                if len(top_10000_ports) == 10000:
                    break
    except FileNotFoundError:
        print("[ERROR] nmap-services file not found. Using default top 10000 ports.")
        top_10000_ports = list(range(1, 10001))
    return top_10000_ports


def prompt_scan_type():
    """Prompt user for scan type."""
    while True:
        scan_type = input("Enter scan type (quick/normal/thorough/full): ").lower()
        if scan_type in ['quick', 'normal', 'thorough', 'full']:
            return scan_type
        else:
            print("[ERROR] Invalid scan type. Please try again.")


def get_ports_by_scan_type(scan_type):
    """Get target ports based on scan type."""
    if scan_type == 'quick':
        return get_top_100_ports()
    elif scan_type == 'normal':
        return get_top_1000_ports()
    elif scan_type == 'thorough':
        return get_top_10000_ports()
    elif scan_type == 'full':
        return list(range(1, 65536))
    else:
        print("[ERROR] Invalid scan type. Using default top 100 ports.")
        return get_top_100_ports()


# Prompt user for scan type
scan_type = prompt_scan_type()

# Get target ports based on scan type
target_ports = get_ports_by_scan_type(scan_type)


def is_valid_ip(ip):
    # Use regex to heck if the given string is a valid IP address
    pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"
    return re.match(pattern, ip)


def is_valid_url(url):
    # Use regex to check if the given string is a valid URL
    pattern = r"^(http(s)?://)?([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)?$"
    return re.match(pattern, url)


def port_scan_banner(host, start_port, end_port):
    try:
        # Detect input type (IP or URL) and resolve host accordingly
        if is_valid_ip(host):
            ip = host
            specify_port_range = input("Would you like to specify a port range? (yes/no): ").lower()
            if specify_port_range == "yes":
                start_port = int(input("Enter start port: "))
                end_port = int(input("Enter end port: "))
                if start_port > end_port:
                    raise ValueError("Invalid port range. Start port cannot be greater than end port.")
            else:
                print("Scanning all ports...")
                start_port = 1
                end_port = 65535
            print(f"Scanning ports {start_port} to {end_port} for {ip}:")
        elif is_valid_url(host):
            ip = socket.gethostbyname(host)
            print(f"Resolved {host} to IP: {ip}")
            specify_port_range = input("Would you like to specify a port range? (yes/no): ").lower()
            if specify_port_range == "yes":
                start_port = int(input("Enter start port: "))
                end_port = int(input("Enter end port: "))
                if start_port > end_port:
                    raise ValueError("Invalid port range. Start port cannot be greater than end port.")
            else:
                print("Scanning all ports...")
                start_port = 1
                end_port = 65535
        else:
            raise ValueError("Invalid input. Please enter a valid IP address or URL.")

        # Loop through the port range and perform port scanning
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port}: OPEN")
                # Perform banner grabbing here
                banner = sock.recv(1024)
                if banner:
                    print(f"Banner for Port {port}: {banner.decode().strip()}")
                    # Check if banner contains service version information
                    if 'Server:' in banner:
                        print("Service version from port {}: {}".format(port, banner.split('Server:', 1)[1].strip()))
                    # Check if banner contains protocol information
                    if 'Protocol:' in banner:
                        print("Protocol from port {}: {}".format(port, banner.split('Protocol:', 1)[1].strip()))
                    # Check if banner contains service status or operational information
                    if 'Status:' in banner:
                        print("Status from port {}: {}".format(port, banner.split('Status:', 1)[1].strip()))
                    # Check if banner contains error messages or debugging information
                    if 'Error:' in banner:
                        print("Error from port {}: {}".format(port, banner.split('Error:', 1)[1].strip()))
                # Close the socket
            sock.close()
        else:
            print(f"Port {port}: CLOSED")

    except socket.gaierror as e:
        print(f"Failed to resolve {host} to an IP address: {e}")
    except ConnectionRefusedError as e:
        print(f"Connection refused for {host}:{port}: {e}")
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

