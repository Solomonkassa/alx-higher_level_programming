# 0x0D. SQL - Introduction

This directory contains solutions to tasks on the topic of SQL, specifically on the basics of SQL language and usage in MySQL.

## Resources
* [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
* [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial)
* [SQL Syntax Cheatsheet](https://www.sqltutorial.org/sql-cheat-sheet/)
* [Introduction to SQL](https://www.w3schools.com/sql/sql_intro.asp)
* [SQL Style Guide](https://www.sqlstyle.guide/)

## Learning Objectives
* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does `DDL` and `DML` stand for
* How to `CREATE` or `ALTER` a table
* How to `SELECT` data from a table
* How to `INSERT`, `UPDATE` or `DELETE` data
* What are `subqueries`
* How to use MySQL functions

## Requirements
* All files are written and compiled on Ubuntu 20.04 LTS using MySQL 5.7 (version 5.7.8-rc)
* All SQL queries should have no error messages
* All SQL keywords should be in uppercase (ex. `SELECT`, `WHERE`...)

## Tasks
* [0. List databases](./0-list_databases.sql): Write a script that lists all databases of your MySQL server.
* [1. Create a database](./1-create_database_if_missing.sql): Write a script that creates the database `hbtn_0c_0` in your MySQL server.
* [2. Delete a database](./2-remove_database.sql): Write a script that deletes the database `hbtn_0c_0` in your MySQL server.
* [3. List tables](./3-list_tables.sql): Write a script that lists all the tables of a database in your MySQL server.
* [4. First table](./4-first_table.sql): Write a script that creates a table called `first_table` in the current database in your MySQL server.
* [5. Full description](./5-full_table.sql): Write a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
* [6. List all in table](./6-list_values.sql): Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
* [7. First add](./7-insert_value.sql): Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.
* [8. Count 89](./8-count_89.sql): Write a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.
* [9. Full creation](./9-full_creation.sql): Write a script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.
* [10. List by best](./10-top_score.sql): Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

# AUTHOR 
- [Solomon Kassa](https://github.com/somonkassa/)
