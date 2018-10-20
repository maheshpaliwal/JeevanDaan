# Import GUI functionality
import tkinter as tk
from tkinter.filedialog import askopenfilenames, asksaveasfilename
# Import internals
from .buttons import *
from .popups import *
# Import style
from . import theme
style_layerspane_normal = {"bg": theme.color4,
                           "width": 200}
style_layersheader = {"bg": theme.color2,
                      "font": theme.titlefont1["type"],
                      "fg": theme.titlefont1["color"],
                      "anchor": "w", "padx": 5}
style_layeritem_normal = {"bg": theme.color4,
                          "width": 200,
                          "relief": "ridge"}
style_layercheck = {"bg": theme.color4}
style_layername_normal = {"bg": theme.color4,
                          "fg": theme.font1["color"],
                          "font": theme.font1["type"],
                          "relief": "flat",
                          "anchor": "w"}
# Import GIS functionality
import gisapp as pg
from . import dispatch
class LayersPane(tk.Frame):
    def __init__(self, master, layer_rightclick=None, **kwargs):
        # get theme style
        style = style_layerspane_normal.copy()
        style.update(kwargs)
        # Make this class a subclass of tk.Frame and add to it
        tk.Frame.__init__(self, master, **style)
        # Make the top header
        self.header = tk.Label(self, text="Layers:", **style_layersheader)
        self.header.pack(side="top", fill="x")
        # Then, the layer list view
        self.layersview = tk.Frame(self, **style)
        self.layersview.pack(side="top", fill="x")
        self.pack_propagate(False)
    def assign_statusbar(self, statusbar):
        statusbar.mapview = self
        self.statusbar = statusbar
