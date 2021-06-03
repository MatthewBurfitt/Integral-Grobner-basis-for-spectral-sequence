# Overview

Library of functions for polynomial arithmetic and computing integral Grobner basis, incuding Grobner basis of the intersections of two ideals and the Grobner basis of Syzygys. In addtion, the polynomials used to provide any Grobner basis interms of the orginal ideal genraotrs can be tracked and returned. If ideal generators are homogenious polynomials, then computations can be restricted to a maximal degree (or dgrees within a partiton of the varaibles).

The code accompanies the paper: Matthew Burfitt, Jelena Grbic "The cohomology of free loop spaces of <img src="https://render.githubusercontent.com/render/math?math=SU(n %2B 1)/T^n">" and the libray includes everything needed to be applied to computations with certian Leray-Serre spectral sequences. All code providing computational results presented in the paper are given as exaples.

# Installation

Place a copy of "IntagralGrobner.py" in your python path, nothing else required other than Python 3.

# Usage

## Example

```python
import IntagralGrobner as G
```

## Reference manual

### Polynomial operations




### Polynomial display functions

#### poly_to_text()
    
Returns a string representation of a given fist input polynomial in varables given as a list of strings with teh same leght as the number of polynomial varaible as the second input.


### Grobner bais functions


