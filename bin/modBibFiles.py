### Title:    Modify BibTex files
### Author:   Kyle M. Lang
### Created:  2019-10-30
### Modified: 2019-10-30

import bibtexparser as btp
from bibtexparser.bibdatabase import BibDatabase as bdb
from bibtexparser.bwriter import BibTexWriter as btw

###--------------------------------------------------------------------------###

def formatBib(iFile, oFile):
    ## Instantiate a BibTexWriter object:
    writer = btw()

    ## Modify the writer's behavior to format output:
    writer.indent           = "  "
    writer.order_entries_by = ("key", "author", "year")
    writer.contents         = ["entries"]
    writer.display_order    = ("key", "title", "author", "year")
    
    ## Read in the raw BibTex file:
    if(type(iFile) is str):
        with open(iFile, "r") as f0: iFile = btp.load(f0)
    elif(type(iFile is bdb)):
        pass
    else:
        raise Exception("iFile must be a string or a BibDatabase object")
    
    ## Write out a correctly formatted BibTex file:
    with open(oFile, "w") as f1:
        f1.write(iFile.comments[0]) # Write the header 
        f1.write("\n\n")
        btp.dump(iFile, f1, writer) # Write the entries

###--------------------------------------------------------------------------###

def extendBib(rawFile, extFile, outFile):
    ## Read in the raw BibTex file:
    with open(rawFile, "r") as f0: raw = btp.load(f0)

    ## Read in the extensions file:
    with open(extFile, "r") as f1: ext = btp.load(f1)

    ## Express entry lists as dictionaries:
    entRaw = raw.entries_dict
    entExt = ext.entries_dict

    ## Add new fields to the appropriate BibTex entries: 
    for key in entExt:
        if key in entRaw:
            entRaw[key].update(entExt[key])

    ## Format and write out the annotated BibTex file:
    formatBib(iFile = raw, oFile = outFile)
