#! -*- utf-8 -*-
from plotly.offline import init_notebook_mode, plot, iplot
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import os

def gallon2liter(value):
    return 3.78541*value


def easy_plot(x_data, y_data, name, title, xlabel, ylabel, color=None, plotter='plotly'):
    """Simplify plotting syntax by doing everything with one function call.
    
    Args:
        x_data (np.ndarray): list of lists with x_data
        y_data (np.ndarray): list of lists with y_data
        y_size (list): list of booleans with the same length as y_data; 'left', 'right'
    
    Returns:
        obj: plotted object based on plotte chosen
    """
    if not isinstance(x_data, np.ndarray):
        x_data = np.array(x_data)
    if not isinstance(y_data, np.ndarray):
        y_data = np.array(y_data)

    assert x_data.shape == y_data.shape
    
    x_data = np.atleast_1d(x_data)
    y_data = np.atleast_1d(y_data)
    
    if plotter == 'plotly':
        fig = _plot_with_plotly(x_data, y_data, name, color, xlabel, ylabel, title)
        return fig


def _plot_with_plotly(x_data, y_data, name, color, xlabel, ylabel, title):
    data = []
    if name and color:
        data.append(go.Scatter(x=x_data, y=y_data, marker=dict(color=color), name=name))
    elif name and not(color):
        data.append(go.Scatter(x=x_data, y=y_data, name=name))
    elif not(name) and color:
        data.append(go.Scatter(x=x_data, y=y_data, marker=dict(color=color)))
    else:
        raise Exception('Error: Data invalid')
    
    layout = dict(title=title, xaxis=dict(title=xlabel),
                  yaxis=dict(title=ylabel))

    return data, layout


def gallon2liter(value):
    return 3.78541*value