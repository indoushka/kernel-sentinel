#!/usr/bin/env python3
import json
from datetime import datetime
import os
import subprocess
import requests
from detector import إصدار_kernel_الحالي
from messages import MESSAGES
from config import load_config

CONFIG = load_config()
LOG_DIR = CONFIG.get("reports", {}).get("directory", "/var/log/kernel-sentinel/reports")
os.makedirs(LOG_DIR, exist_ok=True)

TELEGRAM_BOT_TOKEN = CONFIG.get("notifications", {}).get("telegram", {}).get("bot_token", "")
TELEGRAM_CHAT_ID = CONFIG.get("notifications", {}).get("telegram", {}).get("chat_id", "")
ADMIN_EMAIL = CONFIG.get("notifications", {}).get("email", {}).get("recipient", "admin@example.com")

def إنشاء_تقرير(تحديثات_kernel, lang):
    """
    إنشاء تقرير JSON وإرسال إشعارات Email / Telegram إذا وجدت تحديثات
    """
    التقرير = {
        "tool": CONFIG.get("tool", "Kernel Sentinel"),
        "version": CONFIG.get("version", "1.0.0"),
        "author": "Indoushka",
        "kernel_running": إصدار_kernel_الحالي(),
        "updates_detected": bool(تحديثات_kernel),
        "available_updates": تحديثات_kernel,
        "timestamp_utc": datetime.utcnow().isoformat() + "Z"
    }

    اسم_الملف = os.path.join(
        LOG_DIR,
        f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )

    try:
        with open(اسم_الملف, "w", encoding="utf-8") as f:
            json.dump(التقرير, f, indent=2, ensure_ascii=False)
        print(f"{MESSAGES[lang].get('report_generated','Report generated')}: {اسم_الملف}")
    except Exception as e:
        print(f"خطأ أثناء حفظ التقرير: {e}")
    if تحديثات_kernel:
        رسالة = (
            f"{MESSAGES[lang].get('updates_detected','Updates detected')}\n"
            f"Kernel: {إصدار_kernel_الحالي()}\n"
            f"Packages: {', '.join(تحديثات_kernel)}\n"
            f"Report: {اسم_الملف}\nBy Indoushka"
        )

        إرسال_البريد(ADMIN_EMAIL, MESSAGES[lang].get('email_subject','Kernel Update Notification'), رسالة)
        if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
            إرسال_Telegram(رسالة)

    return التقرير, اسم_الملف


def إرسال_البريد(to_email, subject, body):
    """
    إرسال بريد إلكتروني باستخدام أمر mail أو أي أداة SMTP مستقبلية
    """
    try:
        subprocess.run(['mail', '-s', subject, to_email], input=body, text=True)
    except Exception as e:
        print(f"خطأ أثناء إرسال البريد: {e}")


def إرسال_Telegram(message):
    """
    إرسال رسالة عبر Telegram Bot API
    """
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
        requests.post(url, data=data, timeout=10)
    except Exception as e:
        print(f"خطأ أثناء إرسال Telegram: {e}")
