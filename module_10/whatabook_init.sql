-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('1000 Main St, Austin, TX 78704');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('The Idiot', 'Fyodor Dostoyevsky', 'Novel');

INSERT INTO book(book_name, author, details)
    VALUES('The Lazarus Project', 'Aleksandar Hemon', 'Novel');

INSERT INTO book(book_name, author, details)
    VALUES('The Best Stories of Anton Chekov', 'Anton Chekov', "Short Stories");

INSERT INTO book(book_name, author)
    VALUES('Bosnia: A short History', 'Noel Malcom', 'History');

INSERT INTO book(book_name, author)
    VALUES('Python Crash Course', 'Eric Matthes', 'Computer Programming');

INSERT INTO book(book_name, author)
    VALUES("Kali linux Revealed", 'Offensive Security', 'Computer Security');

INSERT INTO book(book_name, author)
    VALUES('Kazakhstan Weightlifting System', 'Ivan Rojas', 'Exercise Science');

INSERT INTO book(book_name, author)
    VALUES('Linux Basics for Hackers', 'Occupy the Web', 'Computer Security');

INSERT INTO book(book_name, author)
    VALUES('The Book of Basketball', 'Bill Simmons', 'Sports');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Benny', 'Bones');

INSERT INTO user(first_name, last_name)
    VALUES('Bo', 'Bigs');

INSERT INTO user(first_name, last_name)
    VALUES('Jerry', 'Garcia');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Benny'), 
        (SELECT book_id FROM book WHERE book_name = 'Bosnia: A short History')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Bo'),
        (SELECT book_id FROM book WHERE book_name = 'The Idiot')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Jerry'),
        (SELECT book_id FROM book WHERE book_name = 'Linux Basics for Hackers')
    );
