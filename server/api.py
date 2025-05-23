import os
import jwt
import datetime
import psycopg2

from flask import Flask, request, jsonify
from flask_cors import CORS
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

app = Flask(__name__)
cors = CORS(app, origins='*')

# Members API route
@app.route("/api/users", methods=["GET"])
def users():
    return jsonify(
        {
            "users": [
                'Alice',
                'Bob',
                'Charlie'
            ]
        }
    )

if __name__ == "__main__":
    app.run(debug=True, port=8080)