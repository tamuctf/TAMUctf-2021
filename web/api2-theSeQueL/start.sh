#!/bin/sh

su postgres -c "/usr/lib/postgresql/11/bin/initdb; /usr/lib/postgresql/11/bin/postgres" &

sleep 5

psql -U postgres -f /opt/challenge/setup.sql

./sequel
