#d4im row2 d2ker
import IntegralGrobner as G

#set variabel names
varaibles = ["y1","y2","y3","g2","g1","g"]

#set polynomials
sym_polys = [
            [ [1, [0,0,0,2,0,0]], [1, [0,0,0,1,1,0]], [1, [0,0,0,0,2,0]], [4, [0,0,0,1,0,1]], [4, [0,0,0,0,1,1]], [6, [0,0,0,0,0,2]] ],
            [ [1, [0,0,0,0,3,0]], [4, [0,0,0,0,2,1]], [6, [0,0,0,0,1,2]], [4, [0,0,0,0,0,3]] ],
            [ [1, [0,0,0,0,0,4]] ]
            ]

dif_poly4 = [
            [ [1, [1,0,0,0,2,0]], [-1, [0,1,0,2,0,0]], [1, [0,0,1,2,0,0]], [2, [0,0,1,1,1,0]], [8, [0,0,1,1,0,1]], [1, [0,0,1,0,2,0]], [8, [0,0,1,0,1,1]], [16, [0,0,1,0,0,2]] ]
            ]

y1d2 = [ [-1, [1,1,0,1,0,0]], [-4, [1,0,1,0,0,1]], [-1, [1,0,1,0,1,0]], [-1, [1,0,1,1,0,0]] ]

y2d2 = [ [-1, [1,1,0,0,1,0]], [-4, [0,1,1,0,0,1]], [-1, [0,1,1,0,1,0]], [-1, [0,1,1,1,0,0]] ]

y3d2 = [ [-1, [1,0,1,0,1,0]], [1, [0,1,1,1,0,0]] ]

dif_poly2_row2 = [y1d2, y2d2, y3d2]

y3 = [[1, [0,0,1,0,0,0]]]
y3part = [[-4, [0,0,0,0,0,1]], [-1, [0,0,0,0,1,0]], [-1, [0,0,0,1,0,0]]]
row2_d2ker_type1 = [ [1, [1,0,0,0,1,0]], [-1, [0,1,0,1,0,0]] ] + G.mult_poly(y3, y3part)

row2_d2ker = [
             [ [1, [1,0,0,2,0,0]], [4, [1,0,0,1,0,1]], [6, [1,0,0,0,0,2]], [-1, [0,1,0,0,2,0]], [-4, [0,1,0,0,1,1]], [-6, [0,1,0,0,0,2]], [-1, [0,0,1,2,0,0]], [-1, [0,0,1,0,2,0]], [4, [0,0,1,0,0,2]]],
             [ [1, [1,0,0,1,0,3]], [1, [1,0,0,0,1,3]], [1, [0,1,0,0,1,3]], [-1, [0,0,1,1,0,3]] ],    
             [ [2, [1,0,0,1,0,2]], [2, [1,0,0,0,1,2]], [8, [1,0,0,0,0,3]], [-3, [0,1,0,0,2,1]], [-10, [0,1,0,0,1,2]], [-10, [0,1,0,0,0,3]],
               [2, [0,0,1,1,2,0]], [8, [0,0,1,1,1,1]], [10, [0,0,1,1,0,2]], [5, [0,0,1,0,2,1]], [20, [0,0,1,0,1,2]], [22, [0,0,1,0,0,3]]  ],
             [ [3, [0,1,0,0,2,2]], [12, [0,1,0,0,1,3]], [-2, [0,0,1,1,2,1]], [-8, [0,0,1,1,1,2]], [-12, [0,0,1,1,0,3]], [-5, [0,0,1,0,2,2]], [-20, [0,0,1,0,1,3]] ]
             ] + [row2_d2ker_type1]

d4im_row2_d2ker = []
for poly in row2_d2ker:
    d4im_row2_d2ker.append(G.mult_poly(poly, dif_poly4[0], exterior = 3))

#Ideals to intersect
dif_polys = d4im_row2_d2ker
quotient = sym_polys + dif_poly2_row2

#displayes initial polynomial lists                    
print("\n Symetric polynomial set:")
G.display_poly_list(quotient, varaibles)
print("\n Row 2 d2 kernal polynomial set:")
G.display_poly_list(row2_d2ker, varaibles)

#displayes initial image polynomial list                    
print("\n Differential polynomial set:")
G.display_poly_list_numbered(dif_polys, varaibles)

#maximal dimension ranges for homeginous polynomial Grobner basis computation
dim_ranges = [[0, 2], [3, 5]]
max_dims = [2, 6]

#Grobner basis of differential polynomials with expression in terms of original ideal and Grobner basis Syzygys
diff_grobner, diff_expressions = G.grobner_tracking(dif_polys, reduced = True, dim_ranges = dim_ranges, max_dims = max_dims)
print("\n Reduced Grobner basis of differential polynomial set")
G.display_poly_list_numbered(diff_grobner, varaibles)
print("\n Expression of differential Grobner basis in terms of original ideal generators")
G.display_poly_list_list_numbered(diff_expressions, varaibles)
diff_Syzygys = G.Syzygy(diff_grobner, remove_trivial_syz = True)
print("\n Differential Grobner basis Syzygys")
G.display_poly_list_list_numbered(diff_Syzygys, varaibles)

#combined polynomials for intersection calculation
Grobner_basis = G.intersection_Grobner(quotient, diff_grobner, varaibles, dim_ranges = dim_ranges, max_dims = max_dims, grobner_poly_lists_first = True, show_poly_list = False)
print("\n Reduced Grobner basis of intersection:")
G.display_poly_list(Grobner_basis, varaibles)

#determin the reduction of the grobner basis of the intersection in terms of initial differntal image
reductions = []
for i in range(len(Grobner_basis)):
    poly_out, reduction_list = G.list_reduce(Grobner_basis[i], diff_grobner, full_reduced = True, edit_out = False, reduction_out = True)
    reductions.append(reduction_list)
print('\n Reduction of intersection grobner basis by differential image')
G.display_poly_list_list_numbered(reductions, varaibles)


