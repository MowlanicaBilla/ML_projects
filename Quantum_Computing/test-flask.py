import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/foo', methods=['POST']) 
def foo():
    #data = request.json
    data = request.get_data()
    data = json.dumps(data)
    load_data = json.loads(data)
    print(data)
    #data = jsonify(data)
    return type(data)


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=4000, debug=True)