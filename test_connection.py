import snowflake.connector
import os
#export PASSWORD, WAREHOUSE, ACCOUNT, USER, DATABASE, SCHEMA, ROLE
PASSWORD = os.getenv('PASSWORD')
WAREHOUSE = os.getenv('WAREHOUSE')
ACCOUNT = os.getenv('ACCOUNT')
USER = os.getenv('USER')
DATABASE = os.getenv('DATABASE')
SCHEMA = os.getenv('SCHEMA')
ROLE = os.getenv('ROLE')

con = snowflake.connector.connect(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT,
    role=ROLE,
    warehouse=WAREHOUSE,
    database=DATABASE,
    schema=SCHEMA,
    session_parameters={
        'QUERY_TAG': 'EndOfMonthFinancials',
    }
)

print(con)

cur = con.cursor()
try:
  cur.execute("select O_CUSTKEY, O_ORDERKEY from new_orders limit 5;")
  for (col1, col2) in cur:
    print('{0}, {1}'.format(col1, col2))
finally:
    cur.close()
