from flask_wtf import FlaskForm
from wtforms import IntegerField,RadioField, SelectField,StringField
from wtforms.validators import DataRequired,Length,NumberRange



passport = ["AZE","AA"]

number_code = ["+994 50","+994 51","+994 70","+994 77","+994 55","+994 99"]

filial = ["Filiali sechin","Sheki filiali","İnshaatchilar shobesi","Sumqayit filiali","Tovuz filiali","Gence filiali"]

radio_choice = [('1 gün', '1 gün'),('3 gün', '3 gün')]


class CardExtensionsForm(FlaskForm):    
    card_number =  StringField(label='Kartin son 8 reqemi:', validators=[DataRequired()])
    pasport_select = SelectField(label="",choices=passport)
    pasport_number = StringField(label="Shexsiyyeti tesdiq eden sened:",validators=[DataRequired()])
    order = RadioField(label="Sifarish novu", choices = radio_choice)
    number = StringField(label= "Mobil nomreniz:",validators=[DataRequired()])
    number_select = SelectField(choices=number_code)
    filial_select = SelectField(label="Kart goturulecek fil ial",choices=filial)

