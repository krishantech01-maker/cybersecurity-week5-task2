import requests

target_url = "http://localhost:3000"  # Local test target (e.g., OWASP Juice Shop / DVWA)

security_headers = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Referrer-Policy"
]

print(f"--- Checking Security Headers for {target_url} ---")
try:
    response = requests.get(target_url, timeout=5)
    for header in security_headers:
        if header in response.headers:
            print(f"[+] Present: {header} -> {response.headers[header]}")
        else:
            print(f"[-] Missing: {header} (Potential Risk)")
except requests.exceptions.RequestException as e:
    print(f"Connection failed (ensure local target is running): {e}")
