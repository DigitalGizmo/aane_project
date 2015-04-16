#!/bin/sh

dbname="aanedata"
username="root"

psql $dbname $username << EOF
	GRANT ALL ON ALL TABLES IN SCHEMA public to aanedata_user;
	GRANT ALL ON ALL SEQUENCES IN SCHEMA public to aanedata_user;
	GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to aanedata_user;
EOF
