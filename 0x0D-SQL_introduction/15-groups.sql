-- Task 15: Number by score
-- This script lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in the MySQL server.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY SCORE
ORDER BY number DESC, score DESC;
