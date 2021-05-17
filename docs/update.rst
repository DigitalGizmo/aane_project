Update 2021
==============

go from 1.7 to 1.11.17

Created local db w pgAdmin
Getting backup from Gizmo ..201 via pgAdmin

Permissions to grant in Admin
Three each: add, change, delete
aa person
o_person
primary source
source entry

Data transfer
---------------

pg_dump -Fc --clean --verbose aanedata --user=aanedata_user > aanedata_2015_07_10.backup
pg_restore --dbname=aanedata --verbose aanedata_2021_05_17.backup
