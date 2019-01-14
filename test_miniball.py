#
# Copyright (c) 2019 Alexandre Devert
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import numpy
import miniball



def test_bounding_ball_contains_point_set():
	# Check that the computed bounding ball contains all the input points
	for n in range(1, 10):
		for count in range(2, n + 10):
			# Generate points
			S = numpy.random.randn(count, n)

			# Get the bounding sphere
			C, r2 = miniball.get_bounding_ball(S)

			# Check that all points are inside the bounding sphere up to machine precision
			assert numpy.all(numpy.sum((S - C) ** 2, axis = 1) - r2 < 1e-12)



def test_bounding_ball_optimality():
	# Check that the bounding ball are optimal
	for n in range(2, 10):
		for count in range(n + 2, n + 30):
			# Generate a support sphere from n+1 points
			S_support = numpy.random.randn(n + 1, n)
			C_support, r2_support = miniball.get_bounding_ball(S_support)
			
			# Generate points inside the support sphere
			S = numpy.random.randn(count - S_support.shape[0], n)
			S /= numpy.sqrt(numpy.sum(S ** 2, axis = 1))[:,None]
			S *= ((.9 * numpy.sqrt(r2_support)) * numpy.random.rand(count - S_support.shape[0], 1))
			S = S + C_support
				
			# Get the bounding sphere
			C, r2 = miniball.get_bounding_ball(numpy.concatenate([S, S_support], axis = 0))

			# Check that the bounding sphere and the support sphere are equivalent
			# up to machine precision.
			assert numpy.allclose(r2, r2_support)
			assert numpy.allclose(C, C_support)


