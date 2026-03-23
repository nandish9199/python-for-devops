#!/usr/bin/env python3

import shutil
import sys

THRESHOLD = 20  # Alert if usage > 80%

def check_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)

    total_gb = total // (2**30)
    used_gb = used // (2**30)
    free_gb = free // (2**30)

    percent_used = (used / total) * 100

    print(f"\nDisk Usage Report for {path}")
    print("-" * 40)
    print(f"Total: {total_gb} GB")
    print(f"Used : {used_gb} GB")
    print(f"Free : {free_gb} GB")
    print(f"Usage: {percent_used:.2f}%")

    if percent_used > THRESHOLD:
        print("\n⚠ WARNING: Disk usage exceeded threshold!")
        sys.exit(1)  # Useful for Jenkins/Monitoring
    else:
        print("\n✅ Disk usage is under control.")
        sys.exit(0)

if __name__ == "__main__":
    check_disk_usage("/")