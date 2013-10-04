import json
from flask import render_template, flash, redirect, session, url_for, request, g
from spot import plate, db
from forms import SearchForm, IndexForm
from models import Code

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
    country = query[1:3]
    search = Code.query.whoosh_search(country).all()

    if plate_type_index in plate_type_options:
        plate_type = plate_type_options[plate_type_index]

    if search:
        results = search[0].country.country_name
        flag_image = results.replace(' ', '-')
        location = search[0].country.mission
        website = search[0].country.website

    map_data = [results, location, website]

    return render_template('country_page.html',
        query = query,
        results = results,
        location = location,
        plate_type = plate_type,
        flag_image = flag_image,
        data = json.dumps(map_data))




