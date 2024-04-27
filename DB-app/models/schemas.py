from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, Float, Numeric
from sqlalchemy.orm import relationship
from core import db

class Warehouse(db.Model):
    __tablename__ = 'Warehouse'
    WarehouseID = Column(Integer, primary_key=True)
    Location = Column(String(255))

class PaymentDetails(db.Model):
    __tablename__ = 'PaymentDetails'
    PaymentID = Column(Integer, primary_key=True)
    CardNumber = Column(String(16), nullable=False)
    ExpiryDate = Column(Date, nullable=False)
    CVC = Column(Integer, nullable=False)
    CardHolderName = Column(String(100), nullable=False)

class Customer(db.Model):
    __tablename__ = 'Customer'
    CustomerID = Column(Integer, primary_key=True)
    Name = Column(String(100), nullable=False)
    Email = Column(String(100), unique=True, nullable=False)
    Password = Column(String(255), nullable=False)
    Address = Column(Text)
    PaymentID = Column(Integer, ForeignKey('PaymentDetails.PaymentID'))
    Rewards = Column(Integer)
    payment_details = relationship("PaymentDetails", backref="customer")

class Product(db.Model):
    __tablename__ = 'Product'
    ProductID = Column(Integer, primary_key=True)
    Name = Column(String(255), nullable=False)
    Description = Column(Text)
    Price = Column(Float, nullable=False)
    Category = Column(String(50))
    Photo = Column(String(255))
    WarehouseID = Column(Integer, ForeignKey('Warehouse.WarehouseID'))
    StockQuantity = Column(Integer)
    warehouse = relationship("Warehouse", backref="products")

class ShoppingCart(db.Model):
    __tablename__ = 'ShoppingCart'
    CartID = Column(Integer, primary_key=True)
    CustomerID = Column(Integer, ForeignKey('Customer.CustomerID'))
    OrderID = Column(Integer, ForeignKey('Orders.OrderID'))
    ProductID = Column(Integer, ForeignKey('Product.ProductID'))
    CartGroupID = Column(Integer, ForeignKey('CartGroup.CartGroupID'))
    order = relationship("Orders", backref="shopping_cart")
    product = relationship("Product", backref="shopping_cart")
    cart_group = relationship("CartGroup", backref="shopping_cart")

class Review(db.Model):
    __tablename__ = 'Review'
    ReviewID = Column(Integer, primary_key=True)
    Ratings = Column(Integer)
    Comments = Column(Text)
    ProductID = Column(Integer, ForeignKey('Product.ProductID'))
    CustomerID = Column(Integer, ForeignKey('Customer.CustomerID'))
    product = relationship("Product", backref="reviews")
    customer = relationship("Customer", backref="reviews")

class Orders(db.Model):
    __tablename__ = 'Orders'
    OrderID = Column(Integer, primary_key=True)
    Date = Column(Date)
    TotalAmount = Column(Numeric(10, 2), nullable=False)
    Status = Column(String(50))
    CustomerID = Column(Integer, ForeignKey('Customer.CustomerID'))
    customer = relationship("Customer", backref="orders")

class OrderDetails(db.Model):
    __tablename__ = 'OrderDetails'
    OrderDetailID = Column(Integer, primary_key=True)
    OrderID = Column(Integer, ForeignKey('Orders.OrderID'))
    ProductID = Column(Integer, ForeignKey('Product.ProductID'))
    Quantity = Column(Integer)
    Subtotal = Column(Numeric(10, 2))
    order = relationship("Orders", backref="order_details")
    product = relationship("Product", backref="order_details")

class CartGroup(db.Model):
    __tablename__ = 'CartGroup'
    CartGroupID = Column(Integer, primary_key=True)
    UserID_SessionID = Column(Integer, ForeignKey('Customer.CustomerID'))
    user = relationship("Customer", backref="cart_groups")
    