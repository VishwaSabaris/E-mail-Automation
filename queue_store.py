import json

QUEUE_FILE = "queue.json"

def add_event(event):
    try:
        with open(QUEUE_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(event)

    with open(QUEUE_FILE, "w") as f:
        json.dump(data, f)


def get_events():
    try:
        with open(QUEUE_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def clear_events():
    with open(QUEUE_FILE, "w") as f:
        json.dump([], f)
