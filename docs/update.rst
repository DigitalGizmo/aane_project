Update 2021
==============

go from 1.7 to 1.11.17

From 1.11 to 2.2.23
- squashmigrations
  
From 2.2 to 3.2
- pip install --upgrade Django==3.0.14
- pip install --upgrade Django==3.2.3

Data transfer
---------------

pg_dump -Fc --clean --verbose aanedata --user=aanedata_user > aanedata_2015_07_10.backup
pg_restore --dbname=aanedata --verbose aanedata_2021_05_17.backup

- updated url patterns
- added apps.py
  
Migrations, had to do fake
# database already has it
manage.py migrate sources 0009 --fake
