# # /app/models.py
# from .. import db
# class User(db.Model):
#     __tablename__ = 'user'  # Explicitly set the table name
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), nullable=False, unique=True)

#     def __repr__(self):
#         return f'<User {self.name}>'




# /app/models.py


from .. import db

class User(db.Model):
    __tablename__ = 'user'  # Explicitly set the table name
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    

    def __repr__(self):
        return f'<User {self.username}>'


