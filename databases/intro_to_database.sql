CREATE TABLE Students_new (
    Student_ID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    EnrollmentDate DATE
);

-- # CREATE USING INSERT
INSERT INTO Students (
    Student_ID, FirstName, LastName, Email, EnrollmentDate
)
VALUES (
    1, "Godwin", "Boakye", "ohenebayb@gmail.com", "2022-01-01"
);

-- # READING FROM TABLES USING SELECT
SELECT FirstName, LastName FROM Students WHERE EnrollmentDate > "2022-01-02";


-- # MODIFYING EXISTING RECORDS IN A DATABASE USING UPDATE
UPDATE Students SET Email = "ohenebaindustries@gmail.com" WHERE Student_ID = 1;

-- -- # REMOVING ONE OR MORE RECORDS USING DELETE
-- DELETE FROM Students WHERE Student_ID = 1;

-- -- #DATA QUERY LANGUAGE
-- -- SELECT
-- SELECT FirstName, LastName, Email
-- FROM Students
-- WHERE EnrollmentDate >= '2022-01-01'
-- ORDER BY LastName ASC;

-- SELECT Customers.Name, Orders.OrderDate FROM Customers JOIN Orders ON Customers.CustomerID = Orders.CustomerID;

-- -- SORTING TABLE USING ORDER BY
-- SELECT * FROM Students ORDER BY Price ASC;


