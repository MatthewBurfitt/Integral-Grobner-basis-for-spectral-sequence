#d2_row2
#WARNING!!! may take some time to run
import IntegralGrobner as G

#set variabel names
varaibles = ["y1","y2","y3","g2","g1","g"]

#set polynomials
y1 = [1, [1,0,0,0,0,0]]
y2 = [1, [0,1,0,0,0,0]]
y3 = [1, [0,0,1,0,0,0]]

sym_polys = [
    [ [1, [0,0,0,2,0,0]], [1, [0,0,0,1,1,0]], [1, [0,0,0,0,2,0]], [4, [0,0,0,1,0,1]], [4, [0,0,0,0,1,1]], [6, [0,0,0,0,0,2]] ],
    [ [1, [0,0,0,0,3,0]], [4, [0,0,0,0,2,1]], [6, [0,0,0,0,1,2]], [4, [0,0,0,0,0,3]] ],
    [ [1, [0,0,0,0,0,4]] ]
    ]

y1d2 = [ [-1, [1,1,0,1,0,0]], [-4, [1,0,1,0,0,1]], [-1, [1,0,1,0,1,0]], [-1, [1,0,1,1,0,0]] ]

y2d2 = [ [-1, [1,1,0,0,1,0]], [-4, [0,1,1,0,0,1]], [-1, [0,1,1,0,1,0]], [-1, [0,1,1,1,0,0]] ]

y3d2 = [ [-1, [1,0,1,0,1,0]], [1, [0,1,1,1,0,0]] ]

dif_poly2_row2 = [y1d2, y2d2, y3d2]

#Ideals to intersect
dif_polys = dif_poly2_row2
quotient = sym_polys

#displayes initial polynomial list                    
print("\n Symetric polynomial set:")
G.display_poly_list(quotient, varaibles)                    
print("\n Differential polynomial set:")
G.display_poly_list(dif_polys, varaibles)

#maximal dimension ranges for homeginous polynomial Grobner basis computation
dim_ranges = [[0, 2], [3, 5]]
max_dims = [2, 6]

#combined polynomials for intersection calculation
Grobner_basis = G.intersection_Grobner(quotient, dif_polys, varaibles, dim_ranges = dim_ranges, max_dims = max_dims, grobner_poly_lists_first = True)
print("\n Reduced Grobner basis of intersection:")
G.display_poly_list(Grobner_basis, varaibles)

#determin the reduction of the Grobner basis of the intersection in terms of initial differntal image and preimage under the differntial
reductions = []
preimage = []
for i in range(len(Grobner_basis)):
    poly_out, reduction_list = G.list_reduce(Grobner_basis[i], dif_polys, full_reduced = True, edit_out = False, reduction_out = True)
    reductions.append(reduction_list)
    preimage.append(G.add_poly(G.add_poly(G.mono_mult(y1, reduction_list[0]),
                                           G.mono_mult(y2, reduction_list[1])),
                                           G.mono_mult(y3, reduction_list[2])))
print('\n Reduction of intersection Grobner basis by differential image')
G.display_poly_list_list_numbered(reductions, varaibles)
print('\n Preimage under differential of interection of ideals (x_2 multiple)')
G.display_poly_list_numbered(preimage, varaibles)
