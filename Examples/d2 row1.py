#d2_row1
import IntagralGrobner as G

#set variabel names
varaibles = ["y1","y2","y3","g2","g1","g"]

#set polynomials
sym_polys = [
    [ [1, [0,0,0,2,0,0]], [1, [0,0,0,1,1,0]], [1, [0,0,0,0,2,0]], [4, [0,0,0,1,0,1]], [4, [0,0,0,0,1,1]], [6, [0,0,0,0,0,2]] ],
    [ [1, [0,0,0,0,3,0]], [4, [0,0,0,0,2,1]], [6, [0,0,0,0,1,2]], [4, [0,0,0,0,0,3]] ],
    [ [1, [0,0,0,0,0,4]] ]
    ]

dif_poly2 = [
    [ [1, [1,0,0,0,1,0]], [-1, [0,1,0,1,0,0]], [-4, [0,0,1,0,0,1]], [-1, [0,0,1,0,1,0]], [-1, [0,0,1,1,0,0]] ]
    ]

#Ideals to intersect
dif_polys = dif_poly2
quotient = sym_polys

#displayes initial polynomial lists                    
print("\n Symetric polynomial set:")
G.display_poly_list(quotient, varaibles)                   
print("\n Differential polynomial set:")
G.display_poly_list(dif_polys, varaibles)

#maximal dimension ranges for homeginous polynomial grober basis computation
dim_ranges = [[0, 2], [3, 5]]
max_dims = [1, 6]

#combined polynomials for intersection calculation
Grobner_basis = G.intersection_Grobner(quotient, dif_polys, varaibles, dim_ranges = dim_ranges, max_dims = max_dims, grobner_poly_lists_first = True)
print("\n Reduced Grobner basis of intersection:")
G.display_poly_list(Grobner_basis, varaibles)

#determin the reduction of the Grobner basis of the intersection in terms of initial differntal image and preimage under differntial
reductions = []
preimage = []
for i in range(len(Grobner_basis)):
    poly_out, reduction_list = G.list_reduce(Grobner_basis[i], dif_polys, full_reduced = True, edit_out = False, reduction_out = True)
    preimage.append(reduction_list[0])
    reductions.append(reduction_list)
print('\n Reduction of intersection Grobner basis by differential image')
G.display_poly_list_list_numbered(reductions, varaibles)
print('\n Preimage under differential of interection of ideals (x_2 multiple)')
G.display_poly_list_numbered(preimage, varaibles)
