#!/bin/bash

### Title:    Compile LaTeX Files
### Author:   Kyle M. Lang
### Created:  2019-10-30
### Modified: 2019-10-30

### ToDo: Create the annotated bib files on-the-fly

name=high_dim_imp

## Find the BibTex files used:
bibs=`python findBib.py $name`

## Record when we're starting:
t0=`date +%T`

## Make a temporary directory and move there:
#mkdir tmp
#cd tmp

## Pull the LaTeX file into 'tmp':
#cp ../$name.tex ./

## Compile the LaTeX file:
pdflatex $name.tex

## Find all the newly created auxiliary files:
auxFiles=`find * -newermt $t0 | grep aux`
#auxFiles=`ls -t *.aux`

## Run bibtex on each auxiliary file:
for f in $auxFiles; do
    bibtex $f
done

## Do the final LaTeX compilations:
pdflatex $name.tex
pdflatex $name.tex
