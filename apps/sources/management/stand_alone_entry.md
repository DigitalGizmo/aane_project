# Stand-alone entry page Request

## Overview
I need a new page type. This will be a stand-alone page (full page) for a source entry. Currently when on a source page such as /sources/source/2/ there is a list of entries (@templates/sources/source_detail.html). Selecting an entry opens a modal window with an HTMX URL: /sources/entry/{{entry.id}}/.
I would like that same url (/sources/entry/{{entry.id}}/), when entered in a browser, to bring up a full page with the same info as contained in the modal: @templates/sources/entry_pop_detail.html  

## Requirements
- the new page will have the same header layout as other page, e.g. @templates/sources/source_detail.html
- The breadcrum will point back to the appropriate Source Detail list, that is @templates/sources/source_detail.html
- the url of the new page type will be: /sources/entry/{{entry.id}}/
- Let's call the new template source_detail_full.html

## Examples


## Suggestions/Notes
- Later I may want all internal entry links to go to the full page, but for now I want to keep the modal window behavior for internal links.