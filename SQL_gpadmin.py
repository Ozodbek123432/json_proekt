# -- SELECT DISTINCT ship_via
# -- FROM orders
# -- 1- vazifa
# -- SELECT first_name, last_name, birth_date
# -- FROM Employees
# -- 2 chi vaziifa
# -- SELECT *
# -- FROM products
# -- WHERE product_name = 'Chang'
# -- vazifa
# -- SELECT *
# -- FROM Orders
# -- WHERE ship_country = 'France'
#
# -- 4 vazifa
# -- SELECT *
# -- FROM Orders
# -- WHERE freight =  40
# -- 5masala
# -- SELECT *
# -- FROM Products
# -- WHERE unit_price =  18 AND discontinued = 1
# -- 1 vazifa
# SELECT *
# FROM customers
# -- 2 vazifa
# SELECT contact_name
# FROM customers
# -- 3 vazifa
# SELECT *
# FROM orders
# -- 4 vazifa
# SELECT city
# FROM customers
# -- 5 vazifa
# SELECT city,region, country
# FROM customers
# -- 6 vazifa
# SELECT COUNT(*)
# FROM customers
# -- 7 vazifa
# SELECT COUNT(city)
# FROM customers
# SELECT freight
# FROM orders
# WHERE freight BETWEEN 10 AND 50
# --  3 VAZIFA
# SELECT  product_name
# FROM products
# ORDER BY  product_name ASC
# -- 4 VAZIFA
# SELECT   discontinued
# FROM products
# WHERE  discontinued = 1
# --5 VAZIFA
# SELECT *
# FROM customers
# WHERE country IN ('German','UK','USA')
