# Write your MySQL query statement below

select s.unique_id, f.name from Employees as f LEFT JOIN EmployeeUNI as s on s.id = f.id