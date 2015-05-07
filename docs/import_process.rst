Data Import Process
======================

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


