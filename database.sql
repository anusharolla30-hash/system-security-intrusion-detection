DROP DATABASE IF EXISTS security;
CREATE DATABASE security;
USE security;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
INSERT INTO users (username, password)
VALUES ('admin2', 'pass456');

CREATE TABLE security_questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    question VARCHAR(255) NOT NULL,
    answer VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
INSERT INTO security_questions (user_id, question, answer) VALUES
(1, 'What is your favorite fruit?', 'mango'),
(1, 'What is your pet’s name?', 'buddy'),
(1, 'What city were you born in?', 'delhi'),
(1, 'What is your mother’s name?', 'pushpa'),
(1, 'What was the name of your first school?', 'dnyansampada'),
(1, 'What is your favorite color?', 'pink'),
(1, 'What is your best friend’s name?', 'honey bunny'),
(1, 'What is your dream job?', 'engineer'),
(1, 'What is your favorite Actor?', 'allu arjun'),
(1, 'What is your favorite food?', 'chinese');

SELECT * FROM users;
SELECT * FROM security_questions;