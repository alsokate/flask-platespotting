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
    results = Code.query.whoosh_search(query).all()
    return render_template('country_page.html',
        query = query,
        results = results)