Data Handling
======================

Ongoing backups and transfer to local
-------------------------------------

Backup with custom format
::

	cd /var/www/dino_user/data/FTP_transfer


Inital trasnfer to change owner on local end to match. -p for plain text.
::

	pg_dump -OFp --create --verbose aanedata > aanedata_2015_04_16cpfix.backup

With Create, we need to delete and re-create public schema locally

ongoing backups
::

	pg_dump -Fc --clean --verbose aanedata --user=aanedata_user > aanedata_2015_07_10.backup

Import entries from "original" xls table
----------------------------------

clean backup - just in case::

	cd ~/Documents/Projects/AfrAmDB/DataBaks
	pg_dump -OFc --clean --verbose aanedata > aanedata_2015_04_28_clean.backup

For first import - Make sure SourceEntry is empty::

	DELETE FROM sources_sourceentry;

* Save Excel spreadsheet as CSV
* Delete top heading row in plain text.

Import
~~~~~~~
List fields that are being imported in the order they appear in the CSV. PK will be generated automatially. (Include field "clarified" even though it wasn't in original -- need all cols (except pk) represented in csv)

Run from psql command line.
The blanks will be handled by FORCE_NOT_NULL
::

	cd ~/Documents/Projects/AfrAmDB/export_import

	psql postgres
	\connect aanedata

	FORCE_NOT_NULL
	add last col not ref'd "clarified"

	COPY sources_sourceentry (access_order, legacy_id, date_status, low_year, low_month, low_day, upr_year, upr_month, upr_day, date_note, operson_id, legacy_enslaved_id, aa_id, name_note, event, entry_text, clarified, transaction_note, dollars, pounds, shillings, pence, farthing, primary_source_id, pvma_call_num, date_range, vol_book, page_num, notes) FROM '/Users/don/Documents/Projects/AfrAmDB/export_import/entries_4import_3.csv' (FORMAT csv, FORCE_NOT_NULL(date_note, name_note, event, transaction_note, pvma_call_num, date_range, vol_book, page_num, notes, clarified));

Import 2 - had to replace illegal Word ellipses with ..., remove fraction pence

Copy single table to server
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Delete and copy data for entries
::

	aanedata=# DELETE FROM sources_sourceentry;
	aanedata=# ALTER SEQUENCE sources_sourceentry_id_seq RESTART WITH 1;

	psql aanedata < sourceentry.sql

