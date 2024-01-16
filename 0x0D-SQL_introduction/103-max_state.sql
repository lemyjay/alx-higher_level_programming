-- Task 20: Temperatures #2
-- This script displays the max temperature of each state (ordered by State name).
SELECT state, MAX(value) FROM temperatures GROUP BY state ORDER BY state;
