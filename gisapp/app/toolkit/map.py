# Import builtins
import time
# Import GUI libraries
import tkinter as tk
# Import internals
from .popups import popup_message
from .. import icons
# Import GIS functionality
import gisapp as pg
from . import dispatch
# Import style
from . import theme
style_map_normal = {"bg": theme.color1}
class MapView(tk.Canvas):
    def __init__(self, master, **kwargs):
        # get theme style
        style = style_map_normal.copy()
        style.update(kwargs)
        # Make this class a subclass of tk.Canvas and add to it
        tk.Canvas.__init__(self, master, **style)
        # Other
        self.proj = kwargs.get("projection", "WGS84")
        self.statusbar = None
        self.mousepressed = False
        self.mouse_mode = "pan"
        self.zoomcenter = None
        self.zoomfactor = 1
        self.zoomdir = None
        self.last_zoomed = None
    def assign_statusbar(self, statusbar):
        statusbar.mapview = self
        self.statusbar = statusbar
