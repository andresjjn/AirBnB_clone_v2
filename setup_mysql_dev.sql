-- prepares a MySQL server:
-- database hbnb_dev_db
-- user hbnb_dev (in localhost)
-- password hbnb_dev_pwd
-- all privileges on the database hbnb_dev_db
-- SELECT privilege on the database performance_schema

-- EXECUTE
-- cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
