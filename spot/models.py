from spot import plate
from spot import db

class Country(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    country_name = db.Column(db.String(64), unique = True)
    codes = db.relationship('Code', backref='country', lazy='dynamic')
    mission = db.Column(db.String(64))
    website = db.Column(db.String(64))

    def __repr__(self):
        return '<%r>' % (self.country_name)

class Code(db.Model):
    __searchable__ = ['scramble']

    id = db.Column(db.Integer, primary_key = True)
    scramble = db.Column(db.String(64), unique = True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))

    def __repr__(self):
        return '<%r>' % (self.scramble)