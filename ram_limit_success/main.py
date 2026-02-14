import time
import sys

def consume_memory():
    print("Pipeline started. Attempting to consume ~100MB of RAM...")
    # Allocate 100MB
    try:
        data = bytearray(100 * 1024 * 1024) 
        print("Successfully allocated 100MB.")
        print("This is within the 256MB limit, so this pipeline should succeed.")
        print("Waiting 10 seconds to keep memory active...")
        time.sleep(10)
        print("Done.")
    except MemoryError:
        print("Caught unexpectedly MemoryError!")
        sys.exit(1)

if __name__ == "__main__":
    consume_memory()
