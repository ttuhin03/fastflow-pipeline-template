import sys

def main():
    print("This pipeline is designed to fail for testing purposes.")
    print("Raising ValueError now...")
    raise ValueError("Intentional pipeline failure for error handling demo.")

if __name__ == "__main__":
    main()
