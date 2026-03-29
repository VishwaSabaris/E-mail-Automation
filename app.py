import os
from dotenv import load_dotenv
from services.api_service import fetch_github_events
from utils.processor import process_event

load_dotenv()

def main():
    username = os.getenv("GITHUB_USERNAME")
    api_key = os.getenv("API_KEY")

    if not username:
        print("Missing username in .env")
        return

    url = f"https://api.github.com/users/{username}/events"

    headers = {}

    data = fetch_github_events(url, headers)

    if not data:
        print("API request failed")
        return

    print(f"\nProcessing events for: {username}\n")

    for event in data[:5]:
        processed = process_event(event, username)
        print(processed)
        print("-" * 50)

if __name__ == "__main__":
    main()
