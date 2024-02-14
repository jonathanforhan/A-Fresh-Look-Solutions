#!/usr/bin/bash

if ! test -f "plot_2-5.svg"; then
    pdflatex plot_2-5.tex -o plot_2-5.pdf
    pdf2svg plot_2-5.pdf plot_2-5.svg
fi
