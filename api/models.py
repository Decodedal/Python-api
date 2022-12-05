from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reptiles(db.Model):
    __tablename__ = "reptiles"

    id = db.Column(db.Integer, primary_key = True)
    common_name = db.Column(db.String)
    scientific_name = db.Column(db.String)
    conservation_status = db.Column(db.String)
    native_habitiat = db.Column(db.String)
    fun_fact = db.Column(db.String) 

