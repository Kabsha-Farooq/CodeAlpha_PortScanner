import socket

# Target can be an IP (e.g., '192.168.1.1') or domain (e.g., 'google.com')
target = input("Enter target IP or domain: ")

# Define port range
start_port = 1
end_port = 100  # You can increase up to 65535

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

for port in range(start_port, end_port + 1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()
    except KeyboardInterrupt:
        print("\nScan cancelled by user.")
        break
    except socket.gaierror:
        print("Hostname could not be resolved.")
        break
    except socket.error:
        print("Couldn't connect to server.")
        break
