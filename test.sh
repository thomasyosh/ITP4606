#!/bin/sh

. ./.env

if [ "$DATABASE_TYPE" = "postgres" ]; then
    docker run -v ./backend/db/init.sh:/init.sh --env-file .env --rm postgres:latest ./init.sh
    docker rmi $(docker images 'postgres' -a -q)
    echo "Test IF";
fi

if [ "$DATABASE_TYPE" = "mysql" ]; then
    docker run -v ./backend/db/mysql_init.sh:/mysql_init.sh --env-file .env --rm mysql:latest ./mysql_init.sh
    docker rmi $(docker images 'mysql' -a -q)
    echo "mysql database init completed";
fi