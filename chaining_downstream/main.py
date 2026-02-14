"""
Example downstream pipeline for Pipeline-Chaining.

This pipeline is triggered automatically when chaining_upstream completes successfully.
"""
from datetime import datetime, timezone


def main():
    print(f"[chaining_downstream] Started at {datetime.now(timezone.utc).isoformat()}")
    print("Triggered by chaining_upstream. Doing downstream work...")
    print("[chaining_downstream] Done.")


if __name__ == "__main__":
    main()
