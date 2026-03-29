import requests

def fetch_github_events(url, headers=None):
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"API Error: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request Failed: {e}")
        return None
