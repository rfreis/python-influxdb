#!/bin/bash

influx setup --bucket $INFLUXDB_INIT_BUCKET -t mytoken -o $INFLUXDB_INIT_ORG --username=$INFLUXDB_INIT_USERNAME --password=$INFLUXDB_INIT_PASSWORD --host=http://$INFLUXDB_HOST:$INFLUXDB_PORT
