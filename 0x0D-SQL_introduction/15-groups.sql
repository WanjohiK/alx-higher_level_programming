-- script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

-- Don’t list rows without a name value
-- Results should display the score and the name (in this order)
-- Records should be listed by descending score

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
