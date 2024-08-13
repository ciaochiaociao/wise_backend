@echo off

REM Variables
set DB_USER=postgres
set DB_NAME=wise

@REM REM Drop the database if it exists (requires superuser or database owner privileges)
@REM echo Dropping existing database (if it exists)...
@REM psql -U %DB_USER% -c "DROP DATABASE IF EXISTS %DB_NAME%;"

@REM REM Create the database
@REM echo Creating database...
@REM psql -U %DB_USER% -c "CREATE DATABASE %DB_NAME%;"

REM Apply the SQL script to the newly created database
echo Applying SQL script...
psql -U %DB_USER% -d %DB_NAME% -f create_db.sql

echo Database and schema setup complete.