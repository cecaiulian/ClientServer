from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data storage
data = {
    "messages": []
}

@app.route('/api/messages', methods=['GET'])
def get_messages():
    return jsonify(data["messages"]), 200

@app.route('/api/messages', methods=['POST'])
def post_message():
    message = request.json.get("message")
    if message:
        data["messages"].append(message)
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error", "message": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
