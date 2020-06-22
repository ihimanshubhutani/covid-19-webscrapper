from flask import Flask, render_template, request
from main_file import fetch_covid_details
from countries_name import country_dict

app = Flask(__name__)


@app.route('/')
def show_index_page():
    return render_template('index.html', countries=country_dict.keys())


@app.route('/country')
def fetch_details():
    country_name = request.args.get('country')
    return render_template('details.html', details=fetch_covid_details(country_dict[country_name]))


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
