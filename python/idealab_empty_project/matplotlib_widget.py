# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 08:20:22 2019

@author: daukes
"""

import qt
import qt.QtCore as qc
import qt.QtGui as qg
import matplotlib
import matplotlib.pyplot as plt
plt.ion()
matplotlib.rcParams['backend.qt5']=qt.loaded
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
#import numpy


class GraphView(qg.QWidget):
    def __init__(self, name='Name', title='Title', graph_title='Graph Title', parent = None):
        super(GraphView, self).__init__(parent)

        self.name = name
        self.graph_title = graph_title

        self.dpi = 100
        self.fig = Figure((5.0, 3.0), dpi = self.dpi, facecolor = (1,1,1), edgecolor = (0,0,0))
        self.axes = self.fig.add_subplot(111)
        
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)
        self.toolbar = NavigationToolbar(self.canvas,self)
        self.layout = qg.QVBoxLayout()
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.canvas)
        self.layout.setStretchFactor(self.canvas, 1)
        self.setLayout(self.layout)
        self.canvas.show()

    def clear(self):
        self.axes.clear()
    def plot(self,*args,**kwargs):
        self.axes.plot(*args,**kwargs)
    def draw(self):
        self.canvas.draw()
    def add_patch(self,patch):
        self.axes.add_patch(patch)
    def scatter(self,*args,**kwargs):
        self.axes.scatter(*args,**kwargs)
    def text(self,*args,**kwargs):
        self.axes.text(*args,**kwargs)


if __name__=='__main__':
    pass