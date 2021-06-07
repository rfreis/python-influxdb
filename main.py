import os

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS


bucket = os.environ.get('DOCKER_INFLUXDB_INIT_BUCKET', 'my_bucket')


db_host = os.environ.get('DOCKER_INFLUXDB_HOST', 'influxdb')
db_port = os.environ.get('DOCKER_INFLUXDB_PORT', '8086')
db_token = os.environ.get('DOCKER_INFLUXDB_INIT_ADMIN_TOKENN', 'mytoken')
db_org = os.environ.get('DOCKER_INFLUXDB_INIT_ORG', 'my_org')


client = InfluxDBClient(url=f"http://{db_host}:{db_port}", token=db_token, org=db_org)

write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

p = Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)

write_api.write(bucket=bucket, record=p)

## using Table structure
tables = query_api.query(f'from(bucket:"{bucket}") |> range(start: -10m)')

for table in tables:
    print(table)
    for row in table.records:
        print (row.values)


## using csv library
csv_result = query_api.query_csv(f'from(bucket:"{bucket}") |> range(start: -10m)')
val_count = 0
for row in csv_result:
    for cell in row:
        val_count += 1