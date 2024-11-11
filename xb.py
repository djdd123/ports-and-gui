import socket
import time
import sys
import os

# פונקציה לבדוק אם פורט פתוח
def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Wait max 1 second
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

# פונקציה להדפיס טקסט צבעוני
def print_colored(text, color_code):
    colors = {
        "green": "\033[92m",  # צבע ירוק (פתוח)
        "red": "\033[91m",    # צבע אדום (סגור)
        "reset": "\033[0m"    # Reset (ללא צבע)
    }
    print(f"{colors.get(color_code, colors['reset'])}{text}{colors['reset']}")

# פונקציה לציור מצב הפורט
def draw_port_status(port, is_open):
    status = "🔓 Open" if is_open else "🔒 Closed"
    print(f"Port {port}: {status}")

# נבדוק כמה פורטים
def check_ports(host, ports):
    for port in ports:
        is_open = check_port(host, port)
        draw_port_status(port, is_open)
        print_colored(f"Port {port} is {'open' if is_open else 'closed'}", "green" if is_open else "red")
        time.sleep(0.5)

# הדפסת קווים עבור כל פורט (אפשר להוסיף יותר גרפיקה כאן)
def draw_ports(ports):
    print("\nStarting port scan...\n")
    print("-" * 30)
    check_ports("localhost", ports)
    print("-" * 30)

# רשימת פורטים לבדיקה
ports_to_check = [80, 443, 8080, 22, 3306]

# הרצת הפונקציה
draw_ports(ports_to_check)
