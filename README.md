# DB_Data_puller
This repo provides Rest implmentation of data query - very basic version of GraphQL.
It is built over flask and used to fetch data from Oracle DB.
Routes - 
* /get_tables - default route returns all tables available to query for a particular owner here 'ADMIN'
* /get_tables/<tables_name> - returns all the columns in the table with primary key.
* /get_tables/<tables_name>/<column_name>/column_value> - actual data in the db.
