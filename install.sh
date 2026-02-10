#!/usr/bin/env bash
set -e

LANG_SYS=${LANG:-en}
if [[ "$LANG_SYS" == ar* ]]; then
  MSG_START="بدء تثبيت Kernel Sentinel"
  MSG_ROOT="يجب تشغيل السكربت بصلاحيات root"
  MSG_DONE="✔ تم تثبيت Kernel Sentinel بنجاح"
else
  MSG_START="Starting Kernel Sentinel installation"
  MSG_ROOT="This installer must be run as root"
  MSG_DONE="✔ Kernel Sentinel installed successfully"
fi

echo "Kernel Sentinel - By Indoushka"
echo "================================"
echo "$MSG_START"
echo

if [[ "$EUID" -ne 0 ]]; then
  echo "$MSG_ROOT"
  exit 1
fi

apt update
apt install -y python3 python3-requests mailutils

mkdir -p /usr/lib/kernel-sentinel
mkdir -p /var/log/kernel-sentinel/reports
mkdir -p /etc/kernel-sentinel
cp core.py detector.py updater.py reporter.py messages.py config.json /usr/lib/kernel-sentinel/
cp systemd/kernel-sentinel.service systemd/kernel-sentinel.timer /etc/systemd/system/
chmod +x /usr/lib/kernel-sentinel/*.py
chown -R root:root /usr/lib/kernel-sentinel /var/log/kernel-sentinel
systemctl daemon-reload
systemctl enable kernel-sentinel.timer
systemctl start kernel-sentinel.timer

echo
echo "$MSG_DONE"
echo "systemd timer is active (runs every 6 hours)"
