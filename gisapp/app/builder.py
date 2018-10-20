# Import builtins
import sys, os
import time
# Import GUI library
import tkinter as tk
# Import internals
from .toolkit import *
from .dialogues import *
# Import GIS functionality
import gisapp as pg
class GUI(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        # Place top ribbon area
        self.ribbon = Ribbon(self)
        self.ribbon.pack(side="top", fill="x")
        # Add tabs
        hometab = self.ribbon.add_tab("Home")
        # Set starting tab
        self.ribbon.switch(tabname="Home")
        # Place main middle area
        middle_area = tk.Frame(self)
        middle_area.pack(side="top", expand=True, fill="both")
        # Layers pane on left
        self.layerspane = LayersPane(middle_area)
        self.layerspane.pack(side="left", fill="y")
        # Mapwidget on right
        self.mapview = MapView(middle_area)
        self.mapview.pack(side="left", fill="both", expand=True)
        # Place bottom info and mouse coords bar at bottom
        self.statusbar = StatusBar(self, height=20, width=100)
        self.statusbar.pack(side="bottom", fill="x")
        # Assign statusbar to widgets that perform actions
        self.mapview.assign_statusbar(self.statusbar)
        self.layerspane.assign_statusbar(self.statusbar)
def run():
    # create main window
    window = tk.Tk()
    window.wm_title("Python GIS")
    try: # windows and mac
        window.wm_state('zoomed')
    except: # linux
        window.wm_attributes("-zoomed", "1")
    # pack in the GUI frame
    gui = GUI(window)
    gui.place(relwidth=1, relheight=1)
    # open the window
    window.mainloop()
