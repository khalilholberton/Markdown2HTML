#!/usr/bin/python3
"""
This module conatins Markdown
"""
import os
import sys


def Markdown():
    """Markdown function"""
    try:
        if len(sys.argv) != 3:
            print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
            exit(1)
            if not os.path.isfile(sys.argv[1]):
                print("Missing {}".format(sys.argv[1]), file=sys.stderr)
                exit(1)
        try:
            with open(sys.argv[1], 'r') as b:
                for mystring in b:
                    if '#' in mystring:
                        token = mystring.count("#")
                        text = mystring.strip('#\n')
                        text = text.lstrip()
                        page = "<h{}>{}</h{}>".format(token, text, token)
                        code = ""
                        code += page + '\n'
        except Exception:
            pass
        code = code.rstrip()
        with open(sys.argv[2], 'w') as a:
            a.write(code)
            sys.exit(0)
    except Exception:
        pass

if __name__ == "__main__":
    Markdown()
