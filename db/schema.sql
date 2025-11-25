CREATE KEYSPACE IF NOT EXISTS iot
WITH REPLICATION = {
  'class': 'SimpleStrategy',
  'replication_factor': 2
};

USE iot;

CREATE TABLE IF NOT EXISTS readings (
    sede         text,
    sensor_type  text,
    sensor_id    text,
    ts           timestamp,
    value        double,
    PRIMARY KEY ((sede, sensor_type), ts, sensor_id)
) WITH CLUSTERING ORDER BY (ts DESC);
