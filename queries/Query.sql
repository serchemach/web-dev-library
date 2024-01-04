-- CREATE TABLE users(
-- 	id INT AUTO_INCREMENT PRIMARY KEY,
-- 	username VARCHAR(50),
-- 	email VARCHAR(50),
-- 	pass_hash VARCHAR(255) NOT NULL
-- );

-- CREATE TABLE reviews (
-- 	id INT AUTO_INCREMENT PRIMARY KEY,
-- 	content VARCHAR(1000),
-- 	owner_id INT,
-- 	FOREIGN KEY (owner_id) REFERENCES users(id)
-- );

CREATE TABLE books (
	id INT AUTO_INCREMENT PRIMARY KEY,
	description TEXT,
	name VARCHAR(255) NOT NULL,
	file_path VARCHAR(255) NOT NULL
);