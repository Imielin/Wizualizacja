import os
import numpy
import pandas
from flask import Flask, render_template, json, request, redirect, url_for

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__)) # refers to application_top
APP_DATA = os.path.join(APP_ROOT, 'data')

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')


@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    filename = os.path.join(APP_DATA,'narodziny.csv')
    csv_data = pandas.read_csv('data/narodziny.csv', delimiter=',', index_col='Country Code')
    year = '1960'
    proj = '0,0'
    csv_data = csv_data.round(2)
    data_environment = csv_data[year]
    colors = []
    for row in data_environment:
        if row > 54:
            colors.append('A')
        elif row > 48:
            colors.append('B')
        elif row > 42:
            colors.append('C')
        elif row > 36:
            colors.append('D')
        elif row > 30:
            colors.append('E')
        elif row > 24:
            colors.append('F')
        elif row > 18:
            colors.append('G')
        elif row > 12:
            colors.append('H')
        elif row > 6:
            colors.append('I')
        elif row > 0:
            colors.append('J')
        else:
            colors.append('Failed')

    csv_data['colors'] = colors
    data_environment1 = csv_data[year]
    data_environment2 = csv_data['colors']
    print(data_environment)

    top = []
    data_temp = csv_data.sort([year],ascending=False)
    data_temp = data_temp.head(10)
    for index, row in data_temp.iterrows():
        if (pandas.isnull(row[year])):
            top.append([row[0], 0])
        else:
            top.append([row[0], row[year]])
    return render_template('home.html', data1=data_environment1, data2=data_environment2, year=year, proj=proj, top=top)


@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])
@app.route('/home', methods=['POST'])
def home_form_post():
    filename = os.path.join(APP_DATA,'narodziny.csv')
    csv_data = pandas.read_csv('data/narodziny.csv', delimiter=',', index_col='Country Code')
    year = request.form['year']
    proj = request.form['projSel']
    csv_data = csv_data.round(2)
    data_environment = csv_data[year]
    colors = []
    for row in data_environment:
        if row > 54:
            colors.append('A')
        elif row > 48:
            colors.append('B')
        elif row > 42:
            colors.append('C')
        elif row > 36:
            colors.append('D')
        elif row > 30:
            colors.append('E')
        elif row > 24:
            colors.append('F')
        elif row > 18:
            colors.append('G')
        elif row > 12:
            colors.append('H')
        elif row > 6:
            colors.append('I')
        elif row > 0:
            colors.append('J')
        else:
            colors.append('Failed')
    csv_data['colors'] = colors
    data_environment1 = csv_data[year]
    data_environment2 = csv_data['colors']
    print(data_environment)

    top = []
    data_temp = csv_data.sort([year], ascending=False)
    data_temp = data_temp.head(10)
    for index, row in data_temp.iterrows():
        if (pandas.isnull(row[year])):
            top.append([row[0], 0])
        else:
            top.append([row[0], row[year]])

    return render_template('home.html', data1=data_environment1, data2=data_environment2, year=year, proj=proj, top=top)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)