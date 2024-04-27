from sqlalchemy import func
from models.schemas import Review
from core import ma, db

def get_reviews():
    reviews = Review.query.all()
    return reviews

def add_review(ratings, comments, product_id, customer_id):
    new_review = Review(Ratings=ratings, Comments=comments, ProductID=product_id, CustomerID=customer_id)
    db.session.add(new_review)
    db.session.commit()

def delete_review(id):
    review = Review.query.get(id)
    db.session.delete(review)
    db.session.commit()

class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Review

review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)
