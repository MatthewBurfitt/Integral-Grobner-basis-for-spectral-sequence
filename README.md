# Table of Contents

1. [Overview](#Overview)  
2. [Installation](#Installation)  
3. [Usage](#Usage)
      1. [Example](#Example)
      2. [Reference manual](#Reference%20manual)

# Overview

Library of functions for polynomial arithmetic and computing integral Gröbner bases, inducing Gröbner basis of the intersections of two ideals and the Gröbner basis of Syzygys. In addition, the polynomials used to provide any Gröbner basis in terms of the original ideal generators can be tracked and returned. If ideal generators are homogenous polynomials, then computations can be restricted to a maximal degree (or degrees within a partition of the variables).

The code accompanies the paper: Matthew Burfitt, Jelena Grbić "The cohomology of free loop spaces of <img src="https://render.githubusercontent.com/render/math?math=SU(n %2B 1)/T^n">" and the library includes everything needed to be applied to computations with certain Leray-Serre spectral sequences. All code providing computational results presented in the paper are given as examples.

# Installation

Place a copy of "IntagralGrobner.py" in your python path, nothing else required other than Python 3.

# Usage

Load the *IntagralGrobner* library.

```python
import IntagralGrobner as G
```

## Example

Terms are represented as a list of length two the fist entry is the scaler constant (an integer) and the second a list (of integer) powers of variables in the term.
A *polynomial* is a list of terms with the same number of variables.
We represent the polynomial <img src="https://render.githubusercontent.com/render/math?math=x^2 %2B 2xy - 3y^2"> as follows.

```python
#define a polynomial x^2+2xy-3y^2
polynomial = [ [1, [2,0]], [2, [1,1]], [-3, [0,2]] ]

#display the polynomial
print(G.poly_to_text(polynomial, ['x', 'y']))
```

Basic polynomial operations such as evaluation, negation, addition and multiplication can be applied to polynomials.

```python
#define a list of symmetric polynomials
polys=[
      [ [1, [2,0,0]], [1, [0,2,0]], [1, [0,0,2]], [1, [1,1,0]], [1, [1,0,1]], [1, [0,1,1]] ],
      [ [1, [1,0,0]], [1, [0,1,0]], [1, [0,0,1]] ],
      [ [1, [3,0,0]], [1, [0,3,0]], [1, [0,0,3]], [1, [2,1,0]], [1, [2,0,1]], [1, [1,2,0]], [1, [0,2,1]], [1, [1,0,2]], [1, [0,1,2]], [1, [1,1,1]] ]
      ]
 
#display the polynomial list
G.display_poly_list(polys, ['x', 'y', 'z'])

#sort polynomials by lexicographical ordering on variables and enumerated list display
sorted_poly = G.sort_poly(polys[0])
print(G.poly_to_text(sorted_poly, ['x', 'y', 'z']))
sorted_polys = G.sort_poly_list(polys)
G.display_poly_list_numbered(sorted_polys, ['x', 'y', 'z'])

#evaluate or partially evaluate a polynomial on variables
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

For the purpose of Gröbner basis computations, we treat a list of polynomials as the generators of an ideal.

```python

#a list of symmetric polynomials
sym_polys=[
          [ [1, [1,0,0]], [1, [0,1,0]], [1, [0,0,1]] ],
          [ [1, [2,0,0]], [1, [0,2,0]], [1, [0,0,2]], [1, [1,1,0]], [1, [1,0,1]], [1, [0,1,1]] ],
          [ [1, [3,0,0]], [1, [0,3,0]], [1, [0,0,3]], [1, [2,1,0]], [1, [2,0,1]], [1, [1,2,0]], [1, [0,2,1]], [1, [1,0,2]], [1, [0,1,2]], [1, [1,1,1]] ]
          ]
G.display_poly_list_numbered(sym_polys, ['x', 'y', 'z'])
 
#Grobner bais of ideal generated by sym_polys
Grobner_basis = G.grobner(sym_polys, reduced = True, dim_ranges = [], max_dims = [], progress_output = True)
G.display_poly_list_numbered(Grobner_basis, ['x', 'y', 'z'])

#obtaining the Grobner basis of ideal generated by sym_polys along with an expression in terms of the original ideal
Grobner_basis, Grobner_ideal_corespondence = G.grobner_tracking(sym_polys, reduced = True, dim_ranges = [], max_dims = [], progress_output = True)
G.display_poly_list_list_numbered(Grobner_ideal_corespondence, ['x', 'y', 'z'])

#another polynomial list 
dif_polys = [
            [ [2, [1,0,0]], [1, [0,1,0]], [1, [0,0,1]] ],
            [ [1, [1,0,0]], [2, [0,1,0]], [1, [0,0,1]] ],
            [ [1, [1,0,0]], [1, [0,1,0]], [2, [0,0,1]] ]
            ]

#Grobner basis of the intersection of of ideals generated by sym_polys and dif_polys
#the elements quotient of Z[x,y,z] by symmetric polynomials (sym_polys) have a representative blow degree 6 and all polynomials are homogenious
#so we can set on all varaible (dim_ranges = [[0,2]]) the maximal degree to be 6 (max_dims = [6])
Grobner_basis_of_intersection = G.intersection_Grobner(sym_polys, dif_polys, ['x','y','z'], dim_ranges = [[0,2]], max_dims = [6], grobner_poly_lists_first = False, show_poly_list = True)
G.display_poly_list_numbered(Grobner_basis_of_intersection, ['x', 'y', 'z'])

#Grobner basis of the Syzygy relations between the Grobner basis of the intersection polynomials
intersection_Grobner_Syzygys = G.Syzygy(Grobner_basis_of_intersection, remove_trivial_syz = True, dim_ranges = [], max_dims = [])
G.display_poly_list_list_numbered(intersection_Grobner_Syzygys, ['x', 'y', 'z'])
```

More examples form the paper that the library accompanies can be found in the *'Examples'* folder.

## Reference manual

Unless otherwise stated assume that all polynomials used in any function **must** have the same number variable power entries in their term expressions.

### Polynomial operations

#### &#x1F539; eval_poly(poly, values, keep_variable_positions = False)

Evaluates a polynomial at on list of values for all or some variables.

|  | Variable | Description |
| ------------ | ------------- | ------------- |
| **Parameters:** | **poly** | A polynomial. |
| | **values** | List of numbers of the same length as the number of polynomial variables. Entries of the list can be *None* if the equation of that variable it not desired. |
| | **keep_variable_positions** | Determines weather evaluated variables positions are removed form the polynomials or not. |
| **Returns:** | | An integer or float when all variables are evaluated unless *keep_variable_positions* is *TRUE*. |
| Or | | A polynomial when some variable are not evaluated or when *keep_variable_positions* is *TRUE*. |

---

#### &#x1F539; neg_poly(poly_to_neg)

Negate all coefficients of terms in a polynomial.

|  | Variable | Description |
| ------------ | ------------- | ------------- |
| **Parameters:** | **poly_to_neg** | A polynomial. |
| **Returns:** | | Polynomial negation of the input. |

---

#### &#x1F539; add_poly(poly1,poly2)

Adds a pair of polynomials (each polynomial with the same number of variables).

|  | Variable | Description |
| ------------ | ------------- | ------------- |
| **Parameters:** | **poly1** | A polynomial. |
| | **poly2** | A polynomial. |
| **Returns:** | | Polynomial sum of the inputs. |

---

#### &#x1F539; mult_poly(poly1, poly2, exterior = 0)

Multiplies a pair of polynomials (each polynomial with the same number of variables).

|  | Variable | Description |
| ------------ | ------------- | ------------- |
| **Parameters:** | **poly1** | A polynomial. |
| | **poly2** | A polynomial. |
| | **exterior** | A integer less than the number of variables. Though no longer polynomial multiplication, variables in either polynomial below this value will be treated as variable in an exterior algebra when multiplied. |
| **Returns:** | | Polynomial multiplication of the inputs. |

---

#### &#x1F539; mult_list(poly_to_mul, poly_list, exterior = 0)

Multiplies each polynomial in a list list by a polynomial (all polynomial with the same number of variables).

|  | Variable | Description |
| ------------ | ------------- | ------------- |
| **Parameters:** | **poly_to_mul** | A polynomial. |
| | **poly_list** | A list of polynomials. |
| | **exterior** | A integer less than the number of variables. Though no longer polynomial multiplication, variables in any polynomial below this value will be treated as variable in an exterior algebra when multiplied. |
| **Returns:** | | A Polynomial list, multiplication of the input polynomial list by the input polynomial. |

---

#### &#x1F539; sort_poly(poly_to_sort)

Sorts polynomials terms by monomial lexicographical ordering.

|  | Variable | Description |
| ------------ | ------------- | ------------- |
| **Parameters:** | **poly_to_sort** | A polynomial. |
| **Returns:** | | The input polynomial whose terms are sorted. |

---

#### &#x1F539; sort_poly_list(poly_list_to_sort, sort_with = None)

Sorts each polynomial terms in a list by monomial lexicographical ordering and the list order by monomial lexicographical ordering on the ordered leading terms monomial.

|  | Variable | Description |
| ------------ | ------------- | ------------- |
| **Parameters:** | **poly_list_to_sort** | A list of polynomials. |
| **Returns:** | | the input polynomial list whose order and term orders are sorted. |

---


### Polynomial display functions

#### &#x1F539; poly_to_text(poly, variables)

  Returns a string representation of a given polynomial in polynomial variables of a list of strings with the same length as the number of polynomial variables.

  |  | Variable | Description |
  | ------------ | ------------- | ------------- |
  | **Parameters:** | **poly** | A polynomial. |
  | | **variables** | List of strings of the same length as the number of polynomial variables each string representing the charterer(s) to be used to display the variable at the given position in the list. |
  | **Returns:** | | A string representation of the polynomial. |

---

#### &#x1F539; display_poly_list(poly_list, variables)

  Prints a representation of a given list of polynomials (with same number of variables) on separate lines with polynomial arable representations given as a list of strings with the same length as the number of polynomial variables.

  |  | Variable | Description |
  | ------------ | ------------- | ------------- |
  | **Parameters:** | **poly_list** | A list of polynomials. |
  | | **variables** | List of strings of the same length as the number of polynomial variables each string representing the charterer(s) to be used to display the variable at the given position in the list. |

---

#### &#x1F539; display_poly_list_numbered(poly_list, variables)

  Prints a representation of a given list of polynomials (with same number of variables) each polynomial numbered by list position on separate lines with polynomial variable representations given as a list of strings with the same length as the number of polynomial variables.

  |  | Variable | Description |
  | ------------ | ------------- | ------------- |
  | **Parameters:** | **poly_list** | A list of polynomials. |
  | | **variables** | List of strings of the same length as the number of polynomial variables each string representing the charterer(s) to be used to display the variable at the given position in the list. |

---

#### &#x1F539; display_poly_list_list_numbered(poly_list_list, variables)

  Prints a representation of a given list of polynomials (with same number of variables) in a list each polynomial numbered by list position on separate lines. Polynomials are represented in variables given as a list of strings with the same length as the number of polynomial variables.

  |  | Variable | Description |
  | ------------ | ------------- | ------------- |
  | **Parameters:** | **poly_list_list** | A list of lists of polynomials. |
  | | **variables** | List of strings of the same length as the number of polynomial variables each string representing the charterer(s) to be used to display the variable at the given position in the list. |

---

### Gröbner basis functions

#### &#x1F539; reduce(poly1, poly2)

reduces a **sorted** first polynomial by a second **sorted** polynomial (reduces only leading terms).

|  | Variable | Description |
| ------------ | ------------- | ------------- |
| **Parameters:** | **poly1** | A sorted polynomial. |
| | **poly2** | A sorted polynomial. |
| **Returns:** | | Sorted polynomial reduction of the first input by the second. |

---

#### &#x1F539; full_reduce(poly1, poly2, reduction_out = False)

Fully reduces a **sorted** first polynomial by a second **sorted** polynomial (reduces all terms).

|  | Variable | Description |
| ------------ | ------------- | ------------- |
| **Parameters:** | **poly1** | A sorted polynomial. |
| | **poly2** | A sorted polynomial. |
| | **reduction_out** | A bool, that determines weather a polynomial describing the reduction is output. |
| **Returns:** | | Sorted polynomial full reduction of the first input by the second. |
| Or | | A pair of a Sorted polynomial full reduction of the first input by the second and the polynomial multiple of *poly2* used to fully reduce *poly1*. |

---

#### &#x1F539; list_reduce(poly1, poly_list, full_reduced = False)

Reduce a **sorted** first polynomial by a second list of **sorted** polynomials.

|  | Variable | Description |
| ------------ | ------------- | ------------- |
| **Parameters:** | **poly1** | A sorted polynomial. |
| | **poly_list** | A list of sorted polynomials. |
| | **full_reduced** | A bool, that determines weather reduction (*False*) or full reduction (*True*) is used. |
| **Returns:** | | Sorted polynomial reduction of the first input by the second. |

---

#### &#x1F539; list_reduce_tracking(poly1, poly_list, tracker1, tracker_list, full_reduced = False, reduction_out = False)

Reduce a **sorted** first polynomial by a second list of **sorted** polynomial while tracking and repeating the reduction in a second polynomials by as second list of polynomials.

|  | Variable | Description |
| ------------ | ------------- | ------------- |
| **Parameters:** | **poly1** | A sorted polynomial. |
| | **poly_list** | A list of sorted polynomials. |
| | **tracker1** | A polynomial. |
| | **tracker_list** | A list of polynomials. |
| | **full_reduced** | A bool, that determines weather reduction (*False*) or full reduction (*True*) is used. |
| | **reduction_out** | A bool, that determines weather a polynomial list describing the reduction is output. |
| **Returns:** | | A pair of a sorted polynomial and polynomial. A triple of a sorted polynomial, a polynomial list and a polynomial. These are the reduction of *poly1* and the result of applying the same reduction operations to *tracker1* with *tracker_list. |
| Or | | A triple of a sorted polynomial, a polynomial list and a polynomial. These are the reduction of *poly1*, list of multiple polynomials each element in *poly_list* added to *poly1* to reduces it and the result of applying the same operations to *tracker1* with *tracker_list*. |

---

#### &#x1F539; reduce_list(poly_list, full_reduced = True)

Reduces a **sorted** polynomial list by itself.

|  | Variable | Description |
| ------------ | ------------- | ------------- |
| **Parameters:** | **poly_list** | A list of sorted polynomials. |
| | **full_reduced** | A bool, that determines weather reduction (*False*) or full reduction (*True*) is used. |
| **Returns:** | | Sorted polynomial reduction of input polynomial list by itself. |

---

####
 &#x1F539; reduce_list_tracking(poly_list, tracking_list, full_reduced = True)

Reduces a **sorted** polynomial list by itself while tracking the steps of the reduction.

|  | Variable | Description |
| ------------ | ------------- | ------------- |
| **Parameters:** | **poly_list** | A list of sorted polynomials. |
| | **tracking_list** | A list of polynomials. |
| | **full_reduced** | A bool, that determines weather reduction (*False*) or full reduction (*True*) is used. |
| **Returns:** | | A pair of a sorted polynomial reduction of *poly_list* by itself and a polynomial list obtained form *tracking_list* under the same reduction operations. |

---

#### &#x1F539; S_poly(poly1, poly2)

S-polynomial of two **sorted** polynomials.

|  | Variable | Description |
| ------------ | ------------- | ------------- |
| **Parameters:** | **poly1** | A sorted polynomial. |
| | **poly2** | A sorted polynomial. |
| **Returns:** | | S-polynomial of the input polynomials. |

---

#### &#x1F539; G_poly(poly1, poly2)

G-polynomial of two **sorted** polynomials.

|  | Variable | Description |
| ------------ | ------------- | ------------- |
| **Parameters:** | **poly1** | A sorted polynomial. |
| | **poly2** | A sorted polynomial. |
| **Returns:** | | G-polynomial of the input polynomials. |

---

#### &#x1F539; grobner(poly_list, reduced = True, dim_ranges = [], max_dims = [], progress_output = True)

Provides a Romberg basis of the ideal generated by a list polynomials. For homogenous polynomials the Gröbner basis may be considered only up to a certain degrees in any partition of the the polynomial variables.

|  | Variable | Description |
| ------------ | ------------- | ------------- |
| **Parameters:** | **poly_list** | A polynomial list. |
| | **full_reduced** | A bool, that determines weather Gröbner basis is fully reduced (*True*) or not (*False*). |
| | **dim_ranges** | A list of pairs (or two element list) of integers that form a partition of the number of variables in the polynomials (with index begin at 0), e.g. *[[0,2],[3,5]]* is a partition for six variable polynomials. |
| | **max_dims** | A list of integers of the same length as *dim_ranges*, that determines the maximal dimension considers for the Gröbner basis. |
| | **progress_output** | A bool, that determines weather progress updates are printed during the execution of the algorithm. |
| **Returns:** | | A polynomial list of Gröbner basis generators. |

---

#### &#x1F539; grobner_tracking(poly_list, reduced = True, dim_ranges = [], max_dims = [], progress_output = True)

Provides a Gröbner basis of the ideal generated by a list polynomials and the polynomials that multiples that transform the original ideal generators into the Gröbner basis. For homogenous polynomials the Gröbner basis may be considered only up to a certain degrees in any partition of the the polynomial variables.

|  | Variable | Description |
| ------------ | ------------- | ------------- |
| **Parameters:** | **poly_list** | A polynomial list. |
| | **full_reduced** | A bool, that determines weather Gröbner basis is fully reduced (*True*) or not (*False*). |
| | **dim_ranges** | A list of pairs (or two element list) of integers that form a partition of the number of variables in the polynomials (with index begin at 0), e.g. *[[0,2],[3,5]]* is a partition for six variable polynomials. |
| | **max_dims** | A list of integers of the same length as *dim_ranges*, that determines the maximal dimension considers for the Gröbner basis. |
| | **progress_output** | A bool, that determines weather progress updates are printed during the execution of the algorithm. |
| **Returns:** | | A pair of polynomial list of Gröbner basis generators and a list of list of polynomials that represent for each Gröbner basis generator the list of polynomial multiples of the original *poly_list* that sum together to provide that Gröbner basis generator. |

---

#### &#x1F539; intersection_Grobner(poly_list1_in, poly_list2_in, variables, dim_ranges = [], max_dims = [], grobner_poly_lists_first = False, show_poly_list = True, progress_output = True)

Find a reduced Gröbner basis of the intersection of two ideal whose generators are expressed as two polynomial lists. For homogenous polynomials the Gröbner basis may be considered only up to a certain degrees in any partition of the the polynomial variables.

|  | Variable | Description |
| ------------ | ------------- | ------------- |
| **Parameters:** | **poly_list1_in** | A polynomial list. |
| | **poly_list2_in** | A polynomial list. |
| | **variables** | List of strings of the same length as the number of polynomial variables, each string representing the charterer(s) to be used to display the variable at the given position in the list if required. |
| | **dim_ranges** | A list of pairs (or two element list) of integers that form a partition of the number of variables in the polynomials (with index begin at 0), e.g. *[[0,2],[3,5]]* is a partition for six variable polynomials. |
| | **max_dims** | A list of integers of the same length as *dim_ranges*, that determines the maximal dimension considers for the Gröbner basis. |
| | **grobner_poly_lists_first** | A bool, that determines weather the Gröbner basis of input ideas are first computed separately before commuting the intersection on these Gröbner bases instead (usually faster). |
| | **show_poly_list** | A bool, that when *grobner_poly_lists_first* is *TRUE* determines if the initially computed Gröbner biases are displayed before computing the intersection Gröbner basis. |
| | **progress_output** | A bool, that determines weather progress upgrades are printed during the execution of the algorithm. |
| **Returns:** | | A polynomial list of Gröbner basis generators of the interaction of ideals generated by input polynomial lists. |

---

#### &#x1F539; Syzygy(Grobner_bais, remove_trivial_syz = True, dim_ranges = [], max_dims = [])

Provides a Gröbner basis of Syzygys of a Gröbner basis. For homogenous polynomials the Gröbner basis may be considered only up to a certain degrees in any partition of the polynomial variables.

|  | Variable | Description |
| ------------ | ------------- | ------------- |
| **Parameters:** | **Grobner_bais** | A polynomial list that consists of the generators of a Gröbner basis. |
| | **remove_trivial_syz** | A bool, that determines weather Syzygys of the form of the diffidence of multiples by each over of two generators are removed. |
| | **dim_ranges** | A list of pairs (or two element list) of integers that form a partition of the number of variables in the polynomials (with index begin at 0), e.g. *[[0,2],[3,5]]* is a partition for six variable polynomials. |
| | **max_dims** | A list of integers of the same length as *dim_ranges*, that determines the maximal dimension considers for the Gröbner basis. |
| **Returns:** | | A polynomial list of generators of a Gröbner basis Syzygys of the input Gröbner basis. |

---
