# -*- coding: utf-8 -*-
# ****************************************************
# Titresim ve Dalgalar ders notlarının
# Jupyter notebooklarında kullanılan ortak kütüphaneler.
# ****************************************************
from ipywidgets import interact, interactive, fixed, interact_manual, FloatSlider
from IPython.display import display, HTML, Markdown, YouTubeVideo
import matplotlib.ticker as tck
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import sympy as sym
import scipy
from scipy.io import wavfile
import datetime as dt

# matplotlib.colors
# https://matplotlib.org/api/colors_api.html
plt_colors =  ('b', 'g', 'r', 'c', 'm', 'y', 'k', 'w')

params = {
   'axes.titlesize': 24,
   'axes.labelsize': 18,
   'axes.labelweight': 'bold',
   'font.size': 16, 
   'legend.fontsize': 14,
   'xtick.labelsize': 16,
   'xtick.major.size': 10,
   'xtick.major.width': 1.4,
   'xtick.minor.size': 5,
   'xtick.minor.width': 1.4,
   'ytick.labelsize': 16,
   'ytick.major.size': 10,
   'ytick.major.width': 1.4,
   'ytick.minor.size': 5,
   'ytick.minor.width': 1.4,    
   'lines.linewidth': 1.6,
   'lines.markersize': 8,
   'text.usetex': False,
   'mathtext.fontset': 'stix' # \mathbf --> $\mathbf{\Theta_{cm}}$
   #'text.latex.preamble': r'\usepackage{amsmath}'
   #'figure.figsize': [2.5, 4.5]
}
mpl.rcParams.update(params)


# This is a wrapper that take a filename and publish an html <audio> tag to listen to it.
def wavPlayer(filepath):
    """ will display html 5 player for compatible browser

    Parameters :
    ------------
    filepath : relative filepath with respect to the notebook directory ( where the .ipynb are not cwd)
               of the file to play

    The browser need to know how to play wav through html5.

    there is no autoplay to prevent file playing when the browser opens
    """
    
    src = """
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>Simple Test</title>
    </head>
    
    <body>
    <audio controls="controls" style="width:600px" >
      <source src="files/%s?flush_cache=true" type="audio/wav" />
      Your browser does not support the audio element.
    </audio>
    %s
    </body>
    """%(filepath, filepath)
    display(HTML(src))

# LaTeX ifadelerini yazdırmak için
def prinTeX(text, label=ur'', number=ur'\nonumber'):
    if label==ur'': label = ur'label' + str(np.random.random()).replace('.','')
    MarkdownText = \
    ur"""\begin{{align}}
         \label{{{label}}}
         {text} {number}
         \end{{align}}
    """.format(text = text, label=label, number=number)
    display(Markdown(MarkdownText))

# sympy ifadelerini yazdırmak için
def printS(sympyObj, formatS=ur'{} = {}', label=ur'', number=ur'\nonumber'):
    sympyObjLatex = tuple([sym.latex(s) for s in sympyObj])
    prinTeX(formatS.format(*sympyObjLatex), number=number)
    

