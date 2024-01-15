CREATE USER 'root'@'%' IDENTIFIED BY '12345'; 
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;

CREATE DATABASE myapp;
USE myapp;

CREATE TABLE users(
	id INT AUTO_INCREMENT PRIMARY KEY,
	username VARCHAR(50),
	email VARCHAR(50),
	pass_hash VARCHAR(255) NOT NULL
);

CREATE TABLE books (
	id INT AUTO_INCREMENT PRIMARY KEY,
	description TEXT,
	name VARCHAR(255) NOT NULL,
	file_path VARCHAR(255) NOT NULL,
	preview_path VARCHAR(255)
);

CREATE TABLE reviews (
	id INT AUTO_INCREMENT PRIMARY KEY,
	content VARCHAR(1000),
	owner_id INT NOT NULL,
	book_id INT NOT NULL,
	FOREIGN KEY (owner_id) REFERENCES users(id),
	FOREIGN KEY (book_id) REFERENCES books(id)
);

CREATE TABLE user_book_link (
	user_id INT NOT NULL,
	book_id INT NOT NULL,
	FOREIGN KEY (book_id) REFERENCES books(id),
	FOREIGN KEY (user_id) REFERENCES users(id),
	PRIMARY KEY (book_id, user_id)
);

INSERT INTO `books` (`id`, `description`, `name`, `file_path`) VALUES
	(19, 'Describe me some balls', 'Test1', 'uploads/NhQ-VTpn1d2Ln4KNeLvBqg.pdf'),
	(20, 'A book about my cock', 'Is Worse Really Better?', 'uploads/nIny4SrLaWfVP0j8laXn0Q.pdf'),
	(21, 'who knows', 'Some kind of document', 'uploads/29z081tu-M2LDlZOuDEiVQ.pdf'),
	(22, 'Some book on blood magic I had lying around', 'Blood Magick', 'uploads/DfVGhuqjPgrfyUSD0wpfrQ.pdf'),
	(23, 'Idk', 'To Greybach Normal form', 'uploads/irRTHV6aXEYtvQm5JWg_XQ.pdf');

-- Dumping data for table myapp.reviews: ~0 rows (approximately)

-- Dumping data for table myapp.users: ~2 rows (approximately)
INSERT INTO `users` (`id`, `username`, `email`, `pass_hash`) VALUES
	(5, 'alex1111', 'alex@alex.alex', '$2b$12$KDY/DLUkwdaJDVLC2xP1TeFCp3iXHpFpHpS33dTDPvfyCd7jcK9B.'),
	(6, 'super', 'super@super', '$2b$12$td6zOMNCmVURdWivlIFB7OEMdc/70pxX/63tsx8zeILuCBPbG8BWO');

-- Dumping data for table myapp.user_book_link: ~9 rows (approximately)
INSERT INTO `user_book_link` (`user_id`, `book_id`) VALUES
	(5, 2),
	(5, 3),
	(5, 6),
	(5, 8),
	(5, 12),
	(5, 15),
	(5, 18),
	(5, 19),
	(5, 22);