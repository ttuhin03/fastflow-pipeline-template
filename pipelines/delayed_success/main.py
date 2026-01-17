import time
import sys

def main():
    print("Pipeline started. Waiting for 20 seconds...")
    for i in range(20):
        time.sleep(1)
        if (i + 1) % 5 == 0:
            print(f"Elapsed time: {i + 1} seconds...")
    
    print("Wait completed successfully. Finishing pipeline.")

if __name__ == "__main__":
    main()
