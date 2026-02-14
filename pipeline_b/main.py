import sys

def main():
    """
    Example pipeline showing alternative JSON naming support.
    """
    print("Pipeline B: Data Processor")
    print("This pipeline uses 'data_processor.json' instead of 'pipeline.json'.")
    
    # Simulate some work
    for i in range(5):
        print(f"Phase {i+1} complete...")

if __name__ == "__main__":
    main()
