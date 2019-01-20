-- EXERCISE:

-- Aggregate functions
-- Often, you will want to perform some calculation on the data in a database. SQL provides a few functions, called aggregate functions, to help you out with this.

-- For example,

-- SELECT AVG(budget)
-- FROM films;
-- gives you the average value from the budget column of the films table. Similarly, the MAX function returns the highest budget:

-- SELECT MAX(budget)
-- FROM films;
-- The SUM function returns the result of adding up the numeric values in a column:

-- SELECT SUM(budget)
-- FROM films;
-- You can probably guess what the MIN function does! Now it's your turn to try out some SQL functions.


-- INSTRUCTIONS:

-- * Use the SUM function to get the total duration of all films.

-- * Get the average duration of all films.

-- * Get the duration of the shortest film.


-- CODE

SELECT MAX(duration)
FROM films;

SELECT SUM(duration)
FROM films;

SELECT AVG(duration)
FROM films;

SELECT MIN(duration)
FROM films;
