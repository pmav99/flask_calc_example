# -*- coding: utf-8 -*-
# module: my_app.py
# author: Panagiotis Mavrogiorgos <pmav99,gmail>

from flask import Flask, request, render_template, session

import calculations


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate_area', methods=["GET"])
def calculate_area_get():
    return render_template("calculate_area.html")


@app.route('/calculate_area', methods=["POST"])
def calculate_area_post():
    email = request.form["email"]
    x = float(request.form['x'])
    y = float(request.form['y'])
    area = calculations.calculate_area(x, y)
    return render_template('results_area.html', x=x, y=y, area=area)


@app.route('/calculate_square', methods=["GET"])
def calculate_square_get():
    return render_template("calculate_square.html")


@app.route('/calculate_square', methods=["POST"])
def calculate_square_post():
    n = float(request.form['n'])
    square = calculations.calculate_square(n)
    return render_template('results_square.html', n=n, square=square)


@app.route('/calculate_cube', methods=["GET"])
def calculate_cube_get():
    return render_template("calculate_cube.html")


@app.route('/calculate_cube', methods=["POST"])
def calculate_cube_post():
    n = float(request.form['n'])
    cube = calculations.calculate_cube(n)
    return render_template('results_cube.html', n=n, cube=cube)


if __name__ == '__main__':
    app.run(debug=True)
