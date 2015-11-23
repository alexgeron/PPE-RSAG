

from math import * 
recommencer=0 
while recommencer!=1:
    print ("Programme qui calcule les racines d'un polynome du second degré .")
    print ("Tel que Ax²+Bx+C=0")
    A=input('A=') 
    B=input('B=') 
    C=input('C=') 
    delta=B*B-4*A*C 
    print ("Delta=",delta )
    if delta <0:
        print ("Pas de solutions" )
    if delta ==0:
        print ("Une solution") 
        x=-B/2*A 
        print ("X=",x)
    if delta >0:
        print ("Deux solutions") 
        racine_carre_delta=sqrt(delta) 
        l=-B+racine_carre_delta 
        m=2*A 
        x1=k/m 
        x2=l/m 
        print ("X1=",x1) 
        print ("X2=",x2) 
    print ("Fin du programme!")
    print ("Voulez-vous recommencer ?")
    recommencer=input('0. Oui\n1. Non\n')
