from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager





class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email_address= db.Column(db.String(255),unique = True,index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    fullname=db.Column(db.String(255))
    mobile_phone=db.Column(db.Integer())
    office_phone=db.Column(db.Integer())
    password_secure = db.Column(db.String(255))
    book = db.relationship('Book', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref = 'user', lazy = 'dynamic')
    upvotes = db.relationship('Upvote', backref = 'user', lazy = 'dynamic')
    

    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

    def __repr__(self):
        return f'User {self.username}'



class Book(db.Model):
    '''
    '''
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)  
    title = db.Column(db.String())
    summary = db.Column(db.String(), index = True)
    category = db.Column(db.String(255), nullable=False)
    poster = db.Column(db.String())
    location =db.Column(db.String())
    comments = db.relationship('Comment',backref='book',lazy='dynamic')
    upvotes = db.relationship('Upvote', backref = 'book', lazy = 'dynamic')
    
   

    
    @classmethod
    def get_books(cls, id):
        books = Pitch.query.order_by(pitch_id=id).desc().all()
        return books

    def __repr__(self):
        return f'Pitch {self.description}'

    

class Comment(db.Model):
    __tablename__='comments'
    
    id = db.Column(db.Integer,primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)
    description = db.Column(db.Text)

    
    def __repr__(self):
        return f"Comment : id: {self.id} comment: {self.description}"


class Upvote(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key=True)
    upvote = db.Column(db.Integer,default=1)
    book_id = db.Column(db.Integer,db.ForeignKey('book.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_upvotes(self):
        db.session.add(self)
        db.session.commit()


    def add_upvotes(cls,id):
        upvote_book = Upvote(user = current_user, book_id=id)
        upvote_book.save_upvotes()

    
    @classmethod
    def get_upvotes(cls,id):
        upvote = Upvote.query.filter_by(book_id=id).all()
        return upvote

    @classmethod
    def get_all_upvotes(cls,book_id):
        upvotes = Upvote.query.order_by('id').all()
        return upvotes

    def __repr__(self):
        return f'{self.user_id}:{self.book_id}'



