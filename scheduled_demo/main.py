"""
Example pipeline for scheduled (cron) execution.

This pipeline is meant to be run on a schedule via the Fast-Flow Scheduler.
Add a job in the UI (Scheduler) with a cron expression (e.g. "0 9 * * *" for daily at 09:00)
or an interval in seconds, and select this pipeline.
"""
from datetime import datetime, timezone


def main():
    print(f"[scheduled_demo] Run at {datetime.now(timezone.utc).isoformat()}")
    print("Scheduled job executed successfully.")
    return 0


if __name__ == "__main__":
    exit(main())
