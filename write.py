from influxdb_client import Point
from db import write_api, bucket


p = Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)

write_api.write(bucket=bucket, record=p)
