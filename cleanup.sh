#!/bin/bash
# Reset interfaces
echo -e "\033[95mCleaning up...\033[0m"
sudo airmon-ng stop wlan0mon 2>/dev/null
sudo systemctl restart NetworkManager