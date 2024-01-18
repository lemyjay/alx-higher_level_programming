-- This script creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on the MySQL server.
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
) ORDER BY cities.id ASC;
