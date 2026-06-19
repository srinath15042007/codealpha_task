# Phishing Awareness Training

## 📌 Project Description

This project is designed to educate users about phishing attacks and online scams.  
It explains how attackers trick users into revealing sensitive information such as:

- Passwords
- Banking details
- OTPs
- Credit card information

The project also demonstrates a simple Python-based phishing URL detector that identifies suspicious websites using common phishing indicators.

---

## 🎯 Objectives

- Understand phishing attacks
- Learn how phishing websites work
- Detect suspicious URLs
- Improve cybersecurity awareness
- Practice safe browsing habits

---

## 🚀 Features

✅ Detect suspicious URLs  
✅ Check HTTPS usage  
✅ Detect suspicious keywords  
✅ Detect IP-based URLs  
✅ Calculate phishing risk score  
✅ Beginner-friendly cybersecurity project  

---

## 🛠 Technologies Used

- Python 3
- VS Code
- Linux / Ubuntu / Kali Linux

---

## ⚙ Installation

### Step 1: Check Python

```bash
python3 --version
```

---

### Step 2: No External Libraries Required

This project uses built-in Python modules only.

---

## ▶ Running the Program

```bash
python3 PAT.py
```

---

## 📜 Python Code

```python
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

    # Check IP address in URL
    ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'

    if re.search(ip_pattern, parsed.netloc):
        print("[!] URL uses an IP address")
        score += 2

    # Suspicious words
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

    # Long URL detection
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
```

---

## 📷 Sample Input

```text
http://secure-login-bank.com/verify/account
```

---

## 📷 Sample Output

```text
Analyzing URL: http://secure-login-bank.com/verify/account

[!] URL is not using HTTPS
[!] Suspicious keyword found: login
[!] Suspicious keyword found: verify
[!] Suspicious keyword found: account

Risk Score: 4

⚠ Potential Phishing Website
```

---

## 🧠 Phishing Indicators Explained

| Indicator | Meaning |
|-----------|----------|
| No HTTPS | Website may be insecure |
| Suspicious Keywords | Common phishing terms |
| IP Address in URL | Often used in fake websites |
| Long URLs | Used to hide malicious links |

---

## 🔒 Cybersecurity Concepts Learned

- Phishing Awareness
- URL Analysis
- Social Engineering
- Safe Browsing
- Threat Detection

---

## 📌 Future Improvements

- GUI Interface
- Real-time Website Scanner
- Browser Extension
- Machine Learning Detection
- Email Phishing Scanner

---

## 👨‍💻 Author

Your Name
SRINATH T G

CodeAlpha Cyber Security Internship

---

## 📄 Disclaimer

This project is created for educational and awareness purposes only.  
It does not guarantee complete phishing detection accuracy.
