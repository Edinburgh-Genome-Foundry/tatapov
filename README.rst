.. raw:: html

    <p align="center">
    <img alt="tatapov logo" title="tatapov" src="https://raw.githubusercontent.com/Edinburgh-Genome-Foundry/tatapov/master/images/tatapov.png" width="140">
    </p>


Tatapov
-------

.. image:: https://github.com/Edinburgh-Genome-Foundry/tatapov/actions/workflows/build.yml/badge.svg
    :target: https://github.com/Edinburgh-Genome-Foundry/tatapov/actions/workflows/build.yml
    :alt: GitHub CI build status

.. image:: https://coveralls.io/repos/github/Edinburgh-Genome-Foundry/tatapov/badge.svg?branch=master
   :target: https://coveralls.io/github/Edinburgh-Genome-Foundry/tatapov?branch=master


Tatapov is a Python library (`API reference <https://edinburgh-genome-foundry.github.io/tatapov/>`_)
making accessible and easy to explore the DNA overhang misannealing data from
Potapov et al. (2018, `ACS Synth. Biol. <https://pubs.acs.org/doi/10.1021/acssynbio.8b00333>`_)
and Pryor et al. (2020, `PLoS ONE <https://doi.org/10.1371/journal.pone.0238592>`_):

*Comprehensive Profiling of Four Base Overhang Ligation Fidelity by T4 DNA Ligase and
Application to DNA Assembly.* Vladimir Potapov,
Jennifer L. Ong, Rebecca B. Kucera, Bradley W. Langhorst,
Katharina Bilotti, John M. Pryor, Eric J. Cantor, Barry Canton,
Thomas F. Knight, Thomas C. Evans Jr., Gregory Lohman.
ACS Synth. Biol. (2018) 7, 11, 2665–2674.


*Enabling one-pot Golden Gate assemblies of unprecedented complexity using
data-optimized assembly design.* John M. Pryor, Vladimir Potapov,
Rebecca B. Kucera, Katharina Bilotti, Eric J. Cantor, Gregory J. S. Lohman.
PLoS ONE (2020) 15(9): e0238592.


The Supplementary Material of these papers provide tables of inter-overhang
annealing data in various conditions (01h or 18h incubations at 25C or 37C).
Tatapov provides these tables (it will download them automatically
upon first use) as pandas dataframes, so that they are easy to manipulate.

It also provides simple methods to build and plot subsets of the data (plotting
requires Matplotlib installed).


Usage example
-------------

**Plotting**

.. code:: python

  import tatapov

  # Get a subset of the data at 25C (1h incubation)
  data = tatapov.annealing_data["25C"]["01h"]  # a pandas dataframe
  overhangs = ["ACGA", "AAAT", "AGAG"]
  subset = tatapov.data_subset(data, overhangs, add_reverse=True)

  # Plot the data subset
  ax, _ = tatapov.plot_data(subset, figwidth=5, plot_color="Blues")
  ax.figure.tight_layout()
  ax.figure.savefig("example.png")

.. image:: https://raw.githubusercontent.com/Edinburgh-Genome-Foundry/tatapov/master/images/tatapov_example.png

In the plot above, if you see anything else than the square pairs around the
diagonal, it means there is cross-talking between your overhangs (so risk of misannealing).
If one of these diagonal square pairs appears lighter than the others, it means that
the corresponding overhang has weak self-annealing (risk of having no assembly).
A color square in the diagonal means that the overhang can anneal with itself (palindromic).
The Matplotlib colormap is specified with the `plot_color` parameter.

The following datasets are available (see the publications for more details):

.. code:: python

  # Potapov 2018:
  tatapov.annealing_data[temperature][time]
  # where temperature is '25C' or '37C', and time is '01h' or '18h'

  # Pryor 2020 (all 01h):
  tatapov.annealing_data['37C'][enzyme]
  # where enzyme is one of:
  # '2020_01h_BsaI', '2020_01h_BsmBI', '2020_01h_Esp3I' or '2020_01h_BbsI'

**Identifying weak self-annealing overhangs**

.. code:: python

    import tatapov

    annealing_data = tatapov.annealing_data['37C']['01h']

    # Compute a dictionary {overhang: self-annealing score in 0-1}
    relative_self_annealing = tatapov.relative_self_annealings(annealing_data)

    weak_self_annealing_overhangs = [
        overhang
        for overhang, self_annealing in relative_self_annealing.items()
        if self_annealing < 0.4
    ]

**Identifying overhang pairs with significant cross-talking**

.. code:: python

    import tatapov

    annealing_data = tatapov.annealing_data['37C']['01h']

    # Compute a dictionary {overhang_pair: cross-talking score in 0-1}
    cross_annealings = tatapov.cross_annealings(annealing_data)

    high_cross_annealing_pairs = [
        overhang_pair
        for overhang_pair, cross_annealing in cross_annealings.items()
        if cross_annealing > 0.08
    ]


Installation
------------

You can install Tatapov through PIP:

.. code::

    pip install tatapov


License = MIT
-------------

Tatapov is an open-source software originally written at the Edinburgh Genome
Foundry by `Zulko <https://github.com/Zulko>`_ and
`released on Github <https://github.com/Edinburgh-Genome-Foundry/tatapov>`_
under the MIT licence (Copyright 2018 Edinburgh Genome Foundry, University of Edinburgh).


More biology software
---------------------

.. image:: https://raw.githubusercontent.com/Edinburgh-Genome-Foundry/Edinburgh-Genome-Foundry.github.io/master/static/imgs/logos/egf-codon-horizontal.png
  :target: https://edinburgh-genome-foundry.github.io/

Tatapov is part of the `EGF Codons <https://edinburgh-genome-foundry.github.io/>`_
synthetic biology software suite for DNA design, manufacturing and validation.
