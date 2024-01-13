-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.32 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping data for table myapp.books: ~19 rows (approximately)
INSERT INTO `books` (`id`, `description`, `name`, `file_path`) VALUES
	(2, 'string', 'string', 'uploads/Dao of the Bizarre Immortal - Chapter 216 - Considerations.txt'),
	(3, '11', 'Books ', '123123'),
	(4, 'string', 'Book 1\r\n', 'uploads/Dao of the Bizarre Immortal - Chapter 216 - Considerations.txt'),
	(5, 'string', 'Book 1\r\n', 'uploads/Dao of the Bizarre Immortal - Chapter 216 - Considerations.txt'),
	(6, 'string', 'Book 1\r\n', 'uploads/Dao of the Bizarre Immortal - Chapter 216 - Considerations.txt'),
	(7, 'string', 'Book 1\r\n', 'uploads/Dao of the Bizarre Immortal - Chapter 216 - Considerations.txt'),
	(8, 'string', 'Book 1\r\n', 'uploads/Dao of the Bizarre Immortal - Chapter 216 - Considerations.txt'),
	(9, 'string', 'Book 1\r\n', 'uploads/Dao of the Bizarre Immortal - Chapter 216 - Considerations.txt'),
	(10, 'string', 'Book 1\r\n', 'uploads/Dao of the Bizarre Immortal - Chapter 216 - Considerations.txt'),
	(11, 'string', 'Book 1\r\n', 'uploads/Dao of the Bizarre Immortal - Chapter 216 - Considerations.txt'),
	(12, 'string', 'Book 1\r\n', 'uploads/Dao of the Bizarre Immortal - Chapter 216 - Considerations.txt'),
	(13, 'string', 'Book 1\r\n', 'uploads/Dao of the Bizarre Immortal - Chapter 216 - Considerations.txt'),
	(14, 'string', 'Book 1\r\n', 'uploads/Dao of the Bizarre Immortal - Chapter 216 - Considerations.txt'),
	(15, 'string', 'Book 1\r\n', 'uploads/Dao of the Bizarre Immortal - Chapter 216 - Considerations.txt'),
	(16, 'string', 'Book 1\r\n', 'uploads/Dao of the Bizarre Immortal - Chapter 216 - Considerations.txt'),
	(17, 'string', 'Book 1\r\n', 'uploads/Dao of the Bizarre Immortal - Chapter 216 - Considerations.txt'),
	(18, 'string', 'Book 1\r\n', 'uploads/Dao of the Bizarre Immortal - Chapter 216 - Considerations.txt'),
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

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
