### Title:    Test Python Parsing/Modification of BibTex files
### Author:   Kyle M. Lang
### Created:  2019-10-29
### Modified: 2019-10-29

import bibtexparser as btp
from bibtexparser.bwriter import BibTexWriter

order = 2

## Read in the raw BibTex file:
with open("test1.bib") as bib1: raw = btp.load(bib1)

## Read in the annotations file:
with open("test2.bib") as bib2: ann = btp.load(bib2)

## Express entry lists as dictionaries:
rawEnt = raw.entries_dict
annEnt = ann.entries_dict

## Update each BibTex entry with the appropriate annotation:
for key in annEnt:
    if key in rawEnt:
        rawEnt[key].update(annEnt[key])

## Modifying the writer's behavior:
writer = BibTexWriter()
writer.indent = "  "
writer.order_entries_by = ("key", "author", "year")

## How do we want to order the fields?
if order == 0:
    do = ()
elif order == 1:
    do = ("key", "title", "author", "year")
elif order == 2:
   do = ("key",
         "title",
         "booktitle",
         "author",
         "editor",
         "year",
         "month",
         "journal",
         "series",
         "edition",
         "chapter",
         "volume",
         "number",
         "pages",
         "type",
         "publisher",
         "institution",
         "organization",
         "school",
         "address",
         "howpublished",
         "url",
         "link",
         "doi",
         "crossref",
         "abstract",
         "annote",
         "note")
else:
    raise Exception("Invalid value for 'order'.")

writer.display_order = do

## Write out the updated BibTex file:
with open("out1.bib", "w") as out: btp.dump(raw, out, writer)
    
