from flask import Flask, jsonify, request
from automate import Automate


app = Flask(__name__)


@app.route('/')
def home():
    return 'hello world'


@app.route('/routes')
def routes():
    return jsonify({
        'routes': {
            '/': 'home route',
            '/publishedResults': 'published results',
            '/allAttemptedResults': 'allAttemptedResults',
            '/urls/allUrls': 'all r15 urls'
        }})


@app.route('/publishedResults')
def allResults():
    data = Automate.getPublishedResults()
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
    """
    usage:
    .../allAttemptedResults?rollno=<>&course=<>&regulation=<>
    """
    rollno = request.args.get('rollno')
    course = request.args.get('course')
    regulation = request.args.get('regulation')

    regulation = regulation.upper()
    tmp = course[0:3]
    t = tmp.upper()
    course = t + course[3:]
    regulation = regulation.upper()
    
    print("++++++++++")
    print(rollno, course, regulation)
    print("++++++++++")
    x = Automate(rollno=rollno, course=course, regulation=regulation)
    data = x.start()
    return data


if __name__ == "__main__":
    app.run()
