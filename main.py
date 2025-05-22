import tkinter

from Browser import Browser
from HTMLParser import HTMLParser, print_tree
from Url import URL


if __name__ == "__main__":
    import sys
    body = URL(sys.argv[1]).request()
    nodes = HTMLParser(body).parse()
    print_tree(nodes)
    # Browser().load(URL(sys.argv[1]))
    # tkinter.mainloop()