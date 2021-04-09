try:
    import Tkinter
except ImportError:
    import tkinter as Tkinter

print(Tkinter.TkVersion)
print(Tkinter.TclVersion)

Tkinter._test()
