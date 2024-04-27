from sqlalchemy import func
from models.schemas import Product
from core import ma, db

def get_products():
    products = Product.query.all()
    return products

def add_product(name, description, price, category, photo, warehouse_id, stock_quantity):
    new_product = Product(Name=name, Description=description, Price=price, Category=category,
                          Photo=photo, WarehouseID=warehouse_id, StockQuantity=stock_quantity)
    db.session.add(new_product)
    print(new_product)
    db.session.commit()


def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

