import IntagralGrobner as G

#set variabel names
varaibles = ["y1","y2","y3","g2","g1","g"]

#set polynomials
sym_polys = [
            [ [1, [0,0,0,2,0,0]], [1, [0,0,0,1,1,0]], [1, [0,0,0,0,2,0]], [4, [0,0,0,1,0,1]], [4, [0,0,0,0,1,1]], [6, [0,0,0,0,0,2]] ],
            [ [1, [0,0,0,0,3,0]], [4, [0,0,0,0,2,1]], [6, [0,0,0,0,1,2]], [4, [0,0,0,0,0,3]] ],
            [ [1, [0,0,0,0,0,4]] ]
            ]

y1y2 = [[1, [1,1,0,0,0,0]]]
y1y3 = [[1, [1,0,1,0,0,0]]]
y2y3 = [[1, [0,1,1,0,0,0]]]

sym_polys = G.mult_list(y1y2, sym_polys)+ G.mult_list(y1y3, sym_polys) + G.mult_list(y2y3, sym_polys)

y1d2 = [ [-1, [1,1,0,1,0,0]], [-4, [1,0,1,0,0,1]], [-1, [1,0,1,0,1,0]], [-1, [1,0,1,1,0,0]] ]
y2d2 = [ [-1, [1,1,0,0,1,0]], [-4, [0,1,1,0,0,1]], [-1, [0,1,1,0,1,0]], [-1, [0,1,1,1,0,0]] ]
y3d2 = [ [-1, [1,0,1,0,1,0]], [1, [0,1,1,1,0,0]] ]
dif_poly2_row2 = [y1d2, y2d2, y3d2]

y3 = [[1, [0,0,1,0,0,0]]]
y3part = [[-4, [0,0,0,0,0,1]], [-1, [0,0,0,0,1,0]], [-1, [0,0,0,1,0,0]]]
y3part_squared = G.mult_poly(y3, G.mult_poly(y3part,y3part))
y1d4 = [ [-1, [1,1,0,2,0,0]] ] + G.mult_poly([ [1, [1,0,0,0,0,0]] ], y3part_squared)
y2d4 = [ [-1, [1,1,0,0,2,0]] ] + G.mult_poly([ [1, [0,1,0,0,0,0]] ], y3part_squared)
y3d4 = [ [-1, [1,0,1,0,2,0]], [1, [0,1,1,2,0,0]] ]
dif_poly4_row2 = [y1d4, y2d4, y3d4]

y3part_cubed = G.mult_poly(y3, G.mult_poly(y3part, G.mult_poly(y3part,y3part)))
y1d6 = [ [-1, [1,1,0,3,0,0]] ] + G.mult_poly([ [-1, [1,0,0,0,0,0]] ], y3part_cubed)
y2d6 = [ [-1, [1,1,0,0,3,0]] ] + G.mult_poly([ [-1, [0,1,0,0,0,0]] ], y3part_cubed)
y3d6 = [ [-1, [1,0,1,0,3,0]], [1, [0,1,1,3,0,0]] ]
dif_poly6_row2 = [y1d6, y2d6, y3d6]


#Ideals to intersect
dif_polys = dif_poly2_row2 + dif_poly4_row2 + dif_poly6_row2

#displayes initial polynomial list                    
print("\n Symetric polynomial set:")
G.display_poly_list(sym_polys, varaibles)                    
print("\n Differential polynomial set:")
G.display_poly_list(dif_polys, varaibles)

#maximal dimension ranges for homeginous polynomial grober basis computation
dim_ranges = [[0, 2], [3, 5]]
max_dims = [2, 6]

#combined polynomials lists for grobner basis calculation
Grobner_basis = G.grobner(sym_polys + dif_polys, reduced = True, dim_ranges = dim_ranges, max_dims = max_dims)
print("\n Reduced Grobner basis of all relations")
G.display_poly_list(Grobner_basis, varaibles)

