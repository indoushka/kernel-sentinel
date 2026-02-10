#!/usr/bin/env python3
import subprocess
from config import load_config

CONFIG = load_config()

def تشغيل_الأمر(الأمر):
    """Execute a system command safely and return stdout"""
    try:
        نتيجة = subprocess.run(
            الأمر,
            capture_output=True,
            text=True,
            check=True
        )
        return نتيجة.stdout.strip()
    except subprocess.CalledProcessError:
        return ""

def إصدار_kernel_الحالي():
    """Return current kernel version"""
    return تشغيل_الأمر(["uname", "-r"])

def فحص_التحديثات():
    """Check for available kernel updates according to policy"""
    تشغيل_الأمر(["apt", "-qq", "update"])
    تحديثات_قابلة_للتحديث = تشغيل_الأمر(
        ["apt", "list", "--upgradable"]
    ).splitlines()

    تحديثات_kernel = [
        u for u in تحديثات_قابلة_للتحديث
        if any(k in u for k in ["linux-image", "linux-headers"])
    ]

    allowed_flavors = CONFIG.get("kernel_policy", {}).get("auto_update_flavors", [])
    التحديثات_المسموح بها = [
        u for u in تحديثات_kernel
        if any(f in u for f in allowed_flavors)
    ]

    return {
        "update_available": bool(تحديثات_kernel),
        "all_updates": تحديثات_kernel,
        "allowed_updates": التحديثات_المسموح بها
    }
