-- Task 17: Go to UTF8
-- This script converts hbtn_0c_0 database to UTF8(utf8mb4, collate utf8mb4_unicode_ci) in the MySQL server.
-- Convert the database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE hbtn_0c_0;

-- Convert the table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
