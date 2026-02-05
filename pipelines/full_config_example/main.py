"""
Example pipeline with every pipeline.json field set (maximal config).
Use this as a reference for all available options.
"""
import os
import sys
from datetime import datetime, timezone


def main():
    print(f"[full_config_example] Run at {datetime.now(timezone.utc).isoformat()}")
    print(f"LOG_LEVEL from default_env: {os.getenv('LOG_LEVEL', 'not set')}")
    print(f"MY_VAR from default_env: {os.getenv('MY_VAR', 'not set')}")
    print("Maximal config pipeline completed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
