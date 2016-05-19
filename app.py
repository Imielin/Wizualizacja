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
    filename = os.path.join(APP_DATA,'API_EN.ATM.CO2E.KT_DS2_en_csv_v2.csv')
    csv_data = pandas.read_csv('data\API_EN.ATM.CO2E.KT_DS2_en_csv_v2.csv', delimiter=',', index_col='Country Code')
    year = '1970'
    csv_data = csv_data.round(2)
    data_environment = csv_data[year]
    colors = []
    for row in data_environment:
        if row > 2500000:
            colors.append('A')
        elif row > 1000000:
            colors.append('B')
        elif row > 500000:
            colors.append('C')
        elif row > 100000:
            colors.append('D')
        elif row > 50000:
            colors.append('E')
        elif row > 10000:
            colors.append('F')
        elif row > 1000:
            colors.append('G')
        elif row > 500:
            colors.append('H')
        elif row > 100:
            colors.append('I')
        elif row > 0:
            colors.append('J')
        else:
            colors.append('Failed')
    csv_data['colors'] = colors
    data_environment1 = csv_data[year]
    data_environment2 = csv_data['colors']
    print(data_environment)
    return render_template('home.html', data1=data_environment1, data2=data_environment2, year=year)

@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])
@app.route('/home', methods=['POST'])
def home_form_post():
    filename = os.path.join(APP_DATA,'API_EN.ATM.CO2E.KT_DS2_en_csv_v2.csv')
    csv_data = pandas.read_csv('data\API_EN.ATM.CO2E.KT_DS2_en_csv_v2.csv', delimiter=',', index_col='Country Code')
    year = request.form['year']
    csv_data = csv_data.round(2)
    data_environment = csv_data[year]
    colors = []
    for row in data_environment:
        if row > 2500000:
            colors.append('A')
        elif row > 1000000:
            colors.append('B')
        elif row > 500000:
            colors.append('C')
        elif row > 100000:
            colors.append('D')
        elif row > 50000:
            colors.append('E')
        elif row > 10000:
            colors.append('F')
        elif row > 1000:
            colors.append('G')
        elif row > 500:
            colors.append('H')
        elif row > 100:
            colors.append('I')
        elif row > 0:
            colors.append('J')
        else:
            colors.append('Failed')
    csv_data['colors'] = colors
    data_environment1 = csv_data[year]
    data_environment2 = csv_data['colors']
    print(data_environment)
    return render_template('home.html', data1=data_environment1, data2=data_environment2, year=year)

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
