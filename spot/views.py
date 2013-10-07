import json
from flask import render_template, redirect, url_for, g
from spot import plate, db
from forms import SearchForm, IndexForm
import sqlite3
import os
db_path = os.path.abspath('app.db')

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
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    get_id = c.execute("SELECT country_id FROM code WHERE scramble = '%s'" % c_code)
    c_id = get_id.fetchone()
    get_country_info = c.execute("SELECT * from country where id = '%s'" % c_id)
    c_info = get_country_info.fetchone()
    name = c_info[1]
    mission = c_info[2]
    website = c_info[3]

    return [name, mission, website]




