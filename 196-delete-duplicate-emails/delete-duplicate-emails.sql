# Write your MySQL query statement below
-- delete from Person where id in (select max_id from (select max(id)as max_id from Person group by email having count(email) >=2) as e)

-- DELETE p
-- FROM Person p
-- JOIN (
--     SELECT MAX(id) AS max_id
--     FROM Person
--     GROUP BY email
--     HAVING COUNT(email) >= 2
-- ) AS e
-- ON p.id = e.max_id;

DELETE p1
FROM Person p1, Person p2
WHERE p1.Email = p2.Email AND
p1.Id > p2.Id