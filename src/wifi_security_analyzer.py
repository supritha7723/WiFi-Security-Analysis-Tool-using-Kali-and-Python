import random
from datetime import datetime

print("WiFi Security Analysis Tool (Version 2 - Easy Demo)\n")

# Random networks every time
networks = []
names = ["Home-WiFi", "Office-Net", "Cafe-Guest", "Lab-Network", "Neighbor-WiFi", "School-Net"]
for i in range(5):
    networks.append({
        "name": random.choice(names),
        "bssid": f"{random.randint(10,99)}:{random.randint(10,99)}:{random.randint(10,99)}:AA:BB:CC",
        "channel": random.randint(1, 13),
        "signal": random.randint(-85, -30),
        "encryption": random.choice(["WPA2", "WPA3", "Open"])
    })
  
# Menu
print("Choose what you want to do:")
print("1. Scan nearby networks")
print("2. Capture WPA Handshake (demo)")
print("3. Exit")
choice = input("\nEnter 1, 2 or 3: ")

if choice == "1":
    print("\n📡 Scanning nearby WiFi networks...\n")
    print("BSSID                Name               Channel  Signal   Encryption")
    print("-" * 65)
    for net in networks:
        print(f"{net['bssid']:<20} {net['name']:<18} {net['channel']:<7} {net['signal']:<6} {net['encryption']}")

elif choice == "2":
    print("\n🔑 Capturing WPA Handshake (demo mode)...")
    print("   → Target selected: Lab-Network")
    print("   → Handshake captured successfully! (fake)")
    print("   → This shows how hackers can steal the handshake to crack passwords later.")

 Create report
report_name = "report_wifi_analysis.txt"
with open(report_name, "w") as f:
    f.write("WiFi Security Analysis Report\n")
    f.write(f"Generated on: {datetime.now().strftime('%d %B %Y %H:%M')}\n")
    f.write("=" * 60 + "\n\n")
    f.write("BSSID                Name               Channel  Signal   Encryption\n")
    f.write("-" * 65 + "\n")
    for net in networks:
        f.write(f"{net['bssid']:<20} {net['name']:<18} {net['channel']:<7} {net['signal']:<6} {net['encryption']}\n")
    f.write("\nSecurity Recommendation: Always use WPA3 and strong password!\n")
    f.write("Report created for OJT-3 project\n")

print(f"\nDone! Report saved as: {report_name}")
print("   Open the file to see the full report.")
