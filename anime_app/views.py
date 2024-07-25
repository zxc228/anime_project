from flask import render_template, abort
from . import app
from .models import Animes
import random

@app.route('/')
def index():
    quantity = Animes.query.count()
    if not quantity:
        abort(404)
    offset_value = random.randrange(quantity)
    anime = Animes.query.offset(offset_value).first()
    return render_template('anime.html', anime=anime, total_anime_count=quantity)