OpenCMISS Maths
===============

OpenCMISS Maths is a Python package containing math utility functions.
These utility functions are general utilities commonly used by downstream packages.

This package provides two modules

#. vectorops
#. algorithms

These modules are surfaced under the namespace package *opencmiss* within the *maths* package.
To use these modules the following import statement can be used::

  import opencmiss.maths.vectorops
  import opencmiss.maths.algorithms

Vector Operations
-----------------

The *vectorops* module is a collection of functions that operate on python lists as if they were vectors.
A basic implementation to forgo the need to use numpy.

Algorithms
----------

The *algorithms* module is a collection of functions that perform calculations on python lists.
These functions are commonly used in other OpenCMISS packages.

Package API
-----------

Vector Operations Module
************************

.. automodule:: opencmiss.maths.vectorops
   :members:
   :exclude-members: eulerToRotationMatrix3, axisAngleToQuaternion, axisAngleToRotationMatrix, matrixmult, mxconstantmult, vectormatrixmult, vectormxmult, rotmx, rotationMatrix3ToEuler, mxmult, mxconstantmult, mxvectormult

Algorithms Module
*****************

.. automodule:: opencmiss.maths.algorithms
   :members:
