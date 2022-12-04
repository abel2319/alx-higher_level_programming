-- a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
-- The result should display:
--     the score
--     the number of records for this score with the label number
-- The list should be sorted by the number of records (descending)
SELECT score, COUNT(DISTINCT score) as `number` FROM second_table GROUP BY `number` DESC;
