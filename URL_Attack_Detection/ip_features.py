import socket

def get_ip(url):

    try:
        domain = url.replace("https://", "")
        domain = domain.replace("http://", "")
        domain = domain.split("/")[0]

        ip = socket.gethostbyname(domain)

        return ip

    except:
        return "Not Found"