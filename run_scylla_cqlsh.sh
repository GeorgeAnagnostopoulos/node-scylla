#!/bin/bash

#runs the Scylla CQL shell
# scylla1 -> the running scylladb container
# presents a CQL cli
docker run -it --link scylla1:cassandra --rm cassandra:latest /bin/bash -c 'exec cqlsh "$CASSANDRA_PORT_9042_TCP_ADDR" --cqlversion="3.2.0" --color'
