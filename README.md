🛡️ Kernel Sentinel
Smart Kernel Security Update Monitor

By Indoushka

📌 Overview

Kernel Sentinel is a smart, modular, production-ready Linux tool designed to monitor Kernel security updates only, generate audit-ready JSON reports, and send real-time notifications.

It automatically detects the system language and interacts with the user accordingly (Arabic / English).

✨ Key Features

🧠 Smart: Automatically detects system language (Arabic / English)

🧩 Modular Architecture (easy to maintain & extend)

🛡️ Kernel-focused security monitoring

📄 Structured JSON reports (audit & compliance ready)

⏱️ systemd service + timer (fully integrated)

📬 Email notifications

📢 Telegram bot notifications

🧾 Enterprise & production ready

✍️ Author signature embedded (Indoushka)

🏗️ Project Structure
kernel-sentinel/
├── core.py
├── detector.py
├── updater.py
├── reporter.py
├── messages.py
├── config.json
├── systemd/
│   ├── kernel-sentinel.service
│   └── kernel-sentinel.timer
├── README.md
├── LICENSE

⚙️ Requirements

Linux (Ubuntu / Debian)

Python 3.8+

systemd

Root privileges

Dependencies
sudo apt install python3 python3-requests mailutils -y

🚀 Installation
# Create directories
sudo mkdir -p /usr/lib/kernel-sentinel
sudo mkdir -p /var/log/kernel-sentinel/reports
sudo mkdir -p /etc/kernel-sentinel

# Copy files
sudo cp *.py config.json /usr/lib/kernel-sentinel/
sudo cp systemd/kernel-sentinel.* /etc/systemd/system/

# Permissions
sudo chmod +x /usr/lib/kernel-sentinel/*.py

# Enable service
sudo systemctl daemon-reload
sudo systemctl enable kernel-sentinel.timer
sudo systemctl start kernel-sentinel.timer

▶️ Manual Run
sudo python3 /usr/lib/kernel-sentinel/core.py --تحديث

🌍 Language Support

Kernel Sentinel automatically detects system language:

LANG=ar_* → Arabic output

LANG=en_* → English output

No manual configuration required.

📬 Notifications Setup
📧 Email

Requires mailutils or configured SMTP

Set admin email in reporter.py

📢 Telegram

Create a bot via @BotFather

Get BOT_TOKEN

Get your CHAT_ID

Add them in reporter.py

TELEGRAM_BOT_TOKEN = "YOUR_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

📄 Sample JSON Report
{
  "tool": "Kernel Sentinel",
  "version": "1.0.0",
  "author": "Indoushka",
  "kernel_running": "6.8.0-35-generic",
  "updates_detected": true,
  "timestamp_utc": "2026-02-10T18:22:11Z"
}

🧩 Why Kernel Sentinel?
Feature	Kernel Sentinel	Others
Kernel-only focus	✅	❌
Multi-language	✅	❌
JSON compliance reports	✅	❌
Modular architecture	✅	❌
systemd native	✅	❌
Open & extensible	✅	❌
🧠 What “Modular” Means

Each component works independently:

core.py → Engine & language detection

detector.py → Kernel update detection

updater.py → Controlled updates

reporter.py → Reports & notifications

messages.py → Localization

This makes the tool stable, maintainable, and enterprise-grade.

📜 License

MIT License
Free to use, modify, and distribute.

✍️ Author

Indoushka
Kernel Sentinel is built to leave a technical fingerprint in Linux security tooling.
