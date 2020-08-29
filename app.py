from flask import Flask, jsonify, request
from automate import Automate


app = Flask(__name__)


@app.route('/')
def home():
    return 'hello world'


@app.route('/routes')
def home():
    return jsonify({
        'routes': {
            '/': 'home route',
            '/publishedResult' : 'published results',
            '/allAttemptedResults' : 'allAttemptedResults',
            '/urls/allUrls' : 'all r15 urls'
        }})

@app.route('/publishedResults')
def allResults():
    data = Automate.getAllResultsData()
    return jsonify({
        'published_results': data
    })


@app.route('/urls/allUrls')
def allUrls():
    x = Automate.getAllUrls()
    x = x[7:-5]
    return jsonify(x)


@app.route('/allAttemptedResults',  methods=['GET'])
def result():
    rn = request.args.get('rollno')
    print(rn)
    x = Automate(rollno=rn)
    data = x.start()
    return data


if __name__ == "__main__":
    app.run()
