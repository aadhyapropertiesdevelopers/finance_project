# /app/models.py
from .. import db
class payment_types_model(db.Model):
    __tablename__ = 'user'  # Explicitly set the table name
    id = db.Column(db.Integer, primary_key=True)
    payment_type_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.integer, nullable=False)
    def __repr__(self):
        return f'<User {self.name}>'
