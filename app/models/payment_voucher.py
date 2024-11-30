class PaymentVoucher:
    def __init__(self, voucher_id, name, amount, payment_note, payment_receipt, date, status):
        self.voucher_id = voucher_id
        self.name = name
        self.amount = amount
        self.payment_note = payment_note
        self.payment_receipt = payment_receipt
        self.date = date
        self.status = status

    def to_dict(self):
        return {
            "voucher_id": self.voucher_id,
            "name": self.name,
            "amount": self.amount,
            "payment_note": self.payment_note,
            "payment_receipt": self.payment_receipt,
            "date": self.date,
            "status": self.status
        }
