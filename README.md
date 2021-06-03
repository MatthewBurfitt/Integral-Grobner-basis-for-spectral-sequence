# Table of Contents

1. [Overview](#Overview)  
2. [Installation](#Installation)  
3. [Usage](#Usage)
      1. [Example](#Example)
      2. [Reference manual](#Reference &nbsp; manual)

# Overview

Library of functions for polynomial arithmetic and computing integral Grobner basis, incuding Grobner basis of the intersections of two ideals and the Grobner basis of Syzygys. In addtion, the polynomials used to provide any Grobner basis interms of the orginal ideal genraotrs can be tracked and returned. If ideal generators are homogenious polynomials, then computations can be restricted to a maximal degree (or dgrees within a partiton of the varaibles).

The code accompanies the paper: Matthew Burfitt, Jelena Grbic "The cohomology of free loop spaces of <img src="https://render.githubusercontent.com/render/math?math=SU(n %2B 1)/T^n">" and the libray includes everything needed to be applied to computations with certian Leray-Serre spectral sequences. All code providing computational results presented in the paper are given as exaples.

# Installation

Place a copy of "IntagralGrobner.py" in your python path, nothing else required other than Python 3.

# Usage

Load the *IntagralGrobner* libray.

```python
import IntagralGrobner as G
```

## Example

Terms are represented as a list of lenght two the fist entry is the scaler constant (an integer) and the second a lsit (of integer) poweres of varaibles in the term.
A *polynomial* is a list of terms with the same number of varaibles.
We represent the polynomial <img src="https://render.githubusercontent.com/render/math?math=x^2 %2B 2xy - 3y^2"> as followes.

```python
#define a polynomila x^2+2xy-3y^2
polynomial = [ [1, [2,0]], [2, [1,1]], [-3, [0,2]] ]

#display the polynomial
print(G.poly_to_text(polynomial, ['x', 'y']))
```

Basic polynomial operations such as evaluation, negation, addtion and multiplication can be applied to polynomials.

```python
#define a list of symetric polynomials
polys=[
      [ [1, [2,0,0]], [1, [0,2,0]], [1, [0,0,2]], [1, [1,1,0]], [1, [1,0,1]], [1, [0,1,1]] ],
      [ [1, [1,0,0]], [1, [0,1,0]], [1, [0,0,1]] ],
      [ [1, [3,0,0]], [1, [0,3,0]], [1, [0,0,3]], [1, [2,1,0]], [1, [2,0,1]], [1, [1,2,0]], [1, [0,2,1]], [1, [1,0,2]], [1, [0,1,2]], [1, [1,1,1]] ]
      ]
 
#display the polynomial list
G.display_poly_list(polys, ['x', 'y', 'z'])

#sort polynomials by lexagrphic ordering on varaibles and enumerated list disaplay
sorted_poly = G.sort_poly(polys[0])
print(G.poly_to_text(sorted_poly, ['x', 'y', 'z']))
sorted_polys = G.sort_poly_list(polys)
G.display_poly_list_numbered(sorted_polys, ['x', 'y', 'z'])

#evaluate or partialy evaluate a polynomial on variables
fully_evaluated_poly = G.eval_poly(polys[0], [1,2,3])
print(fully_evaluated_poly)
partialy_evaluated_poly1 = G.eval_poly(polys[0], [0,None,None])
print(G.poly_to_text(partialy_evaluated_poly1, ['y', 'z']))
partialy_evaluated_poly2 = G.eval_poly(polys[0], [0,None,None], keep_varaible_positions = True)
print(G.poly_to_text(partialy_evaluated_poly2, ['x', 'y', 'z']))

#polynomial arithmetic
new_poly = G.add_poly(G.mult_poly(polys[1], polys[1]), G.neg_poly(polys[0]))
print(G.poly_to_text(new_poly, ['x', 'y', 'z']))
x = [[2, [1,0,0]]]
new_poly_list = G.mult_list(x, polys)
G.display_poly_list_numbered(new_poly_list, ['x', 'y', 'z'])
```

For the purpose of Grobner basis comutatiosn, we treat a list of polynomials as the gnerators of an ideal.

```python

```

More exaples form the paper that the libray accompanies can be found in the *'Examples'* folder.

## Reference manual

### Polynomial operations

#### &#x1F539; eval_poly()

---

#### &#x1F539; neg_poly()

---

#### &#x1F539; add_poly()

---

#### &#x1F539; mult_poly()

---

#### &#x1F539; mult_list()

---

#### &#x1F539; sort_poly(poly_to_sort)

---

#### &#x1F539; sort_poly_list(poly_list_to_sort, sort_with = None)

---


### Polynomial display functions

#### &#x1F539; poly_to_text(poly, varaibles)

  Returns a string representation of a given polynomial in polynomial varables of a list of strings with the same lenght as the number of polynomial varaibles.

  |  | Variable | Description |
  | ------------ | ------------- | ------------- |
  | **Parameters:** | **poly** | A polynomial. |
  | | **varaibles** | List of strings of the same lenght as the number of polynomial varaibles each string represeting the chrecter(s) to be used to display the varaible at the given poistion in the list. |
  | **Returns:** | | A string represtation of the polynomial. |

---

#### &#x1F539; display_poly_list(poly_list, varaibles)

  Prints a representation of a given list of polynomials (with same nubmer of varaibles) on separate lines with polynomial varable representations given as a list of strings with the same lenght as the number of polynomial varaibles.

  |  | Variable | Description |
  | ------------ | ------------- | ------------- |
  | **Parameters:** | **poly_list** | A list of polynomials. |
  | | **varaibles** | List of strings of the same lenght as the number of polynomial varaibles each string represeting the chrecter(s) to be used to display the varaible at the given poistion in the list. |

---

#### &#x1F539; display_poly_list_numbered(poly_list, varaibles)

  Prints a representation of a given list of polynomials (with same nubmer of varaibles) each polynomial numbered by list position on separate lines with polynomial varable representations given as a list of strings with the same lenght as the number of polynomial varaibles.

  |  | Variable | Description |
  | ------------ | ------------- | ------------- |
  | **Parameters:** | **poly_list** | A list of polynomials. |
  | | **varaibles** | List of strings of the same lenght as the number of polynomial varaibles each string represeting the chrecter(s) to be used to display the varaible at the given poistion in the list. |

---

#### &#x1F539; display_poly_list_list_numbered(poly_list_list, varaibles)

  Prints a representation of a given list of polynomials (with same nubmer of varaibles) in a list each polynomial numbered by list position on separate lines. Polynomials are rperesented in varables given as a list of strings with the same lenght as the number of polynomial varaibles.

  |  | Variable | Description |
  | ------------ | ------------- | ------------- |
  | **Parameters:** | **poly_list_list** | A list of lsits of polynomials. |
  | | **varaibles** | List of strings of the same lenght as the number of polynomial varaibles each string represeting the chrecter(s) to be used to display the varaible at the given poistion in the list. |

---

### Grobner basis functions

#### &#x1F539; reduce()

---

#### &#x1F539; full_reduce()

---

#### &#x1F539; list_reduce()

---

#### &#x1F539; list_reduce_tracking()

---

#### &#x1F539; reduce_list()

---

#### &#x1F539; reduce_list_tracking()

---

#### &#x1F539; S_poly()

---

#### &#x1F539; G_poly()

---

#### &#x1F539; grobner()

---

#### &#x1F539; grobner_tracking()

---

#### &#x1F539; intersection_Grobner()

---

#### &#x1F539; Syzygy()

---
