# stats-refs

This repository contains thematically organized reading lists/bibtex files for
statistical content.

## Structure
In an attempt to make this project as clear, user-friendly, and extensible as
possible, we employ a particular directory structure.
- This project contains two types of reading lists: *Raw* and *Annotated*.
  - The materials that go into the raw reading lists are stored in in the */raw*
    directory.
  - The materials that go into the annotated reading lists are stored in in the
    */annotated* directory.
- The */bin* directory contains Python and BASH scripts to facilitate
  programatic modification, formatting, and compilation of reading lists
- Both the */raw* and */annotated* directories contain thematic subdirectories
  (e.g., */raw/missingData*).
- Each thematic subdirectory contains three subdirectories: *latex*, *bibtex*,
  and *pdf*.
  - The *latex* directory contains the LaTeX files for each reading list.
  - The *bibtex* directory contains the underlying BibTex files.
  - The *pdf* directory contains compiled reading lists in PDF format.
  
## Formatting
The core of this project is it's set of BibTex files. One of the primary
motivations for this project was to create a centralized repository of
well-formatted BibTex files that could be used for diverse writing projects. To
keep these files as clean and useful as possible, we impose the following 
formatting rules.
- The BibTex files in the */raw* directory MUST NOT contain annotations.
  - I.e., these files have no `annote` field.
- The BibTex files in the */annotated* directory MUST contain only annotations.
  - I.e., the only field that these files have is the `annote` field.
- The entries in all BibTex files MUST be ordered in ascending alpha-numeric
  ordering with the following precedence:
  1. The entry's `key` field, if defined
  1. The surnames of the entry's `author` field
  1. The entry's `year` field
  1. The entry's `bibtexkey` field
- The first three fields in each entry SHOULD be:
  1. `title`
  1. `author`
  1. `year`
- The remaining fields SHOULD be ordered alphabetically.
- The `bibtexkey` field MUST be formatted as *author1Author2:year* where:
  - *author1* is the surname of the first author (with first letter lower-case)
  - *author2* is one of the following:
	1. An empty string when the publication has exactly one author
    1. Surname of the second author (with first letter upper-case) when the
       publication has exactly two authors
	1. The string-literal *"EtAl"* when the publication has three or more
       authors

## Programmatic Workflows
The project's formatting guidelines can be programatically applied to a BibTex
file via the `/bin/formatBibFile.py` script.

- For example, running the following code would apply the formatting guidelines
  described above to `myRefs.bib` and return the formatted result as
  `myRefs2.bib` (assuming `formatBibFile.py` and `myRefs.bib` are in the current
  working directory).
  - `python formatBibFile.py myRefs.bib myRefs2.bib`

BibTex files can be annotated (e.g., by merging the BibTex files from the */raw*
and */annotated* directories) via the `/bin/annotateBibFile.py` script.

LaTeX files can be compiled into PDF files via the `/bin/compileLatex.sh`
script.
