CREATE DATABASE findtorun;
CREATE USER findtorun_user WITH PASSWORD 'p@$$w0rd111!!!'; ALTER USER findtorun_user CREATEDB; ALTER ROLE findtorun_user SET client_encoding TO 'utf8'; ALTER ROLE findtorun_user SET default_transaction_isolation TO 'read committed'; ALTER ROLE findtorun_user SET timezone TO 'UTC'; GRANT ALL PRIVILEGES ON DATABASE findtorun TO findtorun_user;
