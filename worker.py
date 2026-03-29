import time
from queue_store import get_events, clear_events, add_event
from utils.processor import process_event

# -------------------------------
# 🔹 OPTIONAL: Inject Test Event
# (Use only for testing)
# -------------------------------
def inject_test_event():
    add_event({
        "event": "PushEvent",
        "repo": "test/repo",
        "time": "2026-03-26T23:30:00Z"
    })
    print("🧪 Test event added to queue")


# -------------------------------
# 🔹 Worker Logic
# -------------------------------
def worker():
    print("🚀 Worker started...")
    
    while True:
        events = get_events()

        if events:
            print(f"⚙️ Processing {len(events)} event(s)...")

            for event in events:
                try:
                    processed = process_event(event)
                    print("✅ Processed:", processed)
                except Exception as e:
                    print("❌ Error processing event:", str(e))

            # Clear queue after processing
            clear_events()
            print("🧹 Queue cleared")

        else:
            print("👀 Waiting for events...")

        time.sleep(5)  # simulate async polling


# -------------------------------
# 🔹 Run Worker
# -------------------------------
if __name__ == "__main__":
    # 🔥 Uncomment this ONLY for testing
    # inject_test_event()

    worker()
