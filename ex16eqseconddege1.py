print("l'équation de second degré s'écrit sous la forme de ax²+bx+c=0 entrer les coefficient svp : ")
a=float(input("entrer le coefficient a : "))
b=float(input("entrer le coefficient b : "))
c=float(input("entrer le coefficient c : "))
if b**b-4*a*c>0 : 
    print("les solutions sont s1 : ", (-b+(b**b-4*a*c)**1/2)/2*a ," s2 : ",  (-b-(b**b-4*a*c)**1/2)/2*a)
elif b**b-4*a*c == 0 : 
    print("vous avez une solution s1 : " , -b/2*a)
else :
    print("pas de solutions réels")