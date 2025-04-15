import subprocess
import re

def sanitize_input(domain):
    # Basic sanitization, but doesn't block command injection well
    return re.sub(r'[^a-zA-Z0-9\.\-]', '', domain)

def check_ping(domain):
    clean_domain = sanitize_input(domain)
    cmd = f"ping -c 1 {clean_domain}"
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL, timeout=3)
        return "Host is reachable"
    except subprocess.CalledProcessError:
        return "Host is unreachable"

if __name__ == "__main__":
    user_input = input("Enter a domain to ping: ")
    print(check_ping(user_input))
