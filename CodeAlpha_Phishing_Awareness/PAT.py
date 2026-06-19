from urllib.parse import urlparse
import re

def check_url(url):
    score = 0

    parsed = urlparse(url)

    print("\nAnalyzing URL:", url)

    # Check HTTPS
    if parsed.scheme != "https":
        print("[!] URL is not using HTTPS")
        score += 1
    else:
        print("[✓] HTTPS detected")

    # Check for IP address
    ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
    if re.search(ip_pattern, parsed.netloc):
        print("[!] URL uses an IP address")
        score += 2

    # Suspicious keywords
    suspicious_words = [
        "login",
        "verify",
        "secure",
        "update",
        "banking",
        "account"
    ]

    for word in suspicious_words:
        if word in url.lower():
            print(f"[!] Suspicious keyword found: {word}")
            score += 1

    # Long URL
    if len(url) > 75:
        print("[!] URL is unusually long")
        score += 1

    print("\nRisk Score:", score)

    if score >= 3:
        print("⚠ Potential Phishing Website")
    else:
        print("✓ Appears Safe")


url = input("Enter URL to analyze: ")
check_url(url)
