from sqlalchemy import func
from models.schemas import ShoppingCart
from core import ma, db

def get_shopping_carts():
    shopping_carts = ShoppingCart.query.all()
    return shopping_carts

def add_shopping_cart(customer_id, order_id, product_id, cart_group_id):
    new_shopping_cart = ShoppingCart(CustomerID=customer_id, OrderID=order_id,
                                     ProductID=product_id, CartGroupID=cart_group_id)
    db.session.add(new_shopping_cart)
    db.session.commit()

def delete_shopping_cart(id):
    shopping_cart = ShoppingCart.query.get(id)
    db.session.delete(shopping_cart)
    db.session.commit()

class ShoppingCartSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ShoppingCart

shopping_cart_schema = ShoppingCartSchema()
shopping_carts_schema = ShoppingCartSchema(many=True)
