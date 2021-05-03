CREATE DATABASE scpFoundation;

\c scpfoundation

DROP TABLE users;
DROP TABLE experiments;
DROP TYPE contLevel;

CREATE TYPE contLevel AS ENUM ('apollyon', 'euclid', 'keter', 'thaumiel', 'safe', 'neutralized');

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    password VARCHAR,
    status VARCHAR
);

CREATE TABLE experiments (
    id SERIAL PRIMARY KEY,
    codename VARCHAR,
    containment contLevel,
    description VARCHAR,
    img VARCHAR
);

CREATE USER yeetus WITH PASSWORD 'stardate2387jellyfish';

GRANT SELECT ON ALL TABLES IN SCHEMA public TO yeetus;

\i /opt/challenge/addItems.sql
