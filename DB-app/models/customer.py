from sqlalchemy import func
from sqlalchemy.orm import relationship
from models.schemas import Customer
from core import ma, db

def get_customers():
    customers = Customer.query.all()
    return customers

def add_customer(name, email, password, address, payment_id, rewards):
    new_customer = Customer(Name=name, Email=email, Password=password, Address=address,
                            PaymentID=payment_id, Rewards=rewards)
    db.session.add(new_customer)
    db.session.commit()

def delete_customer(id):
    customer = Customer.query.get(id)
    db.session.delete(customer)
    db.session.commit()

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer

    shopping_cart = relationship("ShoppingCart", backref="customer", foreign_keys="ShoppingCart.CustomerID")

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
