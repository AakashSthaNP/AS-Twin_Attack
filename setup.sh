#!/bin/bash
# A A K A S H Attack Setup
echo -e "\033[95mInstalling dependencies...\033[0m"
sudo apt update && sudo apt install -y aircrack-ng hostapd dnsmasq python3-scapy
sudo airmon-ng check kill
chmod +x A-A-K-A-S-H.py