import webbrowser
import sys

webbrowser.open("https://2025.pycon.it")


if hasattr(sys, "italian"):

    def k():
        pass

    globals()["🤌"] = k

    stampa("Questo Python è italiano 🤌 🤌")
else:
    print("This is a boring python, not Italian 🤌")
