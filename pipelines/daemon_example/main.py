"""
Example daemon pipeline (permanent mode).

This pipeline runs continuously with a while loop. It demonstrates:
- timeout: 0 - no timeout (runs indefinitely)
- restart_on_crash - automatically restarts if it crashes
- restart_cooldown - seconds to wait before restart after crash
- restart_interval - optional: regular restart (e.g. daily) via scheduler

In production, replace the dummy loop with your actual logic (e.g. Kafka consumer,
S3 file watcher, API polling).
"""
import time
from datetime import datetime, timezone


def main():
    print(f"[daemon_example] Started at {datetime.now(timezone.utc).isoformat()}")
    print("Daemon mode: running until interrupted. Use restart_on_crash for auto-restart.")
    count = 0
    while True:
        count += 1
        print(f"[daemon_example] Heartbeat #{count} at {datetime.now(timezone.utc).isoformat()}")
        time.sleep(10)


if __name__ == "__main__":
    exit(main())
