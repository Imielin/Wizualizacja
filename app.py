from flask import Flask, request, render_template, jsonify
from crawler_main import crawler
from flask_bootstrap import Bootstrap
import pandas as pd
app = Flask(__name__)
Bootstrap(app)



@app.route('/')
def start():
    data = pd.read_csv('pkb.csv', delimiter=',', index_col='Country Code')
    dataf = data['1960']





    return render_template('test.html', data=dataf, year ='1960' )


if __name__ == '__main__':
    app.run(debug=True)
