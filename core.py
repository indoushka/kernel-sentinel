#!/usr/bin/env python3

import sys
import os
from detector import فحص_التحديثات, إصدار_kernel_الحالي
from updater import تحديث_kernel
from reporter import إنشاء_تقرير, LOG_DIR
from messages import MESSAGES

# تأكيد وجود مجلد السجلات
os.makedirs(LOG_DIR, exist_ok=True)


def اكتشف_اللغة():
 
    lang = (
        os.environ.get("LC_MESSAGES")
        or os.environ.get("LANG")
        or "en"
    )
    return "ar" if lang.startswith("ar") else "en"


def تشغيل_الأداة(تحديث_تلقائي=False):
    lang = اكتشف_اللغة()

    print("\n===============================")
    print("Kernel Sentinel ️")
    print("By Indoushka")
    print("===============================")

    print(f"[+] {MESSAGES[lang]['kernel_current']}: {إصدار_kernel_الحالي()}")

    التحديثات = فحص_التحديثات()

    if التحديثات:
        print(f"\n{MESSAGES[lang]['updates_detected']}:")
        for تحديث in التحديثات:
            print(f"  - {تحديث}")

        if تحديث_تلقائي:
            print(f"\n{MESSAGES[lang]['auto_update_start']}")
            if تحديث_kernel():
                print(MESSAGES[lang]['update_success'])
            else:
                print(MESSAGES[lang]['update_failed'])
    else:
        print(f"\n{MESSAGES[lang]['no_updates']}")

    إنشاء_تقرير(التحديثات, lang)


if __name__ == "__main__":
    تحديث_تلقائي = "--تحديث" in sys.argv or "--update" in sys.argv
    تشغيل_الأداة(تحديث_تلقائي=تحديث_تلقائي)
