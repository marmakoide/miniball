#
# Copyright (c) 2019-2021 Alexandre Devert
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the 'Software'), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from setuptools import setup


miniball_classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Topic :: Scientific/Engineering :: Mathematics",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
]


"""
Load the version identifier
"""

miniball_version = None
with open("miniball.py", "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith("__version__"):
            miniball_version = line.split("=")[1].strip().strip("\"'")
            break


"""
Load the package description
"""
with open("README.rst", "r") as f:
    miniball_long_description = f.read()


"""
Main setup
"""

setup(
    name="miniball",
    version=miniball_version,
    author="Alexandre Devert",
    author_email="marmakoide@hotmail.fr",
    url="https://github.com/marmakoide/miniball",
    install_requires=["numpy>=1.17"],
    tests_require=["pytest"],
    py_modules=["miniball"],
    description="Efficiently computes the smallest bounding ball of a point set, in arbitrary number of dimensions.",
    long_description=miniball_long_description,
    license="MIT",
    classifiers=miniball_classifiers,
    python_requires=">=3.5",
)
