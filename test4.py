# # pyright: reportMissingImports=false
# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def home():
#     return "Hello Hassan, Welcome to Flask!"


# if __name__ == "__main__":
#     app.run(debug=True)


def fun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for val in fun():
    print(val)
