from flask import Flask, jsonify, request
from automate import Automate


app = Flask(__name__)


@app.route('/')
def home():
    return 'hello world'


@app.route('/allResutlsData')
def allResults():
    data = Automate.getAllResultsData()
    return jsonify(data)


@app.route('/urls/allUrls')
def allUrls():
    x = Automate.getAllUrls()
    x = x[7:-5]
    return jsonify(x)


@app.route('/all-attempted-results-data',  methods=['GET'])
def result():
    rn = request.args.get('rollno')
    print(rn)
    x = Automate(rollno=rn)
    data = x.start()
    return data


if __name__ == "__main__":
    app.run()
