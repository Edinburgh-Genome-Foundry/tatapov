from functools import lru_cache
import itertools
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


def is_palyndromic(overhang):
    return overhang == reverse_complement(overhang)


all_overhangs = ["".join(o) for o in itertools.product(*(4 * ["ACGT"]))]


def list_overhangs(standard_overhangs_only=False, non_palyndromic=True):
    overhangs = all_overhangs
    if standard_overhangs_only:
        overhangs = sorted(set(standardize_overhang(o) for o in overhangs))
    if non_palyndromic:
        overhangs = [o for o in overhangs if not is_palyndromic(o)]
    return overhangs


def data_subset(dataframe, overhangs, add_reverse=True):
    """
    Restrict a Tatapov dataframe to a set of overhangs.

    Parameters
    ----------
    dataframe : DataFrame
        One of the data sheets provided by Tatapov, e.g.
        ``annealing_data["37C"]["01h"]``.
    overhangs : list
        List of overhangs.
    add_reverse : bool
        If True (recommended), the reverse-complements of the overhangs in the
        provided list will also be kept.
    """
    overhangs = list(overhangs)
    if add_reverse:
        reverses = [reverse_complement(o) for o in overhangs]
        all_overhangs = sum(zip(overhangs, reverses), ())
        overhangs = uniquify_list(all_overhangs)
    return dataframe[overhangs].loc[overhangs]


def plot_data(df, ax=None, colorbar=True, figwidth=None, plot_color="Blues"):
    """
    Plot a (restricted) Tatapov dataframe. Requires matplotlib installed.

    Parameters
    ----------
    df : DataFrame
        One of the data sheets provided by Tatapov, e.g.
        ``annealing_data["37C"]["01h"]``. Or a restriction using ``data_subset``.
    ax : matplotlib.axes.Axes, optional
        A Matplotlib ax. If none is provided, one will be created and returned
        at the end.
    colorbar : bool
        If True, the figure will have a colorbar.
    figwidth : float
        Custom width of the figure (which will be square shaped).
    plot_color : str
        A Matplotlib colormap name.
    """

    if not MATPLOTLIB_AVAILABLE:
        raise ImportError("Install matplotlib to use this method.")
    if ax is None:
        _, ax = plt.subplots(1, figsize=(figwidth, figwidth) if figwidth else None)
    values = np.log10(np.maximum(0.5, df.values[::-1]))
    im = ax.imshow(values, cmap=plot_color)
    if colorbar:
        ax.figure.colorbar(im, label="log10( occurrences )")
    for i in range(len(df)):
        ax.axhline(i, ls="--", alpha=0.3)
        ax.axvline(i, ls="--", alpha=0.3)

    xtick_labels = df.columns
    ax.set_xticks(range(len(xtick_labels)))
    ax.set_xticklabels(xtick_labels, rotation=90)
    ax.xaxis.tick_top()
    ax.set_xlim(right=len(xtick_labels) - 0.5)

    ytick_labels = df.index[::-1]
    ax.set_yticks(range(len(ytick_labels)))
    ax.set_yticklabels(ytick_labels)
    ax.set_ylim(-0.5, len(ytick_labels) - 0.5)
    return ax, im


def relative_self_annealings(
    annealing_data, standardize_overhangs=False, ignore_palyndroms=True
):
    overhangs = list_overhangs(
        standard_overhangs_only=standardize_overhangs, non_palyndromic=ignore_palyndroms
    )
    self_annealings = {
        oh: annealing_data[oh][reverse_complement(oh)] for oh in overhangs
    }
    max_self_annealing = 1.0 * max(self_annealings.values())
    for oh in self_annealings.keys():
        self_annealings[oh] /= max_self_annealing
    return self_annealings


def cross_annealing(annealing_data, overhangs):
    overhangs = list(overhangs) + [reverse_complement(o) for o in overhangs]
    self_annealings = 0
    cross_annealings = 0
    for oh1, oh2 in itertools.combinations(overhangs, 2):
        annealings = annealing_data[oh1][oh2]
        if oh1 == reverse_complement(oh2):
            self_annealings += annealings
        else:
            cross_annealings += annealings
    return cross_annealings / (self_annealings + cross_annealings)


def cross_annealings(annealing_data):
    overhangs = list_overhangs(standard_overhangs_only=False, non_palyndromic=True)
    result = {
        overhangs_pair: cross_annealing(annealing_data, overhangs_pair)
        for overhangs_pair in itertools.combinations(overhangs, 2)
    }
    for (o1, o2), value in list(result.items()):
        result[(o2, o1)] = value
    return result


def standardize_overhang(oh):
    return min(oh, reverse_complement(oh))


def standardize_overhang_pair(pair):
    oh1, oh2 = [standardize_overhang(o) for o in pair]
    return tuple(sorted([oh1, oh2]))
