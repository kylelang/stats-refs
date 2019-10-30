### Title:    Format BibTex files
### Author:   Kyle M. Lang
### Created:  2019-10-30
### Modified: 2019-10-30

iFile = "test1.bib" # Input file name
oFile = "out3.bib"  # Output file name
order = 2           # How to order fields?

import bibtexparser as btp
from bibtexparser.bwriter import BibTexWriter
    
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
    raise Exception("Invalid value for 'order'")

writer.display_order = do
writer.contents = ["comments", "preambles", "strings", "entries"]

## Read in the raw BibTex file:
with open(iFile, "r") as f0: tmp = btp.load(f0)

print("Comments:")
print(tmp.comments)

print(len(tmp.comments))

with open("out4.bib", "w") as f:
    for com in tmp.comments: f.write(com)
    f.write("\r\n\r\n") # use Windows-style eol characters to be consistent with bibtexparser
    f.write("Hello world")
        
'''
## Write out the BibTex file with appropriate formatting:
with open(oFile, "w") as out: btp.dump(tmp, out, writer)

class FormatBibTex(BibTexWriter):
    def __init__(self, bibFile, order):
        super().__init__()
        with open(bibFile, "r") as inBib: _bib0 = btp.load(inBib)
        _order = order

    def 
'''
