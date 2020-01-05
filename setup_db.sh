#!/bin/bash

USER = root
PASS = root

mysql --user="${USER}" --password="${PASS}" --execute="CREATE DATABASE floodfireNewsdiffTest;"
mysql --user="${USER}" --password="${PASS}" floodfireNewsdiffTest < _INSTALL/ffnewsdiff.sql
printf "[RDB]\nDB_HOST = localhost\nDB_PORT = 3306\nDB_USER = ${USER}\nDB_PASSWORD = ${PASS}\nDB_DATABASE = floodfireNewsdiffTest\n" > config.ini