#!/bin/bash

### Title:    Compile LaTeX Files
### Author:   Kyle M. Lang
### Created:  2019-10-30
### Modified: 2019-10-31

### USAGE:
###   ./compileLatex.sh TEX_FILE PATH_FILE
### ARGS:
###   TEX_FILE  = Relative or absolute path (with file name and extension) to
###               the LaTeX file to be compiled
###   PATH_FILE = Relative or absolute path (with file name and extension) to a
###               plain-text file listing the paths of the directories holding
###               the raw BibTex files, the BibTex annotation files, and the
###               helper scripts.
###               - Note that these paths can be either absolute or relative,
###                 but relative pathes will be interpreted with respect to the
###                 directory holding the LaTeX file provided for the TEX_FILE
###                 argument.
###               - The paths listed in the file should include a trailing slash
###               - This file should contain exactly three lines with one path
###                 define on each line:
###               -- Line 1: Path to raw BibTex files
###               -- Line 2: Path to BibTex annotation files
###               -- Line 3: Path to helper script directory

texName=$(basename $1) # Name of the LaTeX file
texPath=$(dirname $1)  # Directory holding the LaTeX file

## Define file paths used below:
rawPath=$(cat $2 | sed -n "1p") # Raw BibTex
annPath=$(cat $2 | sed -n "2p") # BibTex annotations
binPath=$(cat $2 | sed -n "3p") # Software directory

cd $texPath

## Record when we're starting:
t0=$(date +%T)

## Find the BibTex files used in the LaTeX doc:
bibs=$(python ${binPath}findBib.py $texName.tex)

## Annotate the BibTex files:
for bib in $bibs; do
    if [ ! -f "$bib" ]; then
	python ${binPath}annotateBibFile.py ${rawPath}$bib ${annPath}$bib ./$bib
    fi
done

## Compile the LaTeX file:
pdflatex $texName.tex

## Find all the newly created auxiliary files:
auxFiles=$(find * -newermt $t0 | grep aux)

## Run bibtex on each auxiliary file:
for aux in $auxFiles; do bibtex $aux; done

## Do the final LaTeX compilations:
pdflatex $texName.tex
pdflatex $texName.tex

## Clean up: Move the final PDF file to the appropriate directory
mv ${texName/.tex/.pdf} ../pdf

## Clean up: Remove any newly created files:
newFiles=$(find * -newermt $t0)
for nf in $newFiles; do rm $nf; done
