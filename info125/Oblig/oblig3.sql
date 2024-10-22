-- Oppgave 2 a)
SELECT * 
FROM Hotel 
WHERE hotelCity = 'New Yorkl'
ORDER BY numRoom DESC;

-- Oppgave 2 b)
SELECT * 
FROM Guest 
WHERE firstName = 'Sara'
ORDER BY guestAddress ASC;

-- Oppgave 3
-- Create the Art_Gallery database
CREATE DATABASE Art_Gallery;

-- Use the Art_Gallery database
USE Art_Gallery;

-- Create Art table
CREATE TABLE Art (
    Art_id INT PRIMARY KEY,
    Style VARCHAR(50),
    Location VARCHAR(50),
    Publisher VARCHAR(50)
);

-- Create the Artist table
CREATE TABLE Artist (
    Artist_name VARCHAR(100) PRIMARY KEY,
    Art_id INT,
    FOREIGN KEY (Art_id) REFERENCES Art(Art_id)
);


-- Create Art_Publisher table
CREATE TABLE Art_Publisher (
    name VARCHAR(50) PRIMARY KEY,
    Address VARCHAR(100) NOT NULL,
    Telephone VARCHAR(8) NOT NULL
);

-- Create the Order table
CREATE TABLE Order_table (
    Order_id INT PRIMARY KEY,
    Date DATE,
    Price INT,
    Art_id INT,
    FOREIGN KEY (Art_id) REFERENCES Art(Art_id)
);