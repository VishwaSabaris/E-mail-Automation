from flask import Flask, request, jsonify
from database import init_db, insert_event
import sqlite3

app = Flask(__name__)

# 🔐 API Key (move to .env later)
API_KEY = "SECRET123"

# 🧠 Initialize DB
init_db()


# 🏠 Home route
@app.route("/", methods=["GET"])
def home():
    return "Backend is running 🚀"


# 🔗 Route used by n8n
@app.route("/external-api", methods=["POST"])
def external_api():
    try:
        data = request.get_json()

        # ❌ No JSON
        if not data:
            return jsonify({"error": "No JSON data received"}), 400

        # 🔐 API key validation
        if data.get("api_key") != API_KEY:
            return jsonify({"error": "Unauthorized"}), 401

        payload = data.get("payload")

        # ❌ No payload
        if not payload:
            return jsonify({"error": "No payload found"}), 400

        # ⚙️ Process event
        result = process_event(payload)

        # 💾 Store in DB
        insert_event(result)

        return jsonify({
            "status": "success",
            "processed": result
        }), 200

    except Exception as e:
        return jsonify({
            "error": "Server error",
            "message": str(e)
        }), 500


# ⚙️ Event processing logic
def process_event(data):
    event = data.get("event")
    repo = data.get("repo")
    user = data.get("user")
    time = data.get("time")

    status = "Normal Activity"

    # ⏱ Detect late activity
    if time:
        try:
            hour = int(time[11:13])
            if hour >= 22:
                status = "Late Activity"
        except:
            status = "Invalid Time Format"

    return {
        "event": event,
        "repo": repo,
        "user": user,
        "time": time,
        "status": status
    }


# 📊 Get all stored events
@app.route("/events", methods=["GET"])
def get_events():
    try:
        conn = sqlite3.connect("events.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM events")
        rows = cursor.fetchall()

        conn.close()

        # Convert to readable format
        events = []
        for row in rows:
            events.append({
                "id": row[0],
                "event": row[1],
                "repo": row[2],
                "user": row[3],
                "time": row[4],
                "status": row[5]
            })

        return jsonify({"events": events}), 200

    except Exception as e:
        return jsonify({
            "error": "Failed to fetch events",
            "message": str(e)
        }), 500


# 🔁 Optional: Direct GitHub webhook (for future use)
@app.route("/webhook", methods=["POST"])
def github_webhook():
    data = request.json
    print("📥 GitHub event received:", data)

    return jsonify({"status": "received"}), 200


# 🚀 Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
