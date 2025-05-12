import tkinter

from Browser import Browser
from Url import URL


if __name__ == "__main__":
    import sys
    Browser().load(URL(sys.argv[1]))
    tkinter.mainloop()