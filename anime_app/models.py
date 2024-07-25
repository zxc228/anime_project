from . import db

class Animes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_ru = db.Column(db.String(256), nullable=False)
    name_en = db.Column(db.String(256), nullable=False)
    link = db.Column(db.String(256), nullable=False)
    rating = db.Column(db.Float)
    description = db.Column(db.String)
    img_link = db.Column(db.String(256))

   