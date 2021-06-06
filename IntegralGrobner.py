import copy
from math import gcd
import json

#*************************************************Gernaral maths functions*************************************************

#extended Eucliedan agroithum
def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

#lowest common multiple of two integers
def lcm(a,b):
    return (a*b)/gcd(a,b)

#*************************************************Polynomial display functions*************************************************

#gives a text form of a polynomial with polynomial variables named form a varable list
def poly_to_text(poly, variables):
    if poly == []:
        return('0')
    else:
        text = ''
        for term in poly:
            if term[0] == 1 and term == poly[0]:
                if sum(term[1]) == 0:
                    text +=" 1"
            elif term[0] == -1:
                text+="-"
                if sum(term[1]) == 0:
                    text += "1"
            elif term[0]<-1 or term == poly[0]:
                text+=str(term[0])
            elif term[0] == 1:
                text += "+"
                if sum(term[1]) == 0:
                    text += "1"
            else:
                text += "+" + str(term[0])
            for i in range(len(term[1])):
                if term[1][i] ==1 :
                    text += variables[i]
                elif term[1][i] > 1:
                        text += variables[i] + "^" + str(term[1][i])
        return(text)

#prints all polynomials in a list with polynomial variables from a varables list
def display_poly_list(poly_list, variables):
    for poly in poly_list:
        text = "\n " + poly_to_text(poly, variables)
        print(text)

#prints all polynomials nubered using a list with polynomial variables from a varables list
def display_poly_list_numbered(poly_list, variables):
    for i in range(len(poly_list)):
        text = "\n (" + str(i+1) + ") " + poly_to_text(poly_list[i], variables)
        print(text)

#prints all polynomials in a list of lists of polynomials numbering both list levels with polynomial variables from a varables list
def display_poly_list_list_numbered(poly_list_list, variables):
    for i in range(len(poly_list_list)):
        for j in range(len(poly_list_list[i])):
            if j == 0:
                temp = str(i+1) + "."
            else:
                temp = "  "
            text = "\n " + temp + " (" + str(j+1) + ") " + poly_to_text(poly_list_list[i][j], variables)
            print(text)

#*************************************************Polynomial read & write text file functions*************************************************

#Write polynomial to text file
#for polynomials and polynomial lists or list of lists.....
def write_poly(poly, file_name = 'polynomial'):
    if file_name[len(file_name)-4:len(file_name)] != '.txt':
        file_name = file_name + '.txt'
    poly = json.dumps(poly)
    with open(file_name, "w") as f:
        f.write(poly)

#Read polynomial from text file
#for polynomials and polynomial lists or list of lists.....           
def read_poly(file_name = 'polynomial'):
    if file_name[len(file_name)-4:len(file_name)] != '.txt':
        file_name = file_name + '.txt'
    poly = []
    with open(file_name) as f:
        for line in f:
            poly += json.loads(line)
    return poly

#*************************************************Gernaral polynomial functions*************************************************

#combines terms of the same type in a polynomial
def col_poly(poly_to_col):
    poly=copy.deepcopy(poly_to_col)
    for i in range(len(poly)-1,-1,-1):
        for j in range(i-1,-1,-1):
            if poly[i][1]==poly[j][1]:
                poly[j][0]+=poly[i][0]
                del(poly[i])
                break
    for i in range(len(poly)-1,-1,-1):
        if poly[i][0]==0:
            del(poly[i])
    return poly

#Evaluates a polynomial at a list of number values for each varibale
#if a one or more variabes are 'None' then returns a polynomial evaluated on all terms but those variables reducing the total number of variables
#if keep_varaible_positions then return a polynomial with the same number of variables regardless of variable evauation
def eval_poly(poly, values, keep_variable_positions = False):
    numeric = True
    for value in values:
        if value == None:
            numeric = False
            break
    if numeric:
        total = 0
    else:
        new_poly = []
    for term in poly:
        term_total = term[0]
        term_list = []
        for i in range(len(values)):
            if values[i] == None:
                term_list.append(term[1][i])
            else:
                term_total *= values[i]**(term[1][i])
                if keep_variable_positions:
                    term_list.append(0)
        if numeric:
            total += term_total
        else:
            new_poly.append([term_total, term_list])
    if numeric:
        if keep_variable_positions:
            return [[total, [0]*len(values)]]
        else:
            return total
    else:
        return col_poly(new_poly)

#sort polynomial terms by monomial lex order
def sort_poly(poly_to_sort):
    poly=copy.deepcopy(col_poly(poly_to_sort))
    done=False
    while done==False:
        done=True
        for i in range(len(poly)-1):
            for j in range(len(poly[i][1])):
                if poly[i][1][j]>poly[i+1][1][j]:
                    break
                elif poly[i][1][j]<poly[i+1][1][j]:
                    temp=poly[i]
                    poly[i]=poly[i+1]
                    poly[i+1]=temp
                    done=False
                    break
    return poly

#removes the empty polynomials form a list of polynomials
def remove_empty_polys(poly_list):
    new_poly_list = copy.deepcopy(poly_list)
    for i in range(len(new_poly_list)-1,-1,-1):
        if new_poly_list[i] == []:
            del new_poly_list[i]
    return new_poly_list

#sorts a list of polynomials by leadind monomial lex order
#can addtionaly rearange another list in the smae way simultaiously
def sort_poly_list(poly_list_to_sort, sort_with = None):
    poly_list=copy.deepcopy(poly_list_to_sort)
    if sort_with:
        other_thing_to_sort = copy.deepcopy(sort_with)
    for i in range(len(poly_list)):
        poly_list[i] = sort_poly(poly_list[i])
    done=False
    while done==False:
        done=True
        for i in range(len(poly_list)-1):
            for j in range(len(poly_list[i][0][1])):
                if poly_list[i][0][1][j]>poly_list[i+1][0][1][j]:
                    break
                elif poly_list[i][0][1][j]<poly_list[i+1][0][1][j]:
                    temp = poly_list[i]
                    poly_list[i] = poly_list[i+1]
                    poly_list[i+1] = temp
                    if sort_with:
                        temp = other_thing_to_sort[i]
                        other_thing_to_sort[i] = other_thing_to_sort[i+1]
                        other_thing_to_sort[i+1] = temp
                    done=False
                    break
    if sort_with:
        return poly_list, other_thing_to_sort
    else:
        return poly_list

#negates a polynomial
def neg_poly(poly_to_neg):
    poly=copy.deepcopy(poly_to_neg)
    for term in poly:
        term[0]=-term[0]
    return poly

#nomalises a polynomial list, that is makes the leading coeficents of each polynomial posative
def norm_poly_list(poly_list_to_norm, trackers_to_norm = None):
    poly_list = copy.deepcopy(poly_list_to_norm)
    if trackers_to_norm:
        trackers = copy.deepcopy(trackers_to_norm)
        for i in range(len(poly_list)):
            if poly_list[i][0][0]<0:
                poly_list[i] = neg_poly(poly_list[i])
                for j in range(len(trackers[i])):
                    trackers[i][j] = neg_poly(trackers[i][j])
        return poly_list, trackers
    else:
        for i in range(len(poly_list)):
            if poly_list[i][0][0]<0:
                poly_list[i] = neg_poly(poly_list[i])
        return poly_list

#adds a pair of polynomials
def add_poly(poly1,poly2):
    poly=poly1+poly2
    poly=col_poly(poly)
    return poly

#multiplies a polynomial by a constant
def coef_mult(poly_to_mult,coef):
    poly=copy.deepcopy(poly_to_mult)
    for i in range(len(poly)):
        poly[i][0] *= coef
    return poly

#multiplies a polynomial by a monomial
def mono_mult(mon, poly_to_mult, exterior = 0):
    poly=copy.deepcopy(poly_to_mult)
    for i in range(len(poly)-1,-1,-1):
        poly[i][0]*=mon[0]
        for j in range(len(mon[1])):
            poly[i][1][j]+=mon[1][j]
        for k in range(exterior):
            if poly[i][1][k] > 1:
                del(poly[i])
                break
            elif poly_to_mult[i][1][k] == 1:
                for l in range(k,exterior):
                    if mon[1][l] > 0:
                        poly[i][0] *= -1
    return poly

#multiplys two polynomials
def mult_poly(poly1, poly2, exterior = 0):
    poly=[]
    for mon in poly1:
        poly=poly+(mono_mult(mon,poly2, exterior = exterior))
    poly=col_poly(poly)
    return poly

#multiplys a polynomial list by a polynomial
def mult_list(poly_to_mul, poly_list, exterior = 0):
    new_list = []
    for poly in poly_list:
        new_list.append(mult_poly(poly_to_mul, poly, exterior = exterior))
    return new_list

#lowest common multiple of two monomials
def lcm_mon(mon1, mon2):
    mon=copy.deepcopy(mon1)
    mon[0]=lcm(mon1[0],mon2[0])       
    for i in range(len(mon1[1])):
        if mon1[1][i]>=mon2[1][i]:
            mon[1][i]=copy.deepcopy(mon1[1][i])
        else:
            mon[1][i]=copy.deepcopy(mon2[1][i])
    return(mon)

#check monomial divisibility of first monomial by second
def div_check(mon1, mon2):
    divisable=True
    if mon1[0]%mon2[0]==0:
        for i in range(len(mon1[1])):
            if mon1[1][i]<mon2[1][i]:
                divisable=False
                break
    else:
        divisable=False
    return divisable

#divides first monmila by the second monomial
def div_mon(mon1,mon2):
    mon=copy.deepcopy(mon1)
    mon[0]=int(mon1[0]/mon2[0])
    for i in range(len(mon1[1])):
        mon[1][i]=mon1[1][i]-mon2[1][i]
    return mon

#removes all polynomilas is a list with a term divisable by a certain monomial
def remove_polys_containing(poly_list,mon):
    new_poly_list = copy.deepcopy(poly_list)
    for i in range(len(poly_list)-1,-1,-1):
        for j in range(len(poly_list[i])):
            if div_check(poly_list[i][j],mon):
                del(new_poly_list[i])
                break
    return new_poly_list

#checks a certain subset of coeficents does not exceed a given dimension
def dim_range_check(mon, dim_ranges, max_dims):
    satisfied = True
    for i in range(len(max_dims)):
        if sum(mon[1][dim_ranges[i][0]:(dim_ranges[i][1]+1)]) > max_dims[i]:
            satisfied = False
            break
    return satisfied

#removes the first varible form all terms of polynomials in a list of polynomials
def remove_highest_var(poly_list):
    new_poly_list = []
    for poly in poly_list:
        new_poly = []
        for mon in poly:
            new_poly.append([mon[0], mon[1][1:]])
        new_poly_list.append(new_poly)
    return new_poly_list

#***************************************************Grobner basis functions**************************************************

#reduces a sorted first polynomial by a second sorted polynomial
def reduce(poly1, poly2):
    if div_check(poly1[0],poly2[0]):
        poly = add_poly( poly1 , neg_poly(mono_mult(div_mon(poly1[0],poly2[0]),poly2)) )
    return sort_poly(poly)

#reduces a sorted first polynomial by a second sorted polynomial while tracking and repeating the reduction in a second pair of polynomials
def reduce_and_track(poly1, poly2, tracker1, tracker2):
    tracker = copy.deepcopy(tracker1)
    if div_check(poly1[0], poly2[0]):
        term = neg_poly((div_mon(poly1[0], poly2[0])))
        poly = add_poly(poly1, mult_poly(term, poly2))
        for i in range(len(tracker)):
            tracker[i] = sort_poly(add_poly(tracker1[i], mult_poly(term, tracker2[i])))
    return sort_poly(poly), tracker

#fully reduces a sorted first polynomial by a second sorted polynomial (recursive algorithum)
def full_reduce(poly1, poly2, edit_out = False, reduction_out = False):
    edit = False
    reduction = []
    poly=copy.deepcopy(poly1)
    for i in range(len(poly1)):
        if div_check(poly1[i],poly2[0]):
            edit = True
            if reduction_out:
                poly, extra_reduction = full_reduce(sort_poly(add_poly(poly,neg_poly(mono_mult(div_mon(poly[i],poly2[0]),poly2)))), poly2, reduction_out = True)
                reduction.append(div_mon(poly1[i], poly2[0]))
                reduction += extra_reduction
            else:
                poly = full_reduce(sort_poly(add_poly(poly,neg_poly(mono_mult(div_mon(poly[i],poly2[0]),poly2)))), poly2)
            break
    if edit_out:
        if reduction_out:
            return edit, sort_poly(poly), sort_poly(reduction)
        else:
            return edit, sort_poly(poly)
    else:
        if reduction_out:
            return sort_poly(poly), sort_poly(reduction)
        else:
            return sort_poly(poly)

#reduce a sorted first polynomial by a second list of sorted polynomials
def list_reduce(poly1, poly_list, full_reduced = False, edit_out = False, reduction_out = False):
    poly=copy.deepcopy(poly1)
    if reduction_out:
        reduction_list = []
        for i in range(len(poly_list)):
            reduction_list.append([])
    done=False
    edit=False
    while done == False:
        done = True
        for i in range(len(poly_list)):
            if full_reduced:
                if reduction_out:
                    change, poly, reduction = full_reduce(poly, poly_list[i], edit_out = True, reduction_out = True)
                    reduction_list[i] += reduction
                else:
                    change, poly = full_reduce(poly, poly_list[i], edit_out = True)
                done = not change
                if change:
                    edit = True
            else:
                if reduction_out:
                    print('Reduction output only supported for full reductions!')
                if div_check(poly[0],poly_list[i][0]):
                    poly = reduce(poly,poly_list[i])
                    done = False
                    edit = True
            if len(poly) == 0:
                done = True
                break
    if reduction_out:
        for i in range(len(poly_list)):
            reduction_list[i] = sort_poly(col_poly(reduction_list[i]))
    if edit_out:
        if reduction_out:
            return edit, poly, reduction_list
        else:
            return edit, poly
    else:
        if reduction_out:
            return poly, reduction_list
        else:
            return poly

#reduce a sorted first polynomial by a second list of sorted polynomial while tracking and repeating the reduction in a second polynomials by as second list of polynomials
def list_reduce_tracking(poly1, poly_list, tracker1, tracker_list, full_reduced = False, edit_out = False, reduction_out = False):
    poly = copy.deepcopy(poly1)
    tracker = copy.deepcopy(tracker1)
    reduction_list = []
    for i in range(len(poly_list)):
        reduction_list.append([])
    done=False
    edit=False
    while done == False:
        done = True
        for i in range(len(poly_list)):
            if full_reduced:
                change, poly, reduction = full_reduce(poly, poly_list[i], edit_out = True, reduction_out = True)
                reduction_list[i] += reduction
                done = not change
                if change:
                    edit = True
            else:
                if reduction_out:
                    print('Reduction output only supported for full reductions!')
                if div_check(poly[0],poly_list[i][0]):
                    poly = reduce(poly,poly_list[i])
                    done = False
                    edit = True
            if len(poly) == 0:
                done = True
                break
    for i in range(len(poly_list)):
        reduction_list[i] = sort_poly(col_poly(reduction_list[i]))
        for j in range(len(tracker)):
            tracker[j] = sort_poly(add_poly(tracker[j], neg_poly(mult_poly(reduction_list[i], tracker_list[i][j]))))
    if edit_out:
        if reduction_out:
            return edit, poly, reduction_list, tracker
        else:
            return edit, poly, tracker
    else:
        if reduction_out:
            return poly, reduction_list, tracker
        else:
            return poly, tracker

#reduces a sorted polynomial list by itself
def reduce_list(poly_list, full_reduced = True):
    poly_list_new = copy.deepcopy(poly_list)
    done = False
    while done == False:
        done = True
        for i in range(len(poly_list_new)-1,-1,-1):
            poly_list_now = copy.deepcopy(poly_list_new)
            del(poly_list_now[i])
            edit, poly_list_new[i] = list_reduce(poly_list_new[i],poly_list_now, full_reduced = full_reduced, edit_out = True)
            if poly_list_new[i] == []:
                del(poly_list_new[i])
            if edit:
                done = False
    if full_reduce:
        return norm_poly_list(sort_poly_list(poly_list_new))
    else:
        return sort_poly_list(poly_list_new)

#reduces a sorted polynomial list by itself while tracking the steps of the reduction
def reduce_list_tracking(poly_list, tracking_list, full_reduced = True):
    poly_list_new = copy.deepcopy(poly_list)
    tracking_list_new = copy.deepcopy(tracking_list)
    done = False 
    while done == False:
        done = True
        for i in range(len(poly_list_new)-1,-1,-1):
            poly_list_now = copy.deepcopy(poly_list_new)
            tracking_list_now = copy.deepcopy(tracking_list_new)
            del(poly_list_now[i])
            del(tracking_list_now[i])
            edit, poly_list_new[i], tracking_list_new[i] = list_reduce_tracking(poly_list_new[i], poly_list_now, tracking_list_new[i], tracking_list_now,
                                                                                full_reduced = full_reduced, edit_out = True)
            if poly_list_new[i] == []:
                del(poly_list_new[i])
                del(tracking_list_new[i])
            if edit:
                done = False
    if full_reduce:
        poly_list_new, tracking_list_new = sort_poly_list(poly_list_new, sort_with = tracking_list_new)
        poly_list_new, tracking_list_new = norm_poly_list(poly_list_new, trackers_to_norm = tracking_list_new)
        return poly_list_new, tracking_list_new
    else:
        poly_list_new, tracking_list_new = sort_poly_list(poly_list_new, sort_with = tracking_list_new)
        return poly_list_new, tracking_list_new

#S-polynomial of two sorted polynomials
def S_poly(poly1, poly2):
    leading_lcm = lcm_mon(poly1[0],poly2[0])
    poly=add_poly( mono_mult(div_mon(leading_lcm,poly1[0]),poly1) , neg_poly(mono_mult(div_mon(leading_lcm,poly2[0]),poly2)) )
    return sort_poly(poly)

#S-polynomial of two sorted polynomials while tracking and repeating the S-polynomial computation in a second polynomial pair
def S_poly_track(poly1, poly2, track1, track2):
    leading_lcm = lcm_mon(poly1[0],poly2[0])
    term1 = div_mon(leading_lcm,poly1[0])
    term2 = neg_poly([div_mon(leading_lcm, poly2[0])])
    poly = add_poly(mono_mult(term1, poly1) , mult_poly(term2, poly2))
    track = []
    for i in range(len(track1)):
        track.append(sort_poly(add_poly(mono_mult(term1, track1[i]) , mult_poly(term2, track2[i]))))
    return sort_poly(poly), track

#G-polynomail of two sorted polynomials
def G_poly(poly1, poly2):
    leading_lcm = lcm_mon(poly1[0],poly2[0])
    leading_lcm[0] = 1
    divisor, coef1, coef2 = xgcd(poly1[0][0],poly2[0][0])
    poly=add_poly( coef_mult(mono_mult(div_mon(leading_lcm,poly1[0]),poly1),coef1) , coef_mult(mono_mult(div_mon(leading_lcm,poly2[0]),poly2),coef2) )
    return sort_poly(poly)

#G-polynomail of two sorted polynomials while tracking and repeating the G-polynomial computation in a second polynomial pair
def G_poly_track(poly1, poly2, track1, track2):
    leading_lcm = lcm_mon(poly1[0],poly2[0])
    leading_lcm[0] = 1
    divisor, coef1, coef2 = xgcd(poly1[0][0],poly2[0][0])
    term1 = coef_mult([div_mon(leading_lcm, poly1[0])], coef1)
    term2 = coef_mult([div_mon(leading_lcm, poly2[0])], coef2)
    poly = add_poly(mult_poly(term1, poly1), mult_poly(term2, poly2))
    track = []
    for i in range(len(track1)):
        track.append(sort_poly(add_poly(mult_poly(term1, track1[i]), mult_poly(term2, track2[i]))))
    return sort_poly(poly), track

#gromber basis of set of polynomials
def grobner(poly_list, reduced = True, dim_ranges = [], max_dims = [], progress_output = True):
    if progress_output:
        print("\n Grobner basis progress:")
    run = 0 
    grobner_basis = sort_poly_list(poly_list)
    pairs = []
    for i in range(len(grobner_basis)):
        for j in range(i+1,len(grobner_basis)):
            pairs.append([grobner_basis[i],grobner_basis[j]])
    pairs_to_add = []
    pairs_to_check=copy.deepcopy(pairs)
    while pairs != []:
        while pairs_to_check != []:
            for i in range(len(pairs_to_check)-1,-1,-1):
                G_pair_reduce = True
                for g in range(len(grobner_basis)):
                    if div_check(lcm_mon(pairs_to_check[i][0][0],pairs_to_check[i][1][0]),grobner_basis[g][0]) == True and pairs_to_check[i][0][0][0]%grobner_basis[g][0][0]==0 and pairs_to_check[i][1][0][0]%grobner_basis[g][0][0]==0:
                        G_pair_reduce = False
                        break
                if G_pair_reduce == True:
                    temp_poly = G_poly(pairs_to_check[i][0], pairs_to_check[i][1])
                    if len(temp_poly) != 0:
                        temp_poly = norm_poly_list([list_reduce(temp_poly, grobner_basis, full_reduced = reduced)])[0]
                        if len(temp_poly) != 0:
                            if dim_range_check(temp_poly[0], dim_ranges, max_dims):
                                for g in range(len(grobner_basis)):
                                    pairs_to_add.append([grobner_basis[g],temp_poly])
                                grobner_basis.append(temp_poly)
                del(pairs_to_check[i])
        for i in range(len(pairs)-1,-1,-1):
            temp_poly = S_poly(pairs[i][0], pairs[i][1])
            if len(temp_poly) != 0:
                temp_poly = list_reduce(temp_poly, grobner_basis, full_reduced = reduced)
                if len(temp_poly) != 0:
                    if dim_range_check(temp_poly[0], dim_ranges, max_dims):
                        temp_poly = norm_poly_list([temp_poly])[0]
                        for g in range(len(grobner_basis)):
                            pairs_to_add.append([grobner_basis[g],temp_poly])
                        grobner_basis.append(temp_poly)
            del(pairs[i])       
        run += 1
        if progress_output:
            print('Loop '+str(run)+', current length of generators '+str(len(grobner_basis))+', size of next batch of pairs '+str(len(pairs_to_add)))
        pairs += pairs_to_add
        pairs_to_check = copy.deepcopy(pairs_to_add)
        pairs_to_add = []
        if progress_output:
            print('Reducing...')
        if reduced:
            grobner_basis = reduce_list(grobner_basis, full_reduced = True)       
    return grobner_basis

#gromber basis of set of polynomials alos tracking the reduction form the view of the origal idela generators
def grobner_tracking(poly_list, reduced = True, dim_ranges = [], max_dims = [], progress_output = True):
    if progress_output:
        print("\n Grobner basis progress:")
    run = 0
    len_of_ideal = len(poly_list)
    grobner_ideal_corespondence = []
    term_number = len(poly_list[0][0][1])
    for i in range(len_of_ideal):
        grobner_ideal_corespondence.append([])
        for j in range(len_of_ideal):
            if i == j:
                grobner_ideal_corespondence[i].append([[1 , [0]*term_number ]])
            else:
                grobner_ideal_corespondence[i].append([])
    grobner_basis, grobner_ideal_corespondence = sort_poly_list(poly_list, sort_with = grobner_ideal_corespondence)
    pairs = []
    for i in range(len(grobner_basis)):
        for j in range(i+1,len(grobner_basis)):
            pairs.append([[grobner_basis[i], grobner_basis[j]], [grobner_ideal_corespondence[i], grobner_ideal_corespondence[j]]])
    pairs_to_add = []
    pairs_to_check = copy.deepcopy(pairs)
    while pairs != []:
        while pairs_to_check != []:
            for i in range(len(pairs_to_check)-1,-1,-1):
                G_pair_reduce = True
                for g in range(len(grobner_basis)):
                    if div_check(lcm_mon(pairs_to_check[i][0][0][0], pairs_to_check[i][0][1][0]), grobner_basis[g][0]) == True and pairs_to_check[i][0][0][0][0]%grobner_basis[g][0][0]==0 and pairs_to_check[i][0][1][0][0]%grobner_basis[g][0][0]==0:
                        G_pair_reduce = False
                        break
                if G_pair_reduce == True:
                    temp_poly, temp_track = G_poly_track(pairs_to_check[i][0][0], pairs_to_check[i][0][1], pairs_to_check[i][1][0], pairs_to_check[i][1][1])
                    if len(temp_poly) != 0:
                        temp_poly, temp_track = list_reduce_tracking(temp_poly, grobner_basis, temp_track, grobner_ideal_corespondence, full_reduced = reduced)
                        temp_poly, temp_track = norm_poly_list([temp_poly], [temp_track])
                        temp_poly, temp_track = temp_poly[0], temp_track[0]
                        if len(temp_poly) != 0:
                            if dim_range_check(temp_poly[0], dim_ranges, max_dims):
                                for g in range(len(grobner_basis)):
                                    pairs_to_add.append([[grobner_basis[g], temp_poly], [grobner_ideal_corespondence[g], temp_track]])
                                grobner_basis.append(temp_poly)
                                grobner_ideal_corespondence.append(temp_track)
                del(pairs_to_check[i])
        for i in range(len(pairs)-1,-1,-1):
            temp_poly, temp_track = S_poly_track(pairs[i][0][0], pairs[i][0][1], pairs[i][1][0], pairs[i][1][1])#--
            if len(temp_poly) != 0:
                temp_poly, temp_track = list_reduce_tracking(temp_poly, grobner_basis, temp_track, grobner_ideal_corespondence, full_reduced = reduced)
                if len(temp_poly) != 0:
                    if dim_range_check(temp_poly[0], dim_ranges, max_dims):
                        temp_poly, temp_track = norm_poly_list([temp_poly], [temp_track])
                        temp_poly, temp_track = temp_poly[0], temp_track[0]
                        for g in range(len(grobner_basis)):
                            pairs_to_add.append([[grobner_basis[g], temp_poly], [grobner_ideal_corespondence[g], temp_track]])
                        grobner_basis.append(temp_poly)
                        grobner_ideal_corespondence.append(temp_track)
            del(pairs[i])
        run += 1
        if progress_output:
            print('Loop '+str(run)+', current length of generators '+str(len(grobner_basis))+', size of next batch of pairs '+str(len(pairs_to_add)))
        pairs += pairs_to_add
        pairs_to_check = copy.deepcopy(pairs_to_add)
        pairs_to_add = []
        if progress_output:
            print('Reducing...')
        if reduced:
            grobner_basis, grobner_ideal_corespondence = reduce_list_tracking(grobner_basis, grobner_ideal_corespondence, full_reduced = True)
    return grobner_basis, grobner_ideal_corespondence

#Find a reduced Gorbner basis of the interection of two ideal whose generators are epresed as two polynomial lists
def intersection_Grobner(poly_list1_in, poly_list2_in, variables, dim_ranges = [], max_dims = [], grobner_poly_lists_first = False, show_poly_list = True, progress_output = True):
    poly_list = []
    term = [0]*(len(poly_list1_in[0][0][1])+1)
    term[0] = 1
    mon = [1, term]
    if grobner_poly_lists_first:
        poly_list1 = grobner(poly_list1_in, reduced = True, dim_ranges = dim_ranges, max_dims = max_dims, progress_output = progress_output)
        if show_poly_list:
            print("\n Grober basis of first ideal:")
            display_poly_list(poly_list1, variables)
        poly_list2 = grobner(poly_list2_in, reduced = True, dim_ranges = dim_ranges, max_dims = max_dims, progress_output = progress_output)
        if show_poly_list:
            print("\n Grober basis of second ideal:")
            display_poly_list(poly_list2, variables)
    else:
        poly_list1 = poly_list1_in
        poly_list2 = poly_list2_in
    variables = ['t'] + variables
    for i in range(len(dim_ranges)):
        for j in range(len(dim_ranges[i])):
            dim_ranges[i][j] += 1
    
    for poly in poly_list1:
        poly_new = []
        for term in poly:
            temp = copy.deepcopy(term[1])
            temp.insert(0,1)
            poly_term = [term[0],temp]
            poly_new.append(poly_term)
        poly_list.append(poly_new)
    for poly in poly_list2:
        poly_new = []
        for term in poly:
            temp = copy.deepcopy(term[1])
            temp.insert(0,0)
            poly_term = [term[0],temp]
            poly_new.append(poly_term)
            temp = copy.deepcopy(term[1])
            temp.insert(0,1)
            poly_term = [-term[0],temp]
            poly_new.append(poly_term)
        poly_list.append(poly_new)
    Intersection_Grobner = remove_polys_containing(grobner(poly_list, reduced = True, dim_ranges = dim_ranges, max_dims = max_dims, progress_output = progress_output), mon)
    return remove_highest_var(Intersection_Grobner)

#Syzygy Grobner basis of a Grobner basis
def Syzygy(Grobner_bais, remove_trivial_syz = True, dim_ranges = [], max_dims = []): 
    Syzygy_Grobner = []
    for i in range(1, len(Grobner_bais)):
        for j in range(i):
            non_triaval = True
            not_out_of_range = True
            leading_lcm = lcm_mon(Grobner_bais[i][0], Grobner_bais[j][0])
            m1 = div_mon(leading_lcm, Grobner_bais[i][0])
            m2 = div_mon(leading_lcm, Grobner_bais[j][0])
            S = sort_poly(add_poly( mono_mult(m1, Grobner_bais[i]) , neg_poly(mono_mult(m2, Grobner_bais[j])) ))
            syz = list_reduce(S, Grobner_bais, full_reduced = True, edit_out = False, reduction_out = True)[1]
            syz[i] = add_poly(neg_poly(syz[i]), [m1])
            syz[j] = add_poly(neg_poly(syz[j]), neg_poly([m2]))
            for p in range(len(syz)):
                syz[p] = sort_poly(syz[p])
            if remove_trivial_syz:
                for p in range(len(syz)):
                    for g in range(len(Grobner_bais)):
                        if Grobner_bais[g] == syz[p]:
                            non_triaval = False
                            break
                    if not non_triaval:#tab in???
                        break
            if dim_ranges != []:
                for p in range(len(syz)):
                    if syz[p] != []:
                        not_out_of_range = dim_range_check(mono_mult(syz[p][0],[Grobner_bais[p][0]])[0], dim_ranges, max_dims)
                        if not not_out_of_range:
                            break
            if syz != [] and non_triaval and not_out_of_range:#tab in???
                Syzygy_Grobner.append(syz)
    return Syzygy_Grobner

