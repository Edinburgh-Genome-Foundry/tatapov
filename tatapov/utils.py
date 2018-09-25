import os
from functools import lru_cache
import pandas
import numpy as np

try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

def uniquify_list(l):
    return sorted(set(l), key=l.index)

reverse_dict = dict(zip("ATGC", "TACG"))

@lru_cache(maxsize=300)
def reverse_complement(seq):
    return "".join([reverse_dict[e] for e in seq[::-1]])

def data_subset(dataframe, overhangs, add_reverse=True):
    """Restrict a tatapov dataframe to a set of overhangs.

    Parameters
    ----------

    dataframe
      One of the data sheets provided by tatapov, e.g.
      ``annealing_data["37C"]["01h"]``.
    
    overhangs
      list of overhangs
    
    add_reverse
      If True (recommended), the reverse-complements of the overhangs in the
      provided list will also be kept.
    """
    overhangs = list(overhangs)
    if add_reverse:
        reverses = [reverse_complement(o) for o in overhangs]
        all_overhangs = sum(zip(overhangs, reverses), ())
        overhangs = uniquify_list(all_overhangs)
    return dataframe[overhangs].loc[overhangs]

def plot_data(df, ax=None, colorbar=True, figwidth=None):
    """Plot a (restricted) tatapov dataframe. Requires matplotlib installed.

    Parameters
    ----------

    df
      One of the data sheets provided by tatapov, e.g.
      ``annealing_data["37C"]["01h"]``. Or a restriction using ``data_subset``
    
    ax
      A Matplotlib ax. If none is provided, one will be created and returned
      at the end
    
    colorbar
      If True, the figure will have a colorbar
    
    figwidth
      Custom width of the figure (which will be square shaped).
    """
    if not MATPLOTLIB_AVAILABLE:
        raise ImportError("Install matplotlib to use this method.")
    if ax is None:
        _, ax = plt.subplots(
            1, figsize=(figwidth, figwidth) if figwidth else None)
    values = np.log10(np.maximum(0.5, df.values[::-1]))
    im = ax.imshow(values, cmap='Blues')
    if colorbar:
        ax.figure.colorbar(im, label="log10( occurences )")
    for i in range(len(df)):
        ax.axhline(i, ls='--', alpha=0.3)
        ax.axvline(i, ls='--', alpha=0.3)
        
    xtick_labels = df.columns
    ax.set_xticks(range(len(xtick_labels) + 1))
    ax.set_xticklabels(xtick_labels, rotation=90)
    ax.xaxis.tick_top()
    ax.set_xlim(xmax=len(xtick_labels) - .5)
    
    ytick_labels = df.index[::-1]
    ax.set_yticks(range(len(ytick_labels) + 1))
    ax.set_yticklabels(ytick_labels)
    ax.set_ylim(-.5, len(ytick_labels) - .5)
    return ax, im