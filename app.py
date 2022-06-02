from flask import Flask, jsonify, request
import backend


app = Flask(__name__)


@app.route('/')
def home():
    return 'hello world'


# @app.route('/help')
# @app.route('/routes')
# def routes():
#     return jsonify({
#         'routes': {
#             '/': 'home route',
#             '/publishedResults': 'published results',
#             '/allAttemptedResults': 'allAttemptedResults (usage: .../allAttemptedResults?rollno=163g1a0505&course=b.tech&regulation=r15)',
#             '/urls/allUrls': 'all r15 urls'
#         }})


# @app.route('/publishedResults')
# def allResults():
#     data = Automate.getPublishedResults()
#     return jsonify({
#         'published_results': data
#     })


# @app.route('/urls/allUrls')
# def allUrls():
#     x = Automate.getAllUrls()
#     x = x[7:-5]
#     return jsonify(x)


@app.route('/allAttemptedResults',  methods=['GET'])
def result():
    """
    usage:
    .../allAttemptedResults?rollno=<>

    eg:
    .../allAttemptedResults?htno=163g1a0000

    """
    htno = request.args.get('htno')
    # need to validate the query paramerters before making the call
    data = backend.main(htno)
    print(data)
    return jsonify(data)


if __name__ == "__main__":
    app.run()
