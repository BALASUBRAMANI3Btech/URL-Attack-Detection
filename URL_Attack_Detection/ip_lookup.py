import socket

try:
    domain = input("Enter Domain: ")

    ip = socket.gethostbyname(domain)

    print("\nDomain:", domain)
    print("IP Address:", ip)

except:
    print("Invalid Domain")