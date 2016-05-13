#!/bin/bash

#runs the Scylla CQL shell
docker run -it --link scylla1:cassandra -v /home:/home/sw/myWork/angular/node-scylla --rm cassandra /bin/bash -c 'exec cqlsh "$CASSANDRA_PORT_9042_TCP_ADDR" --cqlversion="3.2.0" --color'
