from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})


@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data found'}), 400
    
    if 'name' in data:
        if not isinstance(data['name'], str):
            return jsonify({"error": "Invalid 'name' field"}), 400
    
    name = data.get('name', 'Guest')
    return jsonify({'message': f'Hello, {name.strip()}! You sent a POST Request.'}), 200


if __name__ == '__main__':
    app.run(debug=True)