Tatapov
-------

.. image:: https://travis-ci.org/Edinburgh-Genome-Foundry/tatapov.svg?branch=master
   :target: https://travis-ci.org/Edinburgh-Genome-Foundry/tatapov
   :alt: Travis CI build status

Tatapov is a Python library making accessible and easy to explore the DNA
overhang misannealing data from the following paper
(`available on arxiv <https://www.biorxiv.org/content/early/2018/05/15/322297>`_):

*Optimization of Golden Gate assembly through application of ligation
sequence-dependent fidelity and bias profiling*, Potapov Vladimir,
Jennifer L. Ong, Rebecca B. Kucera, Bradley W. Langhorst,
Katharina Bilotti, John M. Pryor, Eric J. Cantor, Barry Canton,
Thomas F. Knight, Thomas C. Evans Jr., Gregory Lohman. May 2018,
https://doi.org/10.1101/322297


The Supplementary Material of this paper provides tables of inter-overhang
annealing data in various 4 conditions (01h or 18h icubations at 25C or 37C).
Tatapov provides these tables (it will download them automatically from Arxiv
on the first use) as Pandas dataframes, so that they are easy to manipulate.

It also provides simple methods to build and plot subsets of the data (plotting
requires Matplotlib installed). 

Usage Example
-------------

.. code:: python

  data = tatapov.annealing_data["25C"]["01h"] # a pandas dataframe
  subset = tatapov.data_subset(data, ["ACGA", "AAAT", "AGAG"], add_reverse=True)
  ax, _ = tatapov.plot_data(subset, figwidth=5)
  ax.figure.tight_layout()
  ax.figure.savefig("example.png")

Installation
-------------

You can install Tatapov through PIP

.. code::

    sudo pip install tatapov

Alternatively, you can unzip the sources in a folder and type

.. code::

    sudo python setup.py install

License = MIT
--------------

Tatapov is an open-source software originally written at the Edinburgh Genome
Foundry by `Zulko <https://github.com/Zulko>`_ and
`released on Github <https://github.com/Edinburgh-Genome-Foundry/Primavera>`_
under the MIT licence (¢ Edinburg Genome Foundry). Everyone is welcome
to contribute !

Please contact us if there is any issue regarding copyright (there shouldn't be
as the repository does not contain any data, and the paper data is free to
download).

More biology software
-----------------------

.. image:: https://raw.githubusercontent.com/Edinburgh-Genome-Foundry/Edinburgh-Genome-Foundry.github.io/master/static/imgs/logos/egf-codon-horizontal.png
 :target: https://edinburgh-genome-foundry.github.io/

Tatapov is part of the `EGF Codons <https://edinburgh-genome-foundry.github.io/>`_ synthetic biology software suite for DNA design, manufacturing and validation.
