import time
import random
import sys

def main():
    print("Pipeline started. Waiting for 20 seconds before deciding fate...")
    for i in range(20):
        time.sleep(1)
        if (i + 1) % 5 == 0:
            print(f"Elapsed time: {i + 1} seconds...")
    
    fate = random.choice(["SUCCESS", "FAILURE"])
    print(f"Randomly determined outcome: {fate}")
    
    if fate == "FAILURE":
        print("Failing now!")
        sys.exit(1)
    
    print("Succeeding now!")

if __name__ == "__main__":
    main()
