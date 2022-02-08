CREATE TABLE authors(
    authorId INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(80) NOT NULL,
    nationality VARCHAR(80) NOT NULL,
    PRIMARY KEY(authorId)
);

INSERT INTO authors(name, nationality) VALUES
("Robert Jordan", "American"),
("Stieg Larsson", "Swedish"),
("Aki Linnanahde", "Finnish"),
("Enid Blyton", "English"),
("Tove Jansson", "Finnish");

CREATE TABLE books(
    bookId INT NOT NULL AUTO_INCREMENT,
    bookTitle VARCHAR(60) NOT NULL,
    publishedAt YEAR NULL,
    PRIMARY KEY(bookId)
);

INSERT INTO books(bookTitle, publishedAt) VALUES
("The Fires of Heaven", 1993),
("The Girl Who Played with Fire", 2006),
("JERE", 2017),
("Comet in Moominland", 1946),
("Five on a Treasure Island", 1942);

CREATE TABLE customers(
    customerId INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    address VARCHAR(50) NOT NULL,
    city VARCHAR(50),
    PRIMARY KEY(customerId),
    UNIQUE(email)
);

INSERT INTO customers(name, email, address, city) VALUES
("Ville Vihtalahti", "ville.vihtalahti@student.samk.fi", "Siltatie 4", "Pori"),
("Jake Notsocunning", "cunningnot@mymail.com", "Tapiontie 5 C 12", "Turku"),
("Esmeralda Toveson", "esme@mymail.com", "Kalakuja 8", "Rauma"),
("Jake Makeson", "makeson@mymail.com", "Hunajatakatu 10 A 16", "Turku"),
("Lumi Aura", "auranlumi@mymail.com", "Pellaamaantie 22", "Oulu");

CREATE TABLE authorBooks(
    authorId INT NOT NULL AUTO_INCREMENT,
    bookId INT NOT NULL,
    FOREIGN KEY(authorId) REFERENCES authors(authorId),
    FOREIGN KEY(bookId) REFERENCES books(bookId)
);

INSERT INTO authorBooks(bookId) VALUE
(5,5),
(3,3),
(4,4),
(1,1),
(2,2);

CREATE TABLE customerLoans(
    customerId INT NOT NULL,
    bookId INT NOT NULL,
    timeOfLoan DATE NOT NULL,
    FOREIGN KEY(customerId) REFERENCES customers(customerId),
    FOREIGN KEY(bookId) REFERENCES books(bookId)
);

INSERT INTO customerLoans(customerId, bookId, timeOfLoan) VALUES
(1,1,1, '2021-11-13'),
(2,3,3, '2021-11-13'),
(2,4,4, '2021-11-13'),
(4,2,2, '2021-10-16'),
(5,5,5, '2021-10-10');

CREATE TABLE customerReviews(
    customerId INT NOT NULL,
    bookId INT NOT NULL,
    bookScore DECIMAL(2,1) NOT NULL,
    FOREIGN KEY(customerId) REFERENCES customerLoans(customerId),
    FOREIGN KEY(bookId) REFERENCES customerLoans(bookId)
);

INSERT INTO `customerReviews`(`customerId`,`bookId`,`bookScore`) VALUES
    (1,1,5.0),
    (2,3,4.2),
    (2,4,3.6),
    (4,2,4.7),
    (5,5,4.5);