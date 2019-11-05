# stats-refs

This repository contains thematically organized reading lists/BibTex files for
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
  programmatic modification, formatting, and compilation of reading lists
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
file via the `/bin/formatBibFile.py` Python script.
- For example, running the following code would apply the formatting guidelines
  described above to `myRefs.bib` and return the formatted result as
  `myRefs2.bib`.
  - `python formatBibFile.py /path/to/myRefs/myRefs.bib myRefs2.bib`
  
BibTex files can be annotated (e.g., by merging the BibTex files from the */raw*
and */annotated* directories) via the `/bin/annotateBibFile.py` Python script.
- For example, running the following code would apply the annotations contained
  in `myAnnotations.bib` to `myRefs.bib` and return the results as
  `myRefs2.bib`.
  - `python annotateBibFile.py /path/to/myRefs/myRefs.bib
    /path/to/myAnnotations/myAnnotations.bib myRefs2.bib`
  
LaTeX files can be compiled into PDF files via the `/bin/compileLatex.sh`
shell script.
- For example, running the following code would compile `myDoc.tex` using the
  resources defined in `myPaths.txt` (please refer to the documentation in the
  `compileLatex.sh` script for details on how to format the `myPaths.txt` file).
  - `./compileLatex.sh /path/to/myDoc/myDoc.tex /path/to/myPaths/myPaths.txt`

To execute the above commands, the script (i.e., `formatBibFile.py`,
`annotateBibFile.py`, or `compileLatex.sh`) MUST be in the current working
directory OR be findable via the search path defined by your $PATH variable

## Contributing to the Project
We're happy to accept contributions from people outside the core stat-refs
team. All such contributions SHOULD be submitted via a pull request.

In particular, we welcome any of the following types of contributions:
- Annotations for existing BibTex entries
- New BibTex entries
- New reading lists within an extant theme (i.e., LaTeX source and compiled PDF
  documents)
- New thematic directories
  - Any new thematic directories SHOULD include, at least, a [set of] BibTex
    files.
- Corrections to errors in existing BibTex files
- Improvements to the scripts in the *\bin* directory
- Scripts to make the programmatic workflow described above portable to non-*nix
  style operating systems
