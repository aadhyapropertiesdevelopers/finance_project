from app.models.payment_type import PaymentType
from app import db

def add_payment_type(payment_type_data):
    payment_type = PaymentType(
        type_name=payment_type_data["type_name"],
        status=payment_type_data["status"]
    )
    db.session.add(payment_type)
    db.session.commit()
    return payment_type

def get_all_payment_types():
    payment_types = PaymentType.query.all()
    return [ptype.to_dict() for ptype in payment_types]

def get_payment_type_by_id(payment_type_id):
    payment_type = PaymentType.query.get(payment_type_id)
    return payment_type.to_dict() if payment_type else None

def update_payment_type(payment_type_id, updated_data):
    payment_type = PaymentType.query.get(payment_type_id)
    if payment_type:
        payment_type.type_name = updated_data.get("type_name", payment_type.type_name)
        payment_type.status = updated_data.get("status", payment_type.status)
        db.session.commit()
        return payment_type.to_dict()
    return None

def delete_payment_type(payment_type_id):
    payment_type = PaymentType.query.get(payment_type_id)
    if payment_type:
        db.session.delete(payment_type)
        db.session.commit()
        return True
    return False
