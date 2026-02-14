"""
Example upstream pipeline for Pipeline-Chaining.

When this pipeline finishes successfully, it automatically triggers chaining_downstream.
Configure downstream_triggers in pipeline.json.
"""
from datetime import datetime, timezone


def main():
    print(f"[chaining_upstream] Started at {datetime.now(timezone.utc).isoformat()}")
    print("Doing upstream work...")
    for i in range(3):
        print(f"  Step {i + 1}/3 complete")
    print("[chaining_upstream] Done. chaining_downstream will be triggered automatically.")


if __name__ == "__main__":
    main()
