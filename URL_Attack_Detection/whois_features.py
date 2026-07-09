import whois

def get_whois_info(domain):

    try:
        info = whois.whois(domain)

        creation_date = info.creation_date
        expiration_date = info.expiration_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]

        return {
            "registrar": str(info.registrar),
            "creation_date": str(creation_date),
            "expiration_date": str(expiration_date)
        }

    except Exception:
        return {
            "registrar": "Not Available",
            "creation_date": "Not Available",
            "expiration_date": "Not Available"
        }