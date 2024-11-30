from models.payment_voucher import PaymentVoucher

# Mock database
payment_vouchers = []

def add_payment_voucher(voucher_data):
    voucher = PaymentVoucher(**voucher_data)
    payment_vouchers.append(voucher)
    return voucher

def get_all_payment_vouchers():
    return [voucher.to_dict() for voucher in payment_vouchers]

def get_payment_voucher_by_id(voucher_id):
    for voucher in payment_vouchers:
        if voucher.voucher_id == voucher_id:
            return voucher.to_dict()
    return None

def update_payment_voucher(voucher_id, updated_data):
    for voucher in payment_vouchers:
        if voucher.voucher_id == voucher_id:
            voucher.name = updated_data.get("name", voucher.name)
            voucher.amount = updated_data.get("amount", voucher.amount)
            voucher.payment_note = updated_data.get("payment_note", voucher.payment_note)
            voucher.payment_receipt = updated_data.get("payment_receipt", voucher.payment_receipt)
            voucher.date = updated_data.get("date", voucher.date)
            voucher.status = updated_data.get("status", voucher.status)
            return voucher.to_dict()
    return None

def delete_payment_voucher(voucher_id):
    global payment_vouchers
    payment_vouchers = [v for v in payment_vouchers if v.voucher_id != voucher_id]
    return True
