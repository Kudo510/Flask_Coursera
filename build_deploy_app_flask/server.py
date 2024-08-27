from flask import Flask, render_template, request
from Maths.mathematics import sum, sub, mul
# Import the Maths package here

app = Flask("Mathematics Problem Solver")

@app.route("/sum")
def sum_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here
    return str(sum(num1, num2))

@app.route("/sub")
def sub_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here
    return str(sub(num1, num2))

@app.route("/mul")
def mul_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here  
    return str(mul(num1, num2))

# @app.route("/")
# def render_index_page():
#     # Write your code here

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
