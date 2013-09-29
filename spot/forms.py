from flask.ext.wtf import Form
from wtforms import TextField

class IndexForm(Form):
    search = TextField('search')

    
class SearchForm(Form):
    search = TextField('search')