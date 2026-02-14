"""
Example pipeline for one-time (run_once_at) execution.

This pipeline runs once at the datetime specified in pipeline.json under "run_once_at".
Set run_once_at to an ISO datetime in the future (e.g. "2025-12-31T14:00:00").
After Git-Sync or app startup, Fast-Flow creates a scheduler job that runs this pipeline
exactly once at the specified time.
"""
from datetime import datetime, timezone


def main():
    print(f"[run_once_example] Run at {datetime.now(timezone.utc).isoformat()}")
    print("One-time scheduled job executed successfully.")
    return 0


if __name__ == "__main__":
    exit(main())
