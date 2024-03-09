# from flask import Flask, jsonify, request
# app = Flask("moshe")
# data = [
#     {"id": 1, "name": "Item 1"},
#     {"id": 2, "name": "Item 2"},
#     {"id": 3, "name": "Item 3"},
# ]
#
# def score_server():
#     with open("Scores.txt", "r") as f:
#         f.write(f"{POINTS_OF_WINNING}\n")
#
from flask import Flask, render_template

# import score

app = Flask(__name__)


@app.route('/')
def index():
    number = 42  # You can replace this with any number you want to display
    return render_template('index.html', number=number)


@app.errorhandler()
def not_found_error(error):
    return render_template('error.html', error_message='Page not found')


if __name__ == '__main__':
    app.run(debug=True)

app.run(host='127.0.0.1', port="8080")
