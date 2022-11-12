from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import app
from models import News
from models import News_detailed
from models import Products
from models import CardExtensions
from extensions import *

admin = Admin(app)



admin.add_view(ModelView(News,db.session))
admin.add_view(ModelView(News_detailed,db.session))
admin.add_view(ModelView(Products,db.session))
admin.add_view(ModelView(CardExtensions,db.session))
