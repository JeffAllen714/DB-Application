from sqlalchemy import func
from models.schemas import Warehouse
from core import ma, db

def get_warehouses():
    all_warehouses = Warehouse.query.all()
    return warehouses_schema.dump(all_warehouses)

def add_warehouse(location):
    w = Warehouse(Location=location)
    db.session.add(w)
    db.session.commit()

def delete_warehouse(id):
    data = Warehouse.query.get(id)
    db.session.delete(data)
    db.session.commit()

class WarehouseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Warehouse

warehouse_schema = WarehouseSchema()
warehouses_schema = WarehouseSchema(many=True)
