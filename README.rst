Tatapov
--------

.. image:: https://travis-ci.org/Edinburgh-Genome-Foundry/tatapov.svg?branch=master
   :target: https://travis-ci.org/Edinburgh-Genome-Foundry/tatapov
   :alt: Travis CI build status

Tatapov is a library making accessible and explorable misannealing data from the
following paper.


The Supplementary Material provides tables of inter-overhang annealing data in
various 4 conditions (01h or 18h icubations at 25C or 37C). Tatapov provides



.. code:: python

  data = tatapov.annealing_data["25C"]["01h"]
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

Tatapov is an open-source software originally written at the Edinburgh Genome Foundry by `Zulko <https://github.com/Zulko>`_ and `released on Github <https://github.com/Edinburgh-Genome-Foundry/Primavera>`_ under the MIT licence (¢ Edinburg Genome Foundry). Everyone is welcome to contribute !

More biology software
-----------------------

.. image:: https://raw.githubusercontent.com/Edinburgh-Genome-Foundry/Edinburgh-Genome-Foundry.github.io/master/static/imgs/logos/egf-codon-horizontal.png
 :target: https://edinburgh-genome-foundry.github.io/

Saboteurs is part of the `EGF Codons <https://edinburgh-genome-foundry.github.io/>`_ synthetic biology software suite for DNA design, manufacturing and validation.
