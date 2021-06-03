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

#### eval_poly()

---

#### neg_poly()

---

#### add_poly()

---

#### mult_poly()

---

#### mult_list()

---

### Polynomial display functions

#### &#x1F53B; poly_to_text(poly, varaibles)

  Returns a string representation of a given polynomial in polynomial varables of a list of strings with the same lenght as the number of polynomial varaibles.

  |  | Variable | Description |
  | ------------ | ------------- | ------------- |
  | **Parameters:** | **poly** | A polynomial. |
  | | **varaibles** | List of strings of the same lenght as the number of polynomial varaibles each string represeting the chrecter(s) to be used to display the varaible at the given poistion in the list. |
  | **Returns:** | | A string represtation of the polynomial. |

---

#### display_poly_list(poly_list, varaibles)

  Prints a representation of a given list of polynomials (with same nubmer of varaibles) on separate lines with polynomial varable representations given as a list of strings with the same lenght as the number of polynomial varaibles.

  |  | Variable | Description |
  | ------------ | ------------- | ------------- |
  | **Parameters:** | **poly_list** | A list of polynomials. |
  | | **varaibles** | List of strings of the same lenght as the number of polynomial varaibles each string represeting the chrecter(s) to be used to display the varaible at the given poistion in the list. |

---

#### display_poly_list_numbered(poly_list, varaibles)

  Prints a representation of a given list of polynomials (with same nubmer of varaibles) each polynomial numbered by list position on separate lines with polynomial varable representations given as a list of strings with the same lenght as the number of polynomial varaibles.

  |  | Variable | Description |
  | ------------ | ------------- | ------------- |
  | **Parameters:** | **poly_list** | A list of polynomials. |
  | | **varaibles** | List of strings of the same lenght as the number of polynomial varaibles each string represeting the chrecter(s) to be used to display the varaible at the given poistion in the list. |

---

#### display_poly_list_list_numbered(poly_list_list, varaibles)

  Prints a representation of a given list of polynomials (with same nubmer of varaibles) in a list each polynomial numbered by list position on separate lines. Polynomials are rperesented in varables given as a list of strings with the same lenght as the number of polynomial varaibles.

  |  | Variable | Description |
  | ------------ | ------------- | ------------- |
  | **Parameters:** | **poly_list_list** | A list of lsits of polynomials. |
  | | **varaibles** | List of strings of the same lenght as the number of polynomial varaibles each string represeting the chrecter(s) to be used to display the varaible at the given poistion in the list. |

---

### Grobner basis functions

#### reduce()

#### full_reduce()

#### list_reduce()

#### list_reduce_tracking()

#### reduce_list()

#### reduce_list_tracking()

#### S_poly()

#### G_poly()

#### grobner()

#### grobner_tracking()

#### intersection_Grobner()

#### Syzygy()
