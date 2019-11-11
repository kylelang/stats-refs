This directory contains various help scripts. These scripts are meant to help
modifying BibTex files and compiling LaTeX files. Below you will find some brief
information about the scripts contained in this directory.

annotateBibFile.py: Add annotations to raw BibTex files

formatBibFile.py:   Apply project formatting rules to BibTex files

modBibFiles.py:     Python module containing functions to programatically format
                    and merge BibTex files. This module is used by
		    'annotateBibFile.py' and 'formatBibFile.py'.

findBib.py:         Extract the names of BibTex files called within a LaTeX
                    source file.

compileLatex.sh:    Compile LaTeX source into a PDF
