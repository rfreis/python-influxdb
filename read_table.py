from db import query_api, bucket


## using Table structure
tables = query_api.query(f'from(bucket:"{bucket}") |> range(start: -10m)')

for table in tables:
    print(table)
    for row in table.records:
        print (row.values)
