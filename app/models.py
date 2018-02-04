from app import db_instance, login_manager_instance
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager_instance
from hashlib import md5

class User(UserMixin, db_instance.Model):
    id = db_instance.Column(db_instance.Integer, primary_key = True)
    username = db_instance.Column(db_instance.String(64), index=True, unique=True)
    email = db_instance.Column(db_instance.String(120), index=True, unique=True)
    password_hash = db_instance.Column(db_instance.String(128))
    posts = db_instance.relationship("Post", backref="author", lazy="dynamic")

    about_me = db_instance.Column(db_instance.String(180))
    last_seen = db_instance.Column(db_instance.DateTime, default= datetime.utcnow)

    phone_number = db_instance.Column(db_instance.String)
    state = db_instance.Column(db_instance.String)
    district = db_instance.Column(db_instance.String)
    city = db_instance.Column(db_instance.String)
    address = db_instance.Column(db_instance.String)
    kisan_id = db_instance.Column(db_instance.String)



    def __repr__(self):                             # this method tells Python how to print objects of this class, which is going to be useful for debugging. 
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password_hash =  generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self,size):
        digest = md5(self.email.lower().encode("utf-8")).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)


class Post(db_instance.Model):
    id = db_instance.Column(db_instance.Integer, primary_key=True)
    body = db_instance.Column(db_instance.String(180))
    timestamp = db_instance.Column(db_instance.DateTime, index=True, default=datetime.utcnow)
    user_id = db_instance.Column(db_instance.Integer, db_instance.ForeignKey("user.id"))

    def __repr__(self):
        return "<Post {}".format(self.body)

@login_manager_instance.user_loader
def load_user(id):
    return User.query.get(int (id))

class Product(db_instance.Model):
    id = db_instance.Column(db_instance.Integer, primary_key=True, autoincrement=True)
    name = db_instance.Column(db_instance.String)
    category = db_instance.Column(db_instance.String)
    mrp = db_instance.Column(db_instance.Integer)
    offer_price = db_instance.Column(db_instance.Integer)
    cod_eligible = db_instance.Column(db_instance.Integer) # 0/1
    seller_id = db_instance.Column(db_instance.String)
    details = db_instance.Column(db_instance.String)
    delivery_cost = db_instance.Column(db_instance.Integer)
    returnable = db_instance.Column(db_instance.Integer)
    availability = db_instance.Column(db_instance.Integer) # num of units 
    rating = db_instance.Column(db_instance.Integer)
    imagepath = db_instance.Column(db_instance.String)

    def __repr__(self):                             # this method tells Python how to print objects of this class, which is going to be useful for debugging. 
        return "<Product {} , {},  {}>".format(self.id,self.name, self.mrp)

class Contact(db_instance.Model):
    phone_number = db_instance.Column(db_instance.String)
    email = db_instance.Column(db_instance.String)
    message = db_instance.Column(db_instance.String)
    name = db_instance.Column(db_instance.String)
    id = db_instance.Column(db_instance.Integer, primary_key=True, autoincrement=True)





