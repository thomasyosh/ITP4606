#!/bin/sh
set -e
set -u
# su -
# apt-get -y install bash-completion wget
# wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | 
# apt-key add -
# apt-get update
# apt-get -y install postgresql-client

create_database() {
    PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$POSTGRES_HOST" -p "5432" -U "$POSTGRES_USER"<<-EOSQL
    SELECT 'CREATE DATABASE "$POSTGRES_DB"'
    WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '$POSTGRES_DB')\gexec
EOSQL
}

connect_database() {
    PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$POSTGRES_HOST" -p "5432" -U "$POSTGRES_USER" -d "$POSTGRES_DB"
}

create_database
connect_database