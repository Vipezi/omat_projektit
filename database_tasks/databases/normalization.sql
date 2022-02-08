CREATE DATABASE normalization_task;

CREATE TABLE students(
    studentId MEDIUMINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    age TINYINT NOT NULL,
    PRIMARY KEY (studentId)
);

INSERT INTO students(studentId, name, age) VALUES
    ("Shirley Sanders", 19),
    ("Kelly Lorena", 33),
    ("Dale Galloway", 66);

CREATE TABLE courses(
    courseId MEDIUMINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(150) NOT NULL,
    PRIMARY KEY(courseId)
);

INSERT INTO courses(name, description) VALUES
    ("Basics of Computing", "This course will give you basic information of computing"),
    ("UI Design: Advanced", "UI Design advanced course"),
    ("AI Mechanisms in databases", "Common AI mechanisms in databases");

CREATE TABLE studentsincourses(
    studentId MEDIUMINT NOT NULL,
    courseId MEDIUMINT NOT NULL,
    PRIMARY KEY (studentId, courseId),
    FOREIGN KEY (courseId) REFERENCES courses(courseId), 
    FOREIGN KEY (studentId) REFERENCES students(studentId)
);

INSERT INTO studentsincourses(studentId, name) VALUES
(1,1),
(1,2),
(2,2),
(3,3);

CREATE DATABASE normalization_task2;

CREATE TABLE customers(
    customerId MEDIUMINT NOT NULL AUTO_INCREMENT,
    customerName VARCHAR(150) NOT NULL,
    customerPhone VARCHAR(50) NOT NULL,
    customerAddress VARCHAR(100) NOT NULL,
    PRIMARY KEY (customerId)
);

INSERT INTO customers(customerName, customerPhone, customerAddress) VALUES
("Shirley Sanders", "+51241232135",	"Nice Street 12"),
("Kelly Lorena","+445123232", "Amazon blvd 6122"),
("Dale Galloway","+612225123", "Bad Street 61");

CREATE TABLE orders(
    orderId MEDIUMINT NOT NULL AUTO_INCREMENT,
    mealName VARCHAR(50) NOT NULL,
    mealPrice DECIMAL(8,2) NOT NULL,
    PRIMARY KEY (orderId)
);

INSERT INTO orders(mealName, mealPrice) VALUES
("Fries", 4.99),
("Hamburger", 9.90);

CREATE TABLE customersorders(
    customerId MEDIUMINT NOT NULL,
    orderId MEDIUMINT NOT NULL,
    PRIMARY KEY(customerId, orderId),
    FOREIGN KEY (customerId) REFERENCES customers(customerId),
    FOREIGN KEY (orderId) REFERENCES orders(orderId)
);

INSERT INTO customersorders(customerId, orderId) VALUES
(1,1),
(1,2),
(2,1),
(3,2);


