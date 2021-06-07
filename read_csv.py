from db import query_api, bucket


## using csv library
csv_result = query_api.query_csv(f'from(bucket:"{bucket}") |> range(start: -10m)')
val_count = 0
for row in csv_result:
    for cell in row:
        val_count += 1