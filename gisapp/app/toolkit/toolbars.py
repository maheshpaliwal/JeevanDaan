# Import GUI
import tkinter as tk
# Import internals
from .buttons import *
from .popups import *
# Import style
from . import theme
style_toolbar_normal = {"bg": theme.color4}
style_namelabel_normal = {"bg": theme.color4,
                          "font": theme.font2["type"],
                          "fg": theme.font2["color"],
                          "pady": 0}
class Toolbar(tk.Frame):
    def __init__(self, master, toolbarname, **kwargs):
        # get theme style
        style = style_toolbar_normal.copy()
        style.update(kwargs)
        # Make this class a subclass of tk.Frame and add to it
        tk.Frame.__init__(self, master, **style)
        # Divide into button area and toolbar name
        self.buttonframe = tk.Frame(self, **style)
        self.buttonframe.pack(side="top", fill="y", expand=True)
        self.name_label = tk.Label(self, **style_namelabel_normal)
        self.name_label["text"] = toolbarname
        self.name_label.pack(side="bottom")
    def add_button(self, icon=None, **kwargs):
        button = IconButton(self.buttonframe)
        options = {"text":"", "width":48, "height":32, "compound":"top"}
        options.update(kwargs)
        if icon:
            button.set_icon(icon, **options)
        else:
            button.config(**options)
        button.pack(side="left", padx=2, pady=0, anchor="center")
        return button
            
