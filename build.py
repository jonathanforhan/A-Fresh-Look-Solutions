import os

CSS = "../style.css"
MATH_ENGINE = "mathjax=https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"

if not os.path.isdir("html/"):
    os.mkdir("html/")

# build stage 1, charts and figures
for i in range(2, 12):
    if os.path.isfile(f"latex/chapter_{i}/build.py"):
        dir = os.getcwd()
        os.chdir(f"latex/chapter_{i}/")
        os.system("python3 build.py")
        os.chdir(dir)

# build stage 2, html pages
for i in range(2, 12):
    os.system(f"pandoc -s --{MATH_ENGINE} -c {CSS} latex/chapter_{i}/chapter_{i}.tex -o html/chapter_{i}.html")
