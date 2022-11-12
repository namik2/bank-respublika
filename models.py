
from extensions import db
from app import app

class Products(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable=True)
    description = db.Column(db.String(200),nullable=True)

    def __repr__(self):
        return self.title

    def __init__(self,title, description):
        self.title = title
        self.description =  description


    def save(self):
        db.session.add(self)
        db.session.commit()


class News(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable=True)
    share_time = db.Column(db.String(200),nullable=True)
    photoImage = db.Column(db.String(200),nullable=True)

    def __repr__(self):
       return self.title
    
    def __init__(self,title,share_time, photoImage ):
        self.title = title
        self.share_time = share_time   
        self. photoImage  =  photoImage   


    def save(self):
        db.session.add(self)
        db.session.commit()


class News_detailed(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),nullable=True)
    photoImage = db.Column(db.String(200),nullable=True)
    description = db.Column(db.String(200),nullable=True)


    def __repr__(self):
        return self.title
    

    def __init__(self,title,photoImage,description):
        self.title = title
        self. photoImage  =  photoImage
        self.description = description   



    def save(self):
        db.session.add(self)
        db.session.commit()

class CardExtensions(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    card_number = db.Column(db.Integer,nullable = False)
    pasport_select  = db.Column(db.String(100),nullable = False)
    pasport_number = db.Column(db.Integer,nullable = False)
    order =  db.Column(db.String(100),nullable = False)
    number = db.Column(db.Integer,nullable = False)
    number_select = db.Column(db.String(100),nullable = False)
    filial_select = db.Column(db.String(100),nullable = False)
    
    def __repr__ (self):
        return self.pasport_select
    
    def __init___(self,card_number,pasport_select,pasport_number,order,number,number_select,filial_select):
        self.card_number = card_number
        self.pasport_select = pasport_select
        self.pasport_number = pasport_number
        self.order = order
        self.number = number
        self.number_select = number_select
        self.filial_select = filial_select

    def save(self):
        db.session.add(self)
        db.session.commit()


