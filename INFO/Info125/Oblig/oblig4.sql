-- Question 2 a)
CREATE TABLE Can_land (
    Airport_code CHAR(3),
    Airplane_type_name VARCHAR(13) PRIMARY KEY (Airplane_type_name, AIRPLANE_TYPE),
    FOREIGN KEY (Airport_code) REFERENCES AIRPORT(Airport_code),
    FOREIGN KEY (Airplane_type_name) REFERENCES AIRPLANE_TYPE(Airplane_type_name)
)

-- Question 2 b)
SELECT City 
FROM AIRPORT, CAN_LAND
WHERE AIRPORT.Airport_code = CAN_LAND.Airport_code AND Airport_type_name = 'Boing747';  

-- Question 3 a)
SELECT Loc_Code, Address, City, State, Country_Name
FROM DEPT_LOCATION, COUNTRY

-- Question 3 b)
SELECT Job_ID, COUNT(*)
FROM WORKER
GROUP BY Job_ID

-- Question 3 c)
SELECT MAX(Salary)
FROM WORKER
WHERE WORKER.Job_ID = 'IT_PROG'