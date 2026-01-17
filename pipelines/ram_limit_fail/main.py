import time
import sys

def consume_memory():
    print("Pipeline started. Attempting to consume ~100MB of RAM...")
    # Create a list of 12.5 million floats (~100MB)
    # Each float in Python is usually 24-32 bytes, but in a list it's more compact
    # We'll use a bytearray for more predictable memory usage
    try:
        data = bytearray(100 * 1024 * 1024) 
        print("Successfully allocated 100MB.")
        print("Waiting 10 seconds to keep memory active...")
        time.sleep(10)
    except MemoryError:
        print("Caught MemoryError! The system OOM-killed us or refused allocation.")
        sys.exit(1)

if __name__ == "__main__":
    consume_memory()
