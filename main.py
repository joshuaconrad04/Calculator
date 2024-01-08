from flask import Flask, redirect,url_for,render_template, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def calculate():
    data = request.get_json()
    # Perform calculation
    # For simplicity, let's assume the data contains an 'expression' field
    try:
        result = eval(data['expression'])
    except Exception as e:
        result = str(e)
    return jsonify(result=result)

if __name__ =="__main__":
  app.run(port=5002, debug = True)
