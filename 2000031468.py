from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/numbers')
def get_numbers():
    urls = request.args.getlist('uri')
    numbers = set()

    for url in urls:
        try:
            response = requests.get(url, timeout=0.5)
            if response.status_code == 200:
                data = response.json()
                numbers.update(data['numbers'])
        except requests.Timeout:
            pass

    merged_numbers = sorted(numbers)

    return jsonify(numbers=merged_numbers)

if __name__ == '__main__':
    app.run(host='localhost', port=8008)
