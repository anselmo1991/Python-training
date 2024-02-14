# with re
import re

def validate_ip_address(ip_address):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"

    if re.match(pattern, ip_address):
        parts = ip_address.split(".")

        if all(0 <= int(part) <= 255 for part in parts):
            return True

    return False

print(validate_ip_address("176.132.0.1"))
print(validate_ip_address("45.4.0.256"))
print(validate_ip_address(""))
print(validate_ip_address("192.168.0.1"))
print(validate_ip_address("0.0.0.1"))
print(validate_ip_address("10.100.500.32"))
print(validate_ip_address("700"))
print(validate_ip_address("127.0.1"))

# with socket.inet_aton
import socket

def validate_ip_address(ip_address):
    try:
        socket.inet_aton(ip_address)
        return True
    except socket.error:
        return False

print(validate_ip_address("176.132.0.1"))
print(validate_ip_address("45.4.0.256"))
print(validate_ip_address(""))
print(validate_ip_address("192.168.0.1"))
print(validate_ip_address("0.0.0.1"))
print(validate_ip_address("10.100.500.32"))
print(validate_ip_address("700"))
print(validate_ip_address("127.0.1"))
