#!/usr/bin/bash

CSS="style.css"
MATH_ENGINE="mathjax=https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"


mkdir -p dist/


# build stage 1, charts and figures
for i in {2..11};
do
    if test -f "latex/chapter_$i/build.sh"; then
        cwd=$(pwd);
        cd "latex/chapter_$i/" || exit 1;
        bash build.sh;
        cp ./*.svg "$cwd/dist"
        cd "$cwd" || exit 1;
    fi
done


# build stage 2, generate html
for i in {2..11};
do
    pandoc -s "--$MATH_ENGINE" -c "$CSS" "latex/chapter_$i/chapter_$i.tex" -o "dist/chapter_$i.html"
done


# build stage 3, package
cp index.html dist
cp style.css dist
