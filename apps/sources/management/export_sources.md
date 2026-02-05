# Export Feature Request

## Overview
This will be a script to export source data as a .csv file. This will be similart to @export_aapeople_csv.py in the people app. 
The main difference from that script is that many of the fields needed here are indirect relations.

## Requirements
- export is from sources/models/SourceEntry
- Until functionality is confirmed only export 40 records.
- Put the .csv export file in @exports -- this is already ignored by git.

## Examples
Here are the desired fields plus my guesses as to how to access the related data:
Month	> low_month
Year	> low_year
LASTNAME (all caps)	> aa_persons[0].last_name
FirstName	> aa_persons[0].first_name
RecordType >	volume.primary_source.source_type.title
EnslaverLastName	> operson_fk.last_name
EnslaverFirstName	> operson_fk.first_name
City	> entry.volume.primary_source.location.title
State	> entry.volume.primary_source.location.state.abbr
Source 	> volume.primary_source.title
URL 	> https://aane.deerfield-ma.org/sources/source/{entry.id}/
Notes	> entry_text_html

## Suggestions/Notes
- There are potentially multiple aa_persons for a given entry -- for now let's just output the first one.
- The id in the URL is the id of the record
- Don't need to strip HTML