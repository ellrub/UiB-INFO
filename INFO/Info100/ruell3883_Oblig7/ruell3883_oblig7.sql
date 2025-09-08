-- Oppagve 1

CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(30),
    ContactName VARCHAR(30),
    Address VARCHAR(30),
    City VARCHAR(30),
    PostalCode INT(5),
    Country VARCHAR(30),
);

INSERT INTO Customer (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES (1, 'Alfreds Futterkiste', 'Maria Anders', 'Ober Str. 57', 'Berlin', 12209, 'Germany');


-- Oppagve 2
-- a)
SELECT CustomerName 
FROM Customers;

-- b)
SELECT CustomerName 
FROM Customers
WHERE City = 'Berlin';

-- c)
SELECT CustomerName 
FROM Customers
WHERE City = 'Berlin' OR City = 'London';

-- d)
SELECT CustomerName 
FROM Customers
WHERE Country <> 'Germany';