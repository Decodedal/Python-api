from flask import Blueprint , request
from . import models

bp  = Blueprint('snake', __name__ , url_prefix="/reptiles")

# @bp.route('/new')
# def new():
#     return "This page submits new snake"

@bp.route('/', methods=["GET", 'POST'])
def index():
    if request.method == "POST":
        common_name = request.form["common_name"]
        scientific_name = request.form['scientific_name']
        conservation_status = request.form['conservation_status']
        native_habitiat = request.form["native_habitiat"]
        fun_fact = request.form['fun_fact']

        new_reptile = models.Reptiles(common_name = common_name, scientific_name = scientific_name, conservation_status = conservation_status, native_habitiat = native_habitiat, fun_fact = fun_fact)

        models.db.session.add(new_reptile)
        models.db.session.commit()
        print(new_reptile)

        return "successfully added reptile"

    results = models.Reptiles.query.all()

    return results


@bp.route('/<id>')
def show(id):
    return f"This is a page for a single snake at id: {id}"

