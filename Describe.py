import pandas as pd 
import math
donnees = pd.read_excel(r'C:\Users\XPS\Desktop\dataset.xlsx')
print(donnees)


index_list = donnees.index.tolist()
print(index_list)
Arithmancy_list = donnees.Arithmancy.tolist()
print(Arithmancy_list)
Astronomy_list = donnees.Astronomy.tolist()
print(Astronomy_list)
Herbology_list = donnees.Herbology.tolist()
print(Herbology_list)
DefenseAgainstTheDarkArts_list = donnees.DefenseAgainstTheDarkArts.tolist()
print(DefenseAgainstTheDarkArts_list)
Divination_list = donnees.Divination.tolist()
print(Divination_list)
MuggleStudies_list = donnees.MuggleStudies.tolist()
print(MuggleStudies_list) 
AncientRunes_list = donnees.AncientRunes.tolist()
print(AncientRunes_list)
HistoryOfMagic_list = donnees.HistoryOfMagic.tolist()
print(HistoryOfMagic_list)
Transfiguration_list = donnees.Transfiguration.tolist()
print(Transfiguration_list)
Potions_list = donnees.Potions.tolist()
print(Potions_list)
CareOfMagicalCreatures_list = donnees.CareOfMagicalCreatures.tolist()
print(CareOfMagicalCreatures_list)
Charms_list = donnees.Charms.tolist()
print(Charms_list)
Flying_list = donnees.Flying.tolist()
print(Flying_list)
Arithmancy_list_without_nan=[x for x in Arithmancy_list if not math.isnan(x)]
Astronomy_list_without_nan=[x for x in Astronomy_list if not math.isnan(x)]
Herbology_list_without_nan=[x for x in Herbology_list if not math.isnan(x)]
DefenseAgainstTheDarkArts_list_without_nan=[x for x in DefenseAgainstTheDarkArts_list if not math.isnan(x)]
Divination_list_without_nan=[x for x in Divination_list if not math.isnan(x)]
MuggleStudies_list_without_nan=[x for x in MuggleStudies_list if not math.isnan(x)]
AncientRunes_list_without_nan=[x for x in AncientRunes_list if not math.isnan(x)]
HistoryOfMagic_list_without_nan=[x for x in HistoryOfMagic_list if not math.isnan(x)]
Transfiguration_list_without_nan=[x for x in Transfiguration_list if not math.isnan(x)]
Potions_list_without_nan=[x for x in Potions_list if not math.isnan(x)]
CareOfMagicalCreatures_list_without_nan=[x for x in CareOfMagicalCreatures_list if not math.isnan(x)]
Charms_list_without_nan=[x for x in Charms_list if not math.isnan(x)]
Flying_list_without_nan=[x for x in Flying_list if not math.isnan(x)]


def count(L):
    k=0
    for x in L:
            k=k+1
    return k

def mean(L):
    s=0
    for x in L:
        s=s+x
    return s/count(L)

def minimum(L):
    k=L[0]
    for x in L:
        if x<k:
            k=x
    return k

def maximum(L):
    k=L[0]
    for x in L:
        if x>k:
            k=x
    return k
    
def std(L):
    k=0
    s=0
    for x in L:
        k=k+(x-mean(L))**2
        s=s+x
    return math.sqrt(k/s)

def Q1(L):
    n=count(L)
    T=sorted(L)
    if n%4==0:
        return (T[n/4]+T[n/4+1])/2
    return T[n//4]

def Q2(L):
    n=count(L)
    T=sorted(L)
    if n%2==0:
        return (T[n/2]+T[(n/2)+1])/2
    return T[n//2]

def Q3(L):
    n=count(L)
    T=sorted(L)
    if n%(3/4)==0:
        return (T[3*n/4]+T[(3*n/4)+1])/2
    return T[3*n//4]


def afficher(L):
    print(count(L))
    print(mean(L))
    print(minimum(L))
    print(maximum(L))
    print(std(L))
    print(Q1(L))
    print(Q2(L))
    print(Q3(L))


    








