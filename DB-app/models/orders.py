from sqlalchemy import func
from sqlalchemy.orm import relationship
from models.schemas import Orders
from core import ma, db

def get_orders():
    orders = Orders.query.all()
    return orders

def add_order(date, total_amount, status, customer_id):
    new_order = Orders(Date=date, TotalAmount=total_amount, Status=status, CustomerID=customer_id)
    db.session.add(new_order)
    db.session.commit()

def delete_order(id):
    order = Orders.query.get(id)
    db.session.delete(order)
    db.session.commit()

class OrdersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Orders

    order_details = relationship("OrderDetails", backref="order", foreign_keys="OrderDetails.OrderID")

order_schema = OrdersSchema()
orders_schema = OrdersSchema(many=True)
