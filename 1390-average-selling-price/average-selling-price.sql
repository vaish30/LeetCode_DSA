-- -- # Write your MySQL query statement below

-- -- select product_id, 



-- -- from UnitsSold where purchase_date between '2019-02-17' and '2019-02-28'

-- -- units * price 

-- -- WITH purchase_prices AS (
-- --     SELECT
-- --         distinct p.product_id,
-- --         CASE 
-- --             WHEN p.product_id = 1 AND u.purchase_date BETWEEN '2019-02-17' AND '2019-02-28' THEN u.units * 5
-- --             WHEN p.product_id = 1 AND u.purchase_date BETWEEN '2019-03-01' AND '2019-03-22' THEN u.units * 20
-- --             WHEN p.product_id = 2 AND u.purchase_date BETWEEN '2019-02-01' AND '2019-02-20' THEN u.units * 200
-- --             WHEN p.product_id = 2 AND u.purchase_date BETWEEN '2019-02-21' AND '2019-03-31' THEN u.units * 30
-- --             ELSE 0 
-- --         END AS price
-- --     FROM
-- --         UnitsSold u
-- --         JOIN Prices p ON u.product_id = p.product_id
-- -- )
-- -- SELECT * FROM purchase_prices;


-- with purchase_prices as (
--     select
--        u.product_id, u.purchase_date, u.units, p.price
--     from
--        Prices p left join UnitsSold u on p.product_id = u.product_id and u.purchase_date between p.start_date and p.end_date
-- )

-- -- select * from purchase_prices;

-- select product_id, IFNULL(round(sum(units*price)/sum(units),2),0) as average_price from purchase_prices group by product_id;


SELECT p.product_id, IFNULL(ROUND(SUM(units*price)/SUM(units),2),0) AS average_price
FROM Prices p LEFT JOIN UnitsSold u
ON p.product_id = u.product_id AND
u.purchase_date BETWEEN start_date AND end_date
group by product_id

