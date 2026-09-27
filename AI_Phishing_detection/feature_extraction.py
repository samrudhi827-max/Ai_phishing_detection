import re
from urllib.parse import urlparse


def extract_features(url):
    parsed_url = urlparse(url)

    features = {
        "url_length": len(url),
        "dot_count": url.count("."),
        "slash_count": url.count("/"),
        "hyphen_count": url.count("-"),
        "at_count": url.count("@"),
        "question_count": url.count("?"),
        "equal_count": url.count("="),
        "https": 1 if parsed_url.scheme == "https" else 0,
        "subdomain_count": max(0, len(parsed_url.hostname.split(".")) - 2)
        if parsed_url.hostname else 0,
        "has_ip": 1 if re.match(
            r"^\d{1,3}(\.\d{1,3}){3}$",
            parsed_url.hostname or ""
        ) else 0
    }

    return features