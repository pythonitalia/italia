import webbrowser
import sys
import traceback

webbrowser.open("https://2025.pycon.it")


def itahook(*exc_info):
    lines = traceback.format_exception(*exc_info)
    lines[0] = lines[0].replace("Traceback", "🤌🤌🤌")
    last = lines[-1][:-1]  # last line, minus the "\n"
    lines[-1] = f"🤌 {last} 🤌\n"
    print("".join(lines))


sys.excepthook = itahook

if hasattr(sys, "italian"):

    def k():
        pass

    globals()["🤌"] = k

    stampa("Questo Python è italiano 🤌 🤌")
else:
    print("This is a boring python, not Italian 🤌")
