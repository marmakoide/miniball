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
import random



__author__  = 'Alexandre Devert <marmakoide@hotmail.fr>'
__version__ = '1.0.2'



def get_circumsphere(S):
	"""
	Computes the circumsphere of a set of points

	Parameters
	----------
	S : (M, N) ndarray, where 1 <= M <= N + 1
		The input points

	Returns
	-------
	C, r2 : ((2) ndarray, float)
		The center and the squared radius of the circumsphere 
	"""

	U = S[1:] - S[0] 
	B = numpy.sqrt(numpy.sum(U ** 2, axis = 1))
	U /= B[:,None]
	C = numpy.dot(numpy.linalg.solve(numpy.inner(U, U), .5 * B), U)
	return C + S[0], numpy.sum(C ** 2)



def get_bounding_ball(S, epsilon = 1e-7):
	"""
	Computes the smallest bounding ball of a set of points

	Parameters
	----------
	S : (M, N) ndarray, where 1 <= M <= N + 1
		The input points

	epsilon : float
		Tolerance used when testing if a set of point belongs to the same sphere.
		Default is 1e-7

	Returns
	-------
	C, r2 : ((2) ndarray, float)
		The center and the squared radius of the circumsphere 
	"""

	# Iterative implementation of Welzl's algorithm, see
	# "Smallest enclosing disks (balls and ellipsoids)" Emo Welzl 1991

	def circle_contains(D, p):
		c, r2 = D
		return numpy.sum((p - c) ** 2) <= r2

	def get_boundary(R):
		if len(R) == 0:
			return numpy.zeros(S.shape[1]), 0.

		if len(R) <= S.shape[1] + 1:
			return get_circumsphere(S[R])

		c, r2 = get_circumsphere(S[R[:S.shape[1] + 1]])
		if numpy.all(numpy.fabs(numpy.sum((S[R] - c) ** 2, axis = 1) - r2) < epsilon):
				return c, r2

	class Node(object):
		def __init__(self, P, R):
			self.P = P
			self.R = R
			self.D = None
			self.pivot = None
			self.left = None
			self.right = None

	def traverse(node):
		stack = [node]
		while len(stack) > 0:
			node = stack.pop()

			if len(node.P) == 0 or len(node.R) >= S.shape[1] + 1:
				node.D = get_boundary(node.R)
			elif node.left is None:
				node.pivot = random.choice(node.P)			 
				node.left = Node(list(set(node.P) - set([node.pivot])), node.R) 		
				stack.extend((node, node.left))
			elif node.right is None:
				if circle_contains(node.left.D, S[node.pivot]):
					node.D = node.left.D
				else:
					node.right = Node(node.left.P, node.R + [node.pivot])
					stack.extend((node, node.right))
			else:
				node.D = node.right.D
				node.left, node.right = None, None

	root = Node(range(S.shape[0]), [])
	traverse(root)	
	return root.D

