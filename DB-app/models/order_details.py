from sqlalchemy import func
from models.schemas import OrderDetails
from core import ma, db

def get_order_details():
    all_order_details = OrderDetails.query.all()
    return order_details_schema.dump(all_order_details)

def add_order_details(order_id, product_id, quantity, subtotal):
    od = OrderDetails(OrderID=order_id, ProductID=product_id, Quantity=quantity, Subtotal=subtotal)
    db.session.add(od)
    db.session.commit()

def delete_order_details(id):
    data = OrderDetails.query.get(id)
    db.session.delete(data)
    db.session.commit()

class OrderDetailsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OrderDetails

order_details_schema = OrderDetailsSchema()
order_details_schema = OrderDetailsSchema(many=True)
