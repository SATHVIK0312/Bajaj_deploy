from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

@app.route('/sathvik_post', methods=['POST'])
def handle_post():
    try:
        data = request.json.get('data', [])
        
        if not data:
            return jsonify({"is_success": False, "message": "Invalid input"}), 400
        
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        
        lowercase_alphabets = [char for char in alphabets if char.islower()]
        highest_lowercase = max(lowercase_alphabets, default=None)
        
        response = {
            "is_success": True,
            "user_id": "Sathvik",  
            "email": "saisathvik.sangaraju@gmail.com", 
            "roll_number": "21BDS0029r", 
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
        }
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500

@app.route('/sathvik_get', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
