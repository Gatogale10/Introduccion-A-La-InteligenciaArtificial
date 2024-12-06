#Instituto Politecnico Nacional
#Autor: Jorge Gael Lopez Figueras
#Algoritmo genetico con representacion real


import math
import random



def PoblacionI():
    #Como son dos variables se calcula un tipo como un vector en R^2
    # O sea vamos a calcularlos o dar a los habitantes iniciales como arreglos de dos elementos
    #Se va a crear una poblacion aleatoria de 20.


    #Primero generamos a los individuos

    #Vamos a generar a 20 individuos aleatoriamente como poblacion inicial
    pob = []
    for i in range(20):
        x1 = 5  + random.random()*(-10)
        x2 = 8 + random.random()*(-16)

        x3 = [x1,x2]

        #La poblacion se compone de listas estas listas se componen de dos elementos
        pob.append(x3)



    return pob

def funcAptitud(x):

    y = (x[0]**2) + (x[1]**2)

    return y


def barajar(lista):
  N = len(lista)

  lista1 = random.sample(lista,N )
  lista2 = random.sample(lista1,N)
  lista3 = random.sample(lista2,N)

  return lista3

def Aptipob(pob):

    poba = []

    for i in range(len(pob)):
        y = funcAptitud(pob[i])

        poba.append(y)

    return poba


def Torneo(pob):

    #Realizamos un barajeo para cada poblacion
    #Necesitamos una poblacion para hacer el torneo

    pob1 = barajar(pob)
    pob1a = Aptipob(pob1)
    torneo1 = []

    for i in range(int(len(pob1)/2)):

        if pob1a[2*i] <= pob1a[2*i+1]:
            torneo1.append(pob1[2*i])

        else:
            torneo1.append(pob1[2*i+1])




    return torneo1

def cruza(pob1,pob2,p,pf):

    #Vamos a cortar en el bit b1+b2-3

    print(f"Poblacion en cruza {pob1}")




    #Aqui si necesitamos dos poblaciones
    pobc = []
    s = random.random()


    for i in range(pf):
        h1_x= []
        h2_x = []

        if pob2[i] == pob1[i]:
            pobc.append(pob1[i])
        else:
            a = random.random()
            if a < p:

                #Esto es para es x1
                h1_x.append((s-1)*pob1[i][0] + s*pob2[i][0])

                #Esto es para x2 del hijo 1
                h1_x.append((s-1)*pob1[i][1]+ s*pob2[i][1])

                # Esto es para es x1
                h2_x.append((s) * pob1[i][0] + (s-1) * pob2[i][0])

                # Esto es para x2 del hijo 1
                h2_x.append((s) * pob1[i][1] + (s-1) * pob2[i][1])


                pobc.append(h1_x)
                pobc.append(h2_x)

            else:

                pobc.append(pob1[i])
                pobc.append(pob2[i])




    return pobc


def mutacion(pob,p,t,T):

    #Generamos un numero aleatorio entre 0 y 1 para ver si mutamos o no al individuo
    #Notemos que la poblacion esta ordenada de menor a mayor

    #Vamos a ver a quien vamos a mutar

    m = random.randint(0,len(pob)-1)

    #Vamos a ver si lo vamos a mutar
    a = random.random()


    if a < p:

        #Generamos un numero aleatorio entre 0 y 1

        r = random.random()

        # Mutamos a su x1
        y1 = pob[len(pob) - 1][0] - pob[m][0]

        y2 = pob[len(pob) - 1][1] - pob[m][1]

        Delt1 = y1 * (1 - ((r ** (1 - t / T)) ** 5))
        Delt2 = y2 * (1 - ((r ** (1 - t / T)) ** 5))

        if r < 0.5:


            v1 = pob[m][0] + Delt1
            v2 = pob[m][1] +  Delt2

        else:

            v1 = pob[m][0] - Delt1
            v2 = pob[m][1] - Delt2

        pob[m] = [v1, v2]





    return pob

def estrategiaevol(pob):

    pob1 = pob.copy()
    """
    if len(pob1)<20:
        for i in range(20-len(pob1)):
            pob1.append( random.randint(0,(2**(b1+b2))-1))
    """

    poba = Aptipob(pob1)

    #Vemos a los mas aptos
    pobma = sorted(poba)
    print(f"Poblacion sorteada aptitudes: {pobma}")


    pobf = []

    for i in range(int(len(pobma)/2)):

        pobf.append( pob[  poba.index( pobma[i] )  ]  )
    print(f"Poblacion sorteada individuos: {pobf}\n")

    return pobf


def epoca(pob, p1,p2,t,T):

    #Esta funcion nos genera una epoca


    #Primero se barajea la población dos veces


    #Despues Realizamos el torneo

    pob1 = Torneo(pob)
    pob2 = Torneo(pob)


    #Enseguida se realiza la cruza (si hay valores repetidos se almacena un valor , no los dos padres)
    pobc = cruza(pob1,pob2,p1, len(pob1))


    #Si la poblacion cruzada es menor entonces se realizara mas torneo hasta llenar a los 20 individuos

    for i in range(len(pob)-len(pobc)):
        x1 = 5 + random.random() * (-10)
        x2 = 16 + random.random() * (-8)
        pobc.append([x1,x2])


    # Mutacion
    pobbm = mutacion(pobc,p2,t,T)

    # Ahora mezclamos a padres y hijos escogemos a los mas aptos

    pobe = pob+ pobbm



    #pobs = list(set(pob))

    #Escogemos a los mas aptos de los 40 nos quedamos con 20.

    poblacionfinal = estrategiaevol(pobe)


    return poblacionfinal




if __name__ == '__main__':

    #Estos son los valores que vamos a estar usando

    p1 = 0.9 #Probabilidad de cruza
    p2 = 0.2 #Probabilidad de mutacion

    #Intervalos
    u1 = 5
    l1 = -5

    u2 = 8
    l2 = -8




    pob = PoblacionI()
    print(f"Esta es la población inicial {pob} \n \n")


    #Vamos a realizar 10 epocas o generaciones
    T = 100

    for i in range(T):
        print(f"\n ======================================================================Epocaaaaa {i+1} ===========================================================\n ")

        pob = epoca(pob,p1,p2,i+1,T)
        print(f"\n Esta es la poblacion de la epoca {i+1} : {pob}")
        print(f"Esta aptitud es la poblacion de la epoca {i+1}: {Aptipob(pob)} \n")

        print("=======================================================================================================================================================\n")


