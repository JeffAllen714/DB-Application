-- Initialize the OnlineShopping Database
CREATE DATABASE IF NOT EXISTS Online_Shopping;
USE Online_Shopping;

-- Create Warehouse Table
CREATE TABLE Warehouse (
    WarehouseID INT PRIMARY KEY AUTO_INCREMENT,
    Location VARCHAR(255)
	-- MaxCapacity INT,
);

-- Create PaymentDetails Table
CREATE TABLE PaymentDetails (
    PaymentID INT PRIMARY KEY AUTO_INCREMENT,
    CardNumber VARCHAR(16) NOT NULL,
    ExpiryDate DATE NOT NULL,
    CVC INT NOT NULL,
    CardHolderName VARCHAR(100) NOT NULL
);

-- Product Table
CREATE TABLE Product (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    Category VARCHAR(50),
    Photo VARCHAR(255),
    WarehouseID INT,
    StockQuantity INT,
    FOREIGN KEY (WarehouseID) REFERENCES Warehouse(WarehouseID)
);

-- Customer Table
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Address TEXT,
    PaymentID INT,
    Rewards INT,
    CartID INT,
    FOREIGN KEY (CartID) REFERENCES ShoppingCart(CartID),
    FOREIGN KEY (PaymentID) REFERENCES PaymentDetails(PaymentID)
);

-- ShoppingCart Table
CREATE TABLE ShoppingCart (
    CartID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT,
    OrderID INT,
    ProductID INT,
    CartGroupID INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
    FOREIGN KEY (CartGroupID) REFERENCES CartGroup(CartGroupID)
);

-- Review Table
CREATE TABLE Review (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,
    Ratings INT,
    Comments TEXT,
    ProductID INT,
    CustomerID INT,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

-- Orders Table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    Date DATE,
    TotalAmount DECIMAL(10, 2) NOT NULL,
    Status VARCHAR(50),
    CustomerID INT,
    OrderDetailID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (OrderDetailID) REFERENCES OrderDetails(OrderID)
    -- Payment attrbute? links to PaymentDetail in purchase details table
);

-- OrderDetails Table
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    Subtotal DECIMAL(10, 2),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

-- CartGroup Table
CREATE TABLE CartGroup (
    CartGroupID INT PRIMARY KEY AUTO_INCREMENT,
    UserID_SessionID INT,
    FOREIGN KEY (UserID_SessionID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (CartGroupID) REFERENCES ShoppingCart(CartGroupID)
);

-- Referential Actions for Orders Table
ALTER TABLE Orders
ADD CONSTRAINT fk_orders_customer
FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
ON DELETE CASCADE;

-- Referential Actions for ShoppingCart Table
ALTER TABLE ShoppingCart
ADD CONSTRAINT fk_shoppingcart_order
FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
ON DELETE CASCADE;

ALTER TABLE ShoppingCart
ADD CONSTRAINT fk_shoppingcart_product
FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
ON DELETE CASCADE;

-- Referential Actions for Customer Table
ALTER TABLE Customer
ADD CONSTRAINT fk_customer_payment
FOREIGN KEY (PaymentID) REFERENCES PaymentDetails(PaymentID)
ON DELETE SET NULL;

-- SHOW TABLES;

-- SELECT * FROM PaymentDetails
