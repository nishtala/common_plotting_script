#!/usr/bin/env python3
# Rajiv Nishtala
# 25-07-2019. This is me sick and tired of playing with font sizes periodically for publications.

# Modified after Milans code and the link below.
#https://jwalton.info/Embed-Publication-Matplotlib-Latex/

import matplotlib as mpl
import matplotlib.pyplot as plt

def setup_fonts():
    plt.style.use('seaborn-paper')
    plt.style.context("seaborn-colorblind")

    linewidth = 0.5
    mpl.use("pgf")

    nice_fonts = {
            # Use LaTeX to write all text
            "text.usetex": True,
            "font.family": "sans-serif",
            # Use 10pt font in plots, to match 10pt font in document
            "axes.labelsize": 10,
            "font.size": 10,
            # Make the legend/label fonts a little smaller
            "legend.fontsize": 8,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "axes.linewidth": linewidth,
            "pgf.texsystem": "pdflatex",
            "pgf.rcfonts": False,
            "pgf.preamble": [
                r"\usepackage[utf8x]{inputenc}",
                r"\usepackage[T1]{fontenc}",
                r"\renewcommand{\rmdefault}{ptm}",
                r"\AtBeginDocument{\fontdimen2\font=2.8pt}",
                r"\AtBeginDocument{\fontdimen3\font=1.2pt}",
                r"\AtBeginDocument{\fontdimen4\font=0.96pt}",
                ],
            "axes.spines.right" : False,
            "axes.spines.top" : False,
            "savefig.dpi" : 500,
            "savefig.pad_inches" : 1e-4,
            "savefig.bbox" : "tight",
            "legend.framealpha": 0,
            "legend.fancybox": True
    }

    mpl.rcParams.update(nice_fonts)

#Fortunately, our function is easy to adapt. Simply add the default argument subplot=[1, 1]
#to the function definition. Along with this, you must change the line which calculates the
#figure height to fig_height_in = fig_width_in * golden_ratio * (subplot[0] / subplot[1]).
#We’d initialise a figure with 5 rows and 2 columns of axes as
#fig, ax = plt.subplots(5, 2, figsize=set_size(width, subplot=[5, 2])).

# No width is provided, it assumes default of sig-alternate
# gives the width of the current document in pts
#To obtain run this: \showthe\textwidth
#pt. --> Sig-alternate
width =  504.0
def set_size(width=width, fraction=1, subplot=[1, 1]):
    """ Set aesthetic figure dimensions to avoid scaling in latex.

    Parameters
    ----------
    width: float
            Width in pts
    fraction: float
            Fraction of the width which you wish the figure to occupy

    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    # Width of figure
    fig_width_pt = width * fraction

    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    golden_ratio = (5**.5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio * (subplot[0] / subplot[1])

    fig_dim = (fig_width_in, fig_height_in)

    return fig_dim
