from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

# Load quotes from a JSON file
with open('quotes.json', 'r') as file:
    quotes = json.load(file)["quotes"]

@app.route('/', methods=['GET'])
def get_random_quote():
    # Select a random quote
    random_quote = random.choice(quotes)

    # Return the quote as JSON
    return jsonify({'quote': random_quote})

if __name__ == '__main__':
    app.run(debug=True)
