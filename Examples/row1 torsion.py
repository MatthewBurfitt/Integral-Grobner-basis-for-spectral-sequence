import IntagralGrobner as G

#set variabel names
varaibles = ["y1","y2","y3","g2","g1","g"]

#set polynomials
sym_polys = [
            [ [1, [0,0,0,2,0,0]], [1, [0,0,0,1,1,0]], [1, [0,0,0,0,2,0]], [4, [0,0,0,1,0,1]], [4, [0,0,0,0,1,1]], [6, [0,0,0,0,0,2]] ],
            [ [1, [0,0,0,0,3,0]], [4, [0,0,0,0,2,1]], [6, [0,0,0,0,1,2]], [4, [0,0,0,0,0,3]] ],
            [ [1, [0,0,0,0,0,4]] ]
            ]

y1 = [[1, [1,0,0,0,0,0]]]
y2 = [[1, [0,1,0,0,0,0]]]
y3 = [[1, [0,0,1,0,0,0]]]

sym_polys = G.mult_list(y1, sym_polys)+ G.mult_list(y2, sym_polys) + G.mult_list(y3, sym_polys)

dif_poly2 = [
            [ [1, [1,0,0,0,1,0]], [-1, [0,1,0,1,0,0]], [-4, [0,0,1,0,0,1]], [-1, [0,0,1,0,1,0]], [-1, [0,0,1,1,0,0]] ]
            ]

dif_poly4 = [
            [ [1, [1,0,0,0,2,0]], [-1, [0,1,0,2,0,0]], [1, [0,0,1,2,0,0]], [2, [0,0,1,1,1,0]], [8, [0,0,1,1,0,1]], [1, [0,0,1,0,2,0]], [8, [0,0,1,0,1,1]], [16, [0,0,1,0,0,2]] ]
            ]

y3part = [[-4, [0,0,0,0,0,1]], [-1, [0,0,0,0,1,0]], [-1, [0,0,0,1,0,0]]]
first_part = [[1, [1,0,0,0,3,0]], [-1, [0,1,0,3,0,0]]]

dif_poly6 = [G.sort_poly(G.add_poly(first_part, G.mult_poly(y3, G.mult_poly(y3part, G.mult_poly(y3part,y3part)))))]

dif_polys = dif_poly2 + dif_poly4 + dif_poly6

#displayes initial polynomial lists                    
print("\n Symetric polynomial set:")
G.display_poly_list(sym_polys, varaibles)                   
print("\n Differential polynomial set:")
G.display_poly_list(dif_polys, varaibles)

#maximal dimension ranges for homeginous polynomial grober basis computation
dim_ranges = [[0, 2], [3, 5]]
max_dims = [1, 6]

#combined polynomials lists for grobner basis calculation
Grobner_basis = G.grobner(sym_polys + dif_polys, reduced = True, dim_ranges = dim_ranges, max_dims = max_dims)
print("\n Reduced Grobner basis of all relations")
G.display_poly_list(Grobner_basis, varaibles)

