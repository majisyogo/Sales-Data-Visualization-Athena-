import boto3
import time

# AWS region and output S3 bucket
REGION = "ap-northeast-1"
OUTPUT_LOCATION = "s3://your-bucket-name/query-results/"
DATABASE = "demo_db"
QUERY_STRING = """
CREATE DATABASE IF NOT EXISTS demo_db;
CREATE EXTERNAL TABLE IF NOT EXISTS demo_db.sales (
    order_id INT,
    customer_id INT,
    amount DOUBLE,
    order_date STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 's3://your-bucket-name/data/';
"""

# Create Athena client
client = boto3.client("athena", region_name=REGION)

# Execute query
response = client.start_query_execution(
    QueryString=QUERY_STRING,
    QueryExecutionContext={"Database": DATABASE},
    ResultConfiguration={"OutputLocation": OUTPUT_LOCATION}
)

query_execution_id = response["QueryExecutionId"]
print(f"Query started with ID: {query_execution_id}")

# Wait until the query is finished
while True:
    result = client.get_query_execution(QueryExecutionId=query_execution_id)
    status = result["QueryExecution"]["Status"]["State"]
    if status in ["SUCCEEDED", "FAILED", "CANCELLED"]:
        break
    print("Waiting for query to complete...")
    time.sleep(3)

print(f"Query finished with status: {status}")


