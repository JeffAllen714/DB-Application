from sqlalchemy import func
from models.schemas import PaymentDetails
from core import ma, db

def get_payment_details():
    all_payment_details = PaymentDetails.query.all()
    return payment_details_schema.dump(all_payment_details)

def add_payment_details(card_number, expiry_date, cvc, card_holder_name):
    pd = PaymentDetails(CardNumber=card_number, ExpiryDate=expiry_date, CVC=cvc, CardHolderName=card_holder_name)
    db.session.add(pd)
    db.session.commit()

def delete_payment_details(id):
    data = PaymentDetails.query.get(id)
    db.session.delete(data)
    db.session.commit()

class PaymentDetailsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PaymentDetails

payment_details_schema = PaymentDetailsSchema()
payment_details_schema = PaymentDetailsSchema(many=True)
