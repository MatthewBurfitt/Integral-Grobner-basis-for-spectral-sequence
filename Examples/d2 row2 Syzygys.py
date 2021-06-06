import IntegralGrobner as G

#set varaible names
varaibles = ["y1","y2","y3","g2","g1","g"]

#set polynomials
y1d2 = [ [-1, [1,1,0,1,0,0]], [-4, [1,0,1,0,0,1]], [-1, [1,0,1,0,1,0]], [-1, [1,0,1,1,0,0]] ]

y2d2 = [ [-1, [1,1,0,0,1,0]], [-4, [0,1,1,0,0,1]], [-1, [0,1,1,0,1,0]], [-1, [0,1,1,1,0,0]] ]

y3d2 = [ [-1, [1,0,1,0,1,0]], [1, [0,1,1,1,0,0]] ]

dif_poly2_row2 = [y1d2, y2d2, y3d2]

#displayes initial polynomial list                    
print("\n Polynomial set:")
G.display_poly_list(dif_poly2_row2, varaibles)

#maximal dimension ranges for homeginous polynomial Grobner basis computation
dim_ranges = [[0, 2], [3, 5]]
max_dims = [2, 6]

#compute grobner basis up to degree 6
grobner, expressions = G.grobner_tracking(dif_poly2_row2, reduced = True, dim_ranges = dim_ranges, max_dims = max_dims)

#display grobner basis
print("\n Grobner basis:")
G.display_poly_list_numbered(grobner, varaibles)

#display grobner basis expresssion in terms of input polynomials
print("\n Grobner basis in terms of intial input Ideal:")
G.display_poly_list_list_numbered(expressions, varaibles)

#compute Syzygys of the grobner basis
Syzygys = G.Syzygy(grobner, remove_trivial_syz = True, dim_ranges = dim_ranges, max_dims = max_dims)

#display Syzygys
print('\n Syzygys:')
G.display_poly_list_list_numbered(Syzygys, varaibles)
