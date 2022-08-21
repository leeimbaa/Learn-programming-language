USE sql_store	-- 选择数据库

SELECT 列名        
FROM 表名 

SELECT *	-- 选择列，用逗号分开，*代表全选列      
FROM customers	-- 选择表


SELECT first_name,customer_id
FROM customers
-- WHERE customer_id=1
ORDER BY frist_name

SELECT *
FROM customers
-- WHERE customer_id=1
ORDER BY first_name

SELECT 1,2
FROM customers
-- WHERE customer_id=1
ORDER BY first_name

SELECT last_name,first_name,customer_id,city,points
FROM customers
-- WHERE customer_id=1
-- ORDER BY frist_name


