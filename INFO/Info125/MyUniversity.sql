-- NOTE --
-- You must create the tables in the correct order.
-- Foreign keys can become problems if you do not do this.

-- CREATE TABLE Statements --

CREATE TABLE STUDENT(
StudentId INTEGER PRIMARY KEY,
Sname VARCHAR(30),
PhoneNr INTEGER,
Programme VARCHAR(50)
);

CREATE TABLE COURSE(
Course_code VARCHAR(10) PRIMARY KEY,
Course_name VARCHAR(35),
Main_lecturer VARCHAR(30),
Credit_points DECIMAL(2,0),
Institute VARCHAR(25)
);

CREATE TABLE GRADE(
Course_code VARCHAR(10),
StudentId INTEGER,
Grade CHAR(1),
PRIMARY KEY(Course_code, StudentId),
FOREIGN KEY(Course_code) REFERENCES COURSE(Course_code),
FOREIGN KEY(StudentId) REFERENCES STUDENT(StudentId)
);

CREATE TABLE ORG (
    OrgName VARCHAR(35) PRIMARY KEY,
    Address VARCHAR(50),
    Website VARCHAR(35)
);

CREATE TABLE SCHOLARSHIP(
StudentId INTEGER,
Scholarship_type VARCHAR(25),
Date_granted DATE,
Amount DECIMAL(7),
Organization_name VARCHAR(35),
PRIMARY KEY(StudentId, Scholarship_type, Date_granted, Organization_name),
FOREIGN KEY(StudentId) REFERENCES STUDENT(StudentId),
FOREIGN KEY(Organization_name) REFERENCES ORG(OrgName)
);



-- INSERT statements --

-- STUDENT INSERTS --
INSERT INTO STUDENT(StudentId, Sname, PhoneNr, Programme) VALUES (123, 'Ole Bull', 61123231, 'Bachelor of Music');
INSERT INTO STUDENT VALUES (456, 'Henrik Wergeland', 69355122, 'Bachelor of Norwegian Literature');
INSERT INTO STUDENT VALUES (789, 'Ivar Aasen', 61231234, 'Bachelor of Norwegian Literature');
INSERT INTO STUDENT VALUES (666, 'Neil Hansson', 12341234, 'Bachelor of Drama');
INSERT INTO STUDENT VALUES (111, 'Patrick Llory', 43214321, 'Bachelor of Computer Science');
INSERT INTO STUDENT VALUES (421, 'Harris Goldfever', 22225555, 'Bachelor of Mathematics');

-- COURSE INSERTS --
INSERT INTO COURSE VALUES ('INFO125', 'Data Management', 'Carsten Helgesen', 10, 'InfoMedia');
INSERT INTO COURSE VALUES ('MATH100', 'Intorduction to mathematics', 'Alan Turing', 15, 'Mathematical');
INSERT INTO COURSE VALUES ('MUSC331', 'Advanced Music Theory', 'Hans Zimmerman', 10, 'Music and Drama');
INSERT INTO COURSE VALUES ('LING201', 'Advanced Linguistics', 'Knut Hamsun', 15, 'Humanities');

-- GRADE INSERTS --
INSERT INTO GRADE VALUES('INFO125', 111, 'B');
INSERT INTO GRADE VALUES('MATH100', 421, 'C');
INSERT INTO GRADE VALUES('MUSC331', 123, 'A');
INSERT INTO GRADE VALUES('MUSC331', 666, 'B');

-- ORGANIZATION INSERTS --
INSERT INTO ORG VALUES('Uncle Sam', '1600 Pennsylvania Ave NW, Washington, DC 20500', 'www.us.gov');
INSERT INTO ORG VALUES('PETA', '501 Front St. Norfolk, VA 23510', 'www.peta.org');
INSERT INTO ORG VALUES('Stark Industries', 'Imagination Street 1, New York, NY 10118', 'www.starkindustries.gov');
INSERT INTO ORG VALUES('Jehovah''s Witnesses' , '3701 SW 12th St, Topeka, KS 66604', 'www.jw.org');

-- SCHOARSHIP INSERTS --
INSERT INTO SCHOLARSHIP VALUES (666, 'Athletic', '2016-11-24', 30000, 'Uncle Sam');
INSERT INTO SCHOLARSHIP VALUES (421, 'Merit', '2015-08-08', 45000, 'PETA');
INSERT INTO SCHOLARSHIP VALUES (456, 'School-based', '2013-11-24', 15000, 'Stark Industries');
INSERT INTO SCHOLARSHIP VALUES (123, 'Need-based', '2015-01-04', 20000, 'Jehovah''s Witnesses');

-- ALTER statements --
ALTER TABLE STUDENT ADD CONSTRAINT check_phnr CHECK (LENGTH(phonenr) = 8);
ALTER TABLE ORG ADD CONSTRAINT unique_url UNIQUE (website);




-- QUERY 1 --
SELECT 
    grade
FROM
    GRADE,
    STUDENT
WHERE
    STUDENT.studentid = GRADE.STUDENTID
        AND STUDENT.SNAME = 'Patrick Llory';



-- QUERY 2 --
SELECT 
    grade
FROM
    GRADE
        NATURAL JOIN
    STUDENT
WHERE
    sname = 'Patrick Llory';



-- QUERY 3 --
SELECT 
    grade
FROM
    GRADE
        INNER JOIN
    STUDENT ON STUDENT.studentid = GRADE.studentid
WHERE
    sname = 'Patrick Llory';



-- QUERY 4 --
SELECT 
    grade
FROM
    GRADE
WHERE
    studentid IN (SELECT 
            studentid
        FROM
            STUDENT
        WHERE
            sname = 'Patrick Llory');



-- QUERY 6 --
SELECT 
    sname
FROM
    student
        NATURAL JOIN
    scholarship
WHERE
    amount IN (SELECT 
            MAX(amount)
        FROM
            scholarship);



-- QUERY 7 --
SELECT 
    SUM(amount), scholarship.organization_name
FROM
    scholarship
GROUP BY scholarship.organization_name
ORDER BY SUM(amount) DESC;
  


-- Query 8 --
SELECT 
    STUDENT.studentid
FROM
    STUDENT
        LEFT JOIN
    SCHOLARSHIP ON SCHOLARSHIP.studentid = STUDENT.studentid
WHERE
    SCHOLARSHIP.studentid IS NULL;
 
 
 
-- Query 9 --
CREATE VIEW amount (am) AS
    SELECT 
        amount
    FROM
        scholarship;
 
 
 
-- Query 10 --
CREATE VIEW STUDGRADE (studentid , num_of_grades) AS
    SELECT 
        studentid, COUNT(grade)
    FROM
        GRADE
    GROUP BY studentid;