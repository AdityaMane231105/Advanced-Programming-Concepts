server_ip = ("192.168.1.1",)  
allowed_ips = ["10.0.0.1", "10.0.0.2"]

def update_allowed(ip):
    allowed_ips.append(ip)

def show_config():
    print("Server IP:", server_ip)
    print("Allowed IPs:", allowed_ips)

update_allowed("10.0.0.3")
show_config()
