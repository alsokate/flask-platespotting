import json
from flask import render_template, redirect, url_for, g
from spot import plate, db
from forms import SearchForm, IndexForm
import psycopg2
import sys

@plate.before_request
def before_request():
    g.search_form = SearchForm()


@plate.route('/', methods = ['GET', 'POST'])
@plate.route('/index', methods = ['GET', 'POST'])
def index():
    form = IndexForm()
    if form.validate_on_submit():
        return redirect(url_for('search_results', query = g.search_form.search.data))
    return render_template('index.html', form=form)


@plate.route('/search', methods = ['POST'])
def search():
    return redirect(url_for('search_results', query = g.search_form.search.data))


@plate.route('/search_results/<query>')
def search_results(query):
    plate_type = ''
    flag_image = ''
    results = ''
    location = ''
    website = ''
    plate_type_options = {'D': 'Diplomat', 'C': 'Foreign Consul', 'S': 'Non-diplomatic Staff'}
    plate_type_index = query[0].upper()
    country_code = query[1:3]
    search = code_search(country_code)


    if plate_type_index in plate_type_options:
        plate_type = plate_type_options[plate_type_index]

    if search:
        results = search[0]
        flag_image = results.replace(' ', '-')
        location = search[1]
        website = search[2]

    map_data = [results, location, website]
    return render_template('country_page.html',
        query = query,
        results = results,
        location = location,
        plate_type = plate_type,
        flag_image = flag_image,
        data = json.dumps(map_data))

def code_search(c_code):
    connection_settings = "host=localhost dbname=app user=kate password=emotiveowl"
    db = psycopg2.connect(connection_settings)
    c = db.cursor()

    c.execute("""SELECT country_id FROM code WHERE to_tsvector(scramble) @@ to_tsquery('%s');""" % c_code)
    get_id = c.fetchone()[0]
    c.execute("""SELECT * FROM country WHERE to_tsvector(CAST (id as text)) @@ to_tsquery('%s');""" % get_id)
    get_country_data =  c.fetchone()
    name = get_country_data[1]
    mission = get_country_data[2]
    website =  get_country_data[3]

    return [name, mission, website]




