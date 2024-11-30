from app import db

class PaymentType(db.Model):
    __tablename__ = 'payment_types'

    payment_type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_name = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            "payment_type_id": self.payment_type_id,
            "type_name": self.type_name,
            "status": self.status
        }
