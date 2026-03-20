WiFi-Security-Analysis-Tool-using-Kali-and-python

 Project Overview:
This project demonstrates basic WiFi network security auditing using Kali Linux tools and custom Python automation.

What it does (simple explanation):
- Puts WiFi adapter into monitor mode
- Scans nearby WiFi networks (shows SSID, BSSID, channel, encryption, signal)
- Captures WPA/WPA2 handshake (4-way handshake) from a target network
- Automatically creates a text report with scan results
- Helps understand how weak WiFi passwords can be tested (for educational/lab use only)

Important Note:  
This project is for authorized lab/testing networks only. Never use on real networks without permission — it is illegal.

Technologies Used:
- Kali Linux:- (or any Linux with aircrack-ng)
- Aircrack-ng suite:- (airmon-ng, airodump-ng, aireplay-ng)
- Python 3:- (custom automation script)
- Libraries: subprocess, csv, time, os, datetime

Features:
- Menu-driven Python script
- Automatic monitor mode setup
- Network scanning + CSV parsing
- Handshake capture with deauthentication
- Generates clean text report


