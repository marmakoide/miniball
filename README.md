# miniball
A Python module to efficiently compute the smallest bounding ball of a point 
set, in arbitrary number of dimensions.

## Implementation notes

The algorithm implemented is Welzl's algorithm. It is a pure Python implementation,
it is not a binding of the popular C++ package [miniball](https://people.inf.ethz.ch/gaertner/subdir/software/miniball.html)

The algorithm, although often presented in its recursive form, is here implemented
in an iterative fashion. Python have an hard-coded recursion limit, therefore
a recursive implementation of Welzl's algorithm would have an artificially limited
number of point it could process.

## Authors

* **Alexandre Devert** - *Initial work* - [marmakoide](https://github.com/marmakoide)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


