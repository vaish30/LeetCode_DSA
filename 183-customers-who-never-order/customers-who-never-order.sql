# Write your MySQL query statement below
select c.name AS Customers from Customers as c where c.id not in (select o.customerId from Orders as o)