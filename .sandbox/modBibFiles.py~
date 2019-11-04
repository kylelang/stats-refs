### Title:    Format BibTex files
### Author:   Kyle M. Lang
### Created:  2019-10-30
### Modified: 2019-10-30

import sys
import bibtexparser as btp
from bibtexparser.bibdatabase import BibDatabase as bdb
from bibtexparser.bwriter import BibTexWriter as btw

###--------------------------------------------------------------------------###

def formatBibTex(iFile, oFile):
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
        f1.write(iFile.comments[0])
        f1.write("\n\n")
        btp.dump(iFile, f1, writer)

    return(0)

###--------------------------------------------------------------------------###

def annotate(rawFile, annFile, outFile):
    ## Read in the raw BibTex file:
    with open(rawFile, "r") as f0: raw = btp.load(f0)

    ## Read in the annotations file:
    with open(annFile, "r") as f1: ann = btp.load(f1)

    ## Express entry lists as dictionaries:
    entRaw = raw.entries_dict
    entAnn = ann.entries_dict

    ## Update each BibTex entry with the appropriate annotation:
    for key in entAnn:
        if key in entRaw:
            entRaw[key].update(entAnn[key])

    ## Format and write out the annotated BibTex file:
    formatBibTex(iFile = raw, oFile = oFile)

    return(0)

'''
args = sys.argv

if len(args) > 3:
    order = args[3]
else:
    order = None

formatBibTex(iFile = args[1], oFile = args[2], order = order)
'''
