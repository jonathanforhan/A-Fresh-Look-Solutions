import os

if not os.path.exists("plot_2-5.svg"):
    os.system("pdflatex plot_2-5.tex -o plot_2-5.pdf")
    os.system("pdf2svg plot_2-5.pdf plot_2-5.svg")
