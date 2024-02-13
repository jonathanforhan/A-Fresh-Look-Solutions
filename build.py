import os

if not os.path.isdir("html/"):
    os.mkdir("html/")

for i in range(2, 12):
    os.system(f"pandoc -s latex/chapter_{i}/chapter_{i}.tex -c ../style.css -o html/chapter_{i}.html")
