.. image:: https://img.shields.io/pypi/v/miniball.svg
   :target: https://pypi.org/project/miniball/
   :alt: miniball on PyPI

.. image:: https://travis-ci.com/marmakoide/miniball.svg?branch=master
   :target: https://travis-ci.com/marmakoide/miniball
   :alt: miniball on TravisCI
   
.. image:: https://img.shields.io/badge/license-MIT-green.svg
   :target: https://github.com/marmakoide/miniball/blob/master/LICENSE
   :alt: MIT License badge

========
miniball
========

A Python module to efficiently compute the smallest bounding ball of a point 
set, in arbitrary number of dimensions.

The algorithm runs in approximatively linear time in respects to the number of
input points. This is NOT a derivative nor a port of 
`Bernd Gaertner's C++ library <https://people.inf.ethz.ch/gaertner/subdir/software/miniball.html>`__.

This project is licensed under the MIT License

Requirements
============

miniball 1.1 requires

* Python >= 3.5
* Numpy >= 1.17

Installation
============

.. code-block:: console

	$ pip install miniball


Usage
=====

Here is how you can get the smallest bounding ball of a set of points ``S``

.. code-block:: pycon

	>>> import numpy
	>>> import miniball
	>>> S = numpy.random.randn(100, 2)
	>>> C, r2 = miniball.get_bounding_ball(S)

The center of the bounding ball is ``C``, its radius is the square root of ``r2``. 
The input coordinates ``S`` can be integer, they will automatically cast to floating
point internally.

And that's it ! miniball does only one thing with one function.


Result accuracy
---------------

Although the algorithm returns exact results in theory, in practice it returns
result only exact up to a given precision. The ``epsilon`` keyword argument allows 
to control that precision, it is set to 1e-7 by default.

.. code-block:: pycon

	>>> import numpy
	>>> import miniball
	>>> S = numpy.random.randn(100, 2)
	>>> C, r2 = miniball.get_bounding_ball(S, epsilon=1e-7)


Repeatability
-------------

The algorithm to compute bounding balls relies on a pseudo-random number generator.
Although the algorithms return an exact solution, it is only exact up to the epsilon
parameter. As a consequence, running the ``get_bounding_ball`` function twice on 
the same input might not return exactly the same output.

By default, each call to ``get_bounding_ball`` pull out a new, freshly seeded 
pseudo-random number generator. Therefore, if you wish to get repeatable results 
from ``get_bounding_ball``, you have to (and only have to) pass the same pseudo-random 
number generator, using with the ``rng`` keyword argument

.. code-block:: pycon

	>>> import numpy
	>>> import miniball	
	>>> S = numpy.random.randn(100, 2)	
	>>> rng = numpy.random.RandomState(42)
	>>> C, r2 = miniball.get_bounding_ball(S, rng = rng)


Implementation notes
====================

The algorithm implemented is Welzl's algorithm. It is a pure Python implementation,
it is not a binding of the popular C++ package `Bernd Gaertner's miniball <https://people.inf.ethz.ch/gaertner/subdir/software/miniball.html>`__.

The algorithm, although often presented in its recursive form, is here implemented
in an iterative fashion. Python have an hard-coded recursion limit, therefore
a recursive implementation of Welzl's algorithm would have an artificially limited
number of point it could process.

Authors
=======

* **Alexandre Devert** - *Initial work* - `marmakoide <https://github.com/marmakoide>`__

License
=======

This project is licensed under the MIT License - see the `LICENSE <LICENSE>`__ file for details
