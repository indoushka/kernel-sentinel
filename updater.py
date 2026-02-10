#!/usr/bin/env python3
import subprocess
from config import load_config

CONFIG = load_config()

def تحديث_kernel():
    """
    Apply kernel updates according to policy
    Requires root privileges
    """
    if not CONFIG.get("security", {}).get("require_root", True):
        return False

    from detector import فحص_التحديثات
    updates_info = فحص_التحديثات()
    allowed = updates_info["allowed_updates"]

    if not allowed:
        return False  

    try:
        subprocess.run(
            ["apt", "install", "-y"] + allowed,
            check=True
        )
        return True
    except subprocess.CalledProcessError:
        return False
