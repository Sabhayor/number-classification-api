# Number Classification API

## Overview

The **Number Classification API** is a RESTful service built with **Python** and **Flask** that accepts a number and returns interesting mathematical properties about it, along with a fun fact.

The API classifies numbers based on their properties, such as whether they are prime, perfect, or Armstrong numbers, and calculates the sum of their digits. It also retrieves a fun fact related to the number.

## Features
- Classifies numbers by checking if they are prime, perfect, or Armstrong numbers.
- Calculates the sum of digits of a number.
- Provides a fun fact about the number.

## Technology Stack
- **Python**: The backend programming language.
- **Flask**: Lightweight web framework to build the API.
- **CORS (Cross-Origin Resource Sharing)**: To ensure the API is accessible from various domains.
- **GitHub**: Version control to host the project code.

## API Endpoint

**Endpoint**: `GET <your-url>/api/classify-number?number=<number>`

### Request Parameters

- `number`: The integer number that needs to be classified. 

### Response Formats

#### 1. Successful Response (200 OK)

**Example Request:**
```http
GET <your-url>/api/classify-number?number=371
```

**Example Response:**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

- `number`: The number being classified.
- `is_prime`: Boolean indicating whether the number is a prime number.
- `is_perfect`: Boolean indicating whether the number is a perfect number.
- `properties`: A list of properties the number holds (e.g., Armstrong, odd, etc.).
- `digit_sum`: The sum of the digits of the number.
- `fun_fact`: A fun fact related to the number.

#### 2. Error Response (400 Bad Request)

**Example Request:**
```http
GET <your-url>/api/classify-number?number=alphabet
```

**Example Response:**
```json
{
    "number": "alphabet",
    "error": true
}
```

- `number`: The invalid input that caused the error.
- `error`: Boolean indicating that an error occurred due to invalid input.

### Error Handling
- The API returns a 400 HTTP status code if the input is not a valid integer (e.g., if a string or non-numeric value is provided).
- Proper validation is implemented to ensure only valid integers are processed.

## Code Quality

- The API follows a modular and organized code structure for better readability and maintainability.
- Basic error handling and input validation are in place to ensure stability.
- The code avoids hardcoded values and uses dynamic inputs wherever applicable.

## Deployment

- The API is hosted on a publicly accessible endpoint, ensuring it can be reached from external applications.
- Response times are optimized to ensure that the API responds within 500ms.

## Installation Instructions

To run the Number Classification API locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-github-username>/number-classification-api.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd number-classification-api
   ```

3. **Install dependencies**:
   You need `Flask` and `Flask-CORS`. Install them using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask Application**:
   ```bash
   python app.py
   ```

5. **Access the API**:
   The API will be running locally on `http://127.0.0.1:5000/`. You can test it by visiting:
   ```http
   http://127.0.0.1:5000/api/classify-number?number=371
   ```

## CORS (Cross-Origin Resource Sharing)

CORS support is enabled to ensure that the API can be accessed from different domains and can be used in front-end applications, such as JavaScript apps.

## GitHub Repository

The full source code for the project is available on GitHub at:

[GitHub Repository](https://github.com/<your-github-username>/number-classification-api)

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Fun fact API: [Numbers API](http://numbersapi.com/#42)
- Mathematical properties information: [Wikipedia - Parity (Mathematics)](https://en.wikipedia.org/wiki/Parity_(mathematics))

