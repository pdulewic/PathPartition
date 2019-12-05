#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

class Path:
    def __init__(self, ID):
        self.pathID = ID
        self.segments = []
        self.numberOfSegments = 0

    def append(self, segment):
        self.segments.append(segment)
        self.numberOfSegments += 1

    def display(self, locator = 1):
        fig, ax = plt.subplots()
        ax.set_aspect('equal', 'box') 
        ax.grid(True)
        ax.xaxis.set_major_locator(ticker.MultipleLocator(locator))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(locator))

        for segment in self.segments:
            segment.draw(ax)

        ax.autoscale_view()
        plt.show()
