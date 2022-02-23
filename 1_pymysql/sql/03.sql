drop database if exists test_db;
create database test_db;

CREATE TABLE `test_db`.`user` (
   `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
   `type` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '0',
   `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `password` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `sex` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '1',
   `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `birth_date` varchar(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `phone_number` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `active` tinyint(4) NOT NULL DEFAULT 1,
   `created_at` timestamp NULL DEFAULT current_timestamp(),
   `updated_at` timestamp NULL DEFAULT NULL ON UPDATE current_timestamp(),
   PRIMARY KEY (`id`),
   UNIQUE KEY `UK_USERS_EMAIL` (`email`)
 );

INSERT INTO `test_db`.`user`
 (`active`,`password`,`phone_number`,`updated_at`,`created_at`,`email`,`type`,`birth_date`,`name`,`id`,`sex`)
VALUES ("1", "1", "01014686004", NULL, "2020-08-23 17:47:37", "jini", "0", "921216", "지니", "1", "2"),
("0", "22", "01012341234", "2021-02-08 17:59:37", "2020-09-09 17:04:32", "coco", "2", "930901", "코코", "2", "2"),
 ("1", "333", "01023231231", NULL, "2020-11-28 16:13:09", "sol", "0", "930101", "솔", "3", "1"),
 ("1", "444", "01022223333", NULL, "2020-12-03 05:09:37", "siwoo", "0", "920924", "시우", "4", "1"),
  ("1", "23", "01077772222", "2021-02-10 16:27:29", "2021-02-10 16:12:41", "sol2", "2", "89022", "솔", "5", "1");
COMMIT;
