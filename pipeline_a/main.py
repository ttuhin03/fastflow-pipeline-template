import os
import requests
from datetime import datetime

def main():
    """
    Standard example pipeline showing environment variable usage 
    and external dependency (requests).
    """
    api_key = os.getenv("API_KEY", "default-key")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    
    print(f"[{log_level}] {datetime.now().isoformat()} - Pipeline A started.")
    print(f"Using API Key: {api_key[:4]}****")
    
    # Example logic
    print("Fetching sample data...")
    # response = requests.get("https://api.github.com")
    # print(f"Status Code: {response.status_code}")
    
    print("Processing completed successfully.")

if __name__ == "__main__":
    main()
