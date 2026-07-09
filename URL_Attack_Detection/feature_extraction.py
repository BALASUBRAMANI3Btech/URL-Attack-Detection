def extract_features(url):
    features = []

    # URL Length
    features.append(len(url))

    # Number of Dots
    features.append(url.count('.'))

    # Number of Hyphens
    features.append(url.count('-'))

    # Number of @ Symbols
    features.append(url.count('@'))

    # HTTPS Check
    if "https" in url:
        features.append(1)
    else:
        features.append(0)

    return features