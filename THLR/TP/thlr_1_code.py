l1 = [1,3,5,7,9]
l2 = [0,4,2,6,8]
l3 = [7,1,9,4,5,2,6]

impair = set(l1)
pair = set(l2)
random = set(l3)

#[Q9]
def union(E,F):
    temp = set([])
    for elt in E:
        temp.add(elt)
    for elt in F:
        temp.add(elt)
    res = set(list(temp))
    return res
#[/Q9]

#[Q10]
def intersection(E,F):
    l = []
    for elt in E:
        if elt in F:
            l.append(elt)
    res = set(l)
    return res   
#[/Q10]

#[Q11]
def subtraction(E,F):
    l = []
    for elt in E:
        if not elt in F:
            l.append(elt)
    return set(l)
#[/Q11]

#[Q12]
def diff(E,F):
    unionSet = union(E,F)
    interSet = intersection(E,F)
    return subtraction(unionSet,interSet)
#[/Q12]
def sublists(l):
    if l==[]:
        return [[]]
    else:
        res = []
        sublists(l[1:]) # Pas fini
#[Q13]

#[/Q13]