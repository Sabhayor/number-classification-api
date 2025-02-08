from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number."""
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return n == sum(d**power for d in digits)

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    """Classify a number and return its properties."""
    number = request.args.get('number')

    # Validate input
    if not number.isdigit():
        return jsonify({"number": number, "error": True}), 400
    
    num = int(number)
    properties = []
    
    # Check properties
    if is_armstrong(num):
        properties.append("armstrong")
    if num % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    # Fetch fun fact
    fun_fact = "No fun fact available"
    try:
        response = requests.get(f"http://numbersapi.com/{num}")
        if response.status_code == 200:
            fun_fact = response.text
    except requests.exceptions.RequestException:
        pass

    result = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(num)),
        "fun_fact": fun_fact
    }

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
