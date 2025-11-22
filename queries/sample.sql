CREATE DATABASE IF NOT EXISTS sales_db;

CREATE EXTERNAL TABLE IF NOT EXISTS sales_db.sales (
    date STRING,
    product STRING,
    quantity INT,
    price DOUBLE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 's3://your-bucket-name/data/';

