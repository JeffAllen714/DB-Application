from sqlalchemy import func
from models.schemas import CartGroup
from core import ma, db

def get_cart_groups():
    all_cart_groups = CartGroup.query.all()
    return cart_groups_schema.dump(all_cart_groups)

def add_cart_group(user_id_session_id):
    cg = CartGroup(UserID_SessionID=user_id_session_id)
    db.session.add(cg)
    db.session.commit()

def delete_cart_group(id):
    data = CartGroup.query.get(id)
    db.session.delete(data)
    db.session.commit()

class CartGroupSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CartGroup

cart_group_schema = CartGroupSchema()
cart_groups_schema = CartGroupSchema(many=True)
