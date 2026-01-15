import socket

# Ask the user for the target
target = input("Enter website to scan: ")

print(f"\nScanning target: {target}\n")

# Common ports to scan
ports = [21, 22, 80, 443]

for port in ports:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is closed")

        s.close()

    except socket.error as e:
        print(f"Error scanning port {port}: {e}")

print("\nScan complete.")
