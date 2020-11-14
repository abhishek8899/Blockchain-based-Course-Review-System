from flask import Flask

# app = Flask(__name__)

# from app import views

def create_app():
    app = Flask(__name__)
    from app import views