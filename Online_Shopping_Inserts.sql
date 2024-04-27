-- Insert into PaymentDetails
INSERT INTO PaymentDetails (CardNumber, ExpiryDate, CVC, CardHolderName)
VALUES ('1234567890123456', '2025-12-31', 123, 'John Doe');

-- Insert into Review
INSERT INTO Review (Ratings, Comments, ProductID, CustomerID)
VALUES (5, 'Great product!', 1, 1);

-- Insert into Warehouse
INSERT INTO Warehouse (Location, MaxCapacity)
VALUES ('Main Warehouse', 1000);

-- Insert into OrderDetails
INSERT INTO OrderDetails (OrderID, ProductID, Quantity, Subtotal)
VALUES (1, 1, 2, 30.00);
