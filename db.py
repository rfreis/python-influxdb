import os

from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS


bucket = os.environ.get('INFLUXDB_INIT_BUCKET', 'my_bucket')


db_host = os.environ.get('INFLUXDB_HOST', 'influxdb')
db_port = os.environ.get('INFLUXDB_PORT', '8086')
db_token = os.environ.get('INFLUXDB_INIT_ADMIN_TOKENN', 'mytoken')
db_org = os.environ.get('INFLUXDB_INIT_ORG', 'my_org')


client = InfluxDBClient(url=f"http://{db_host}:{db_port}", token=db_token, org=db_org)

write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()
