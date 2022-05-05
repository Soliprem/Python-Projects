# This is a script to automate adding entries to your Biber (or similar) bibliography list. Set the path to you file below
import os
# Path to your bib file
mybibfile = "/home/soliprem/latex-stuff/soli_list.bib"
custom = []

def decision():
    # global custom
    choice = input(" what next? Press:\n  e: edition\n  s: section/chapter\n  p: publisher\n  c: custom\n  q: quit\n:")
    if choice == "q":
        return
    elif choice == "e":
        custom.append("\n\tedition = " + "{" + input("edition: ") + "},")
        print("\n")
    elif choice == "s":
        custom.append("\n\tchapter = " + "{" + input("chapter/section: ") + "},")
        print("\n")
    elif choice == "p":
        custom.append("\n\tpublisher = " + "{" + input("publisher: ") + "},")
        print("\n")
    elif choice == "c":
        category = input(" category\n:")
        custom.append("\n\t"+ category + " = " + "{" + input(category+"\n:") + "},")
        print("\n")
    decision()

def write(file):
    with open(file, "a") as f:
        f.write(kind)
        f.write(tag)
        f.write(author)
        f.write(year)
        f.write(title)
        for i in custom:
            f.write(i)
        f.write("\n}")

kind = "\n@" + input("  type: ")
tag = "{" + input("  tag: ") + ","
author = "\n\tauthor" + " = {" + input("  author: ") + "},"
year = "\n\tyear" + " = {" + input("  year: ") + "},"
title = "\n\ttitle" + " = {" +  input("  title: ") + "},"
print("\n")

decision()

check = input("review entry? (y/n)\n:")
if check == "y":
    os.system("touch tempfile")
    write("tempfile")
    os.system("cat tempfile")
    os.system("rm tempfile")
    print("\n\n")

confirm = input("confirm? (y/n))\n:")
if confirm == "y":
    write(mybibfile)
