
import dns.resolver

def get_dns_records(domain):

    dns_info = {
        "A": [],
        "MX": [],
        "NS": []
    }

    try:
        # A Records (IPv4 Addresses)
        answers = dns.resolver.resolve(domain, "A")
        for record in answers:
            dns_info["A"].append(str(record))
    except:
        dns_info["A"].append("Not Available")

    try:
        # MX Records (Mail Servers)
        answers = dns.resolver.resolve(domain, "MX")
        for record in answers:
            dns_info["MX"].append(str(record.exchange))
    except:
        dns_info["MX"].append("Not Available")

    try:
        # NS Records (Name Servers)
        answers = dns.resolver.resolve(domain, "NS")
        for record in answers:
            dns_info["NS"].append(str(record.target))
    except:
        dns_info["NS"].append("Not Available")

    return dns_info