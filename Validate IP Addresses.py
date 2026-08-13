import re

def validate_ip(ip):
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    ipv6_pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    return bool(re.match(ipv4_pattern, ip) or re.match(ipv6_pattern, ip))

print(validate_ip("192.168.1.1"))  
print(validate_ip("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  
print(validate_ip("999.999.999.999"))  
