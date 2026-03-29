def process_event(data):
    event = data.get("event", "Unknown")
    repo = data.get("repo", "unknown/repo")
    time = data.get("time", "")

    try:
        hour = int(time[11:13])
    except:
        hour = 0

    status = "Late Activity" if hour >= 22 else "Normal Activity"

    return {
        "user": "vishwa",
        "event": event,
        "repo": repo,
        "time": time,
        "status": status
    }
