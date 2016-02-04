import random
import collections
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import binom
import math

#C(n,k) => from scipy.special import binom
#binom(N,k)

def count_words(words):
    return collections.Counter(words)
    
def get_liste_aleat():
    liste = []
    for i in range(0,1000):
        liste.append(random.randint(0,1))
    return liste


#evolution progressive de la proba
#loglog =>
#semilog => quand function  f(x) = Ae^bx , faire log[f[x]] = logA + bx=> obtention d'une droite
#loglog => f(x) = Ax^b )> log(f(x)) = log(A)+ b*log(x)
#la proba diminue d'avoir un 1 pour p1 = 0.1 quand le nombre de tirage augmente
def tracerGraphe(p1,N):
    ma_liste = []
    ordonne = [1*r for r in range(1,N)]
    for r in ordonne:
         #dic = count_words(get_liste_aleat())
         #r = dic[1]
         ma_liste.append(np.power(p1,r)*np.power((1-p1),(N-r)))
    plt.semilogy(ordonne,ma_liste)
    plt.xlabel('Number of elements 1')
    plt.ylabel('Espace des probabilites')
    plt.title('Concentration de la mesure')
    plt.show()

# 1 element parmis 11 peu de combinaisons, pareil pour trouver les combinaisons de 10 elements parmis 11

def tracerGrapheBinome(N):
    ma_liste = []
    ordonne = [1*r for r in range(1,N)]
    for r in ordonne:
         ma_liste.append(binom(N,r))
    plt.semilogy(ordonne,ma_liste)
    plt.xlabel('r')
    plt.ylabel('Nombre de combinaisons')
    plt.title('Binome de newton')
    plt.show()

def tracerGrapheBinome(N,p1):
    ma_liste = []
    mes_moyennes = []
    ma_variance = []
    ordonne = [1*r for r in range(0,N)]
    for r in ordonne:
         ma_liste.append(binom(N,r)*np.power(p1,r)*np.power((1-p1),(N-r)))
    for i in range(1,N+1):
        #mes_moyennes.append(np.mean(ma_liste[:i])/np.var(ma_liste[:i]))
        mes_moyennes.append( math.sqrt(i * p1 *( 1- p1))/ (i*p1))
    print(len(mes_moyennes))
    plt.semilogy(ordonne,ma_liste)
    plt.xlabel('r')
    plt.ylabel('Probas * nombre de combinaisons')
    plt.title('Produit P avec le graphe de newton')
    plt.show()
    plt.plot(ordonne,mes_moyennes)
    plt.xlabel('r')
    plt.ylabel('Probas * nombre de combinaisons')
    plt.title('Produit P avec le graphe de newton')
    plt.show()

def tracer(N,p1):
    ma_liste = []
    final = []
    vals = [0.01 *r for r in range(0,50)]
    ordonne = [1*r for r in range(0,N)]
    for r in ordonne:
        ma_liste.append(binom(N,r)*np.power(p1,r)*np.power((1-p1),(N-r)))
    for e in vals:
        l = list (ma_liste) #copy.copy (ma\liste)
        to_add = []
        for s in range(N):
            if(l[s]>e):
                to_add.append(l[s])
        final.append(math.log(len(to_add),2))
    plt.semilogy(vals,final)
    plt.xlabel('r')
    plt.ylabel('Probas * nombre de combinaisons')
    plt.title('Produit P avec le graphe de newton')
    plt.show()  


 
#tracerGraphe(0.1,100)
#tracerGraphe(0.1,1000)
#tracerGrapheBinome(100)
#tracerGrapheBinome(1000)
#tracerGrapheBinome(1000,0.1)
tracer(100,0.1)
