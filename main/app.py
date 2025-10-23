from flask import Flask, request, jsonify

app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return "Welcome to the Flask app!", 200

# Health check route
@app.route('/health')
def health():
    return jsonify(status="healthy"), 200

# Simple POST endpoint
@app.route('/data', methods=['POST'])
def data():
    # Expect JSON data
    if not request.is_json:
        return jsonify(error="Invalid content type. Expected application/json."), 400
    
    content = request.get_json()
    return jsonify(
        message="Data received successfully",
        received_data=content
    ), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
