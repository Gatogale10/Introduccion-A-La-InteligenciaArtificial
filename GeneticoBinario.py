import math
import random


#Generamos a los padres con un aleatorio de

def Conversion(li,ui,ki,bi):

    return li + (  (ki*(ui-li)) / ((2**bi)-1)    )


def ObtenerBits(ui,li,m):

    return math.floor( math.log2( (ui-li)*(10**m) ) +0.99 )

def PoblacionI():
    #Como son dos variables se calcula un tipo como un vector en R^2
    # O sea vamos a calcularlos o dar a los habitantes iniciales como arreglos de dos elementos
    #Se va a crear una poblacion aleatoria de 20.

    #Es el valor del x1:
    b1 = ObtenerBits(5, -5, 2)
    print(b1)

    #Es el valor de x2:
    b2 = ObtenerBits(8,-8,2)
    print(b2)

    #Vamos a generar a 20 individuos aleatoriamente como poblacion inicial
    pob = []
    for i in range(20):
        x1 = random.randint(0,(2**(b1))-1)
        x2 = random.randint(0, (2**(b2))-1)
        x3 = random.randint(0,(2**(b1+b2))-1)

        #Ahora el individuo n va a tener esto junto
        x1 = x1 << b2

        pob.append(x3)
        #pob.append(x1^x2)

    #Notemos que hay 20 individuos con el x1 y x2 dentro de el a nivel de bits
    # x1 esta en la parte entre 2**(b1+b2-1) y 2**(b2-1) y x2 2**(b2-1) y 0

    return pob

def funcAptitud(Ind,b1,b2):

    #Vamos a cortar los bits donde corresponde y transformarlos a su representacion en decimal
    x1 = Ind & (  ( (2**(b1+b2) )-1) - ( (2**(b2))-1)  )
    x1 = x1 >> b2
    x2 = Ind & ( (2**(b2))-1  )

    #Transformamos esto a reales
    #Nota: los valores de li y ui pueden cambiar.

    x1r = Conversion(-5,5,x1,b1)
    x2r = Conversion(-8, 8, x2, b2)

    #Evaluamos en la funcion dada
    # La funcion de igual forma puede cambiar

    y = (x1r**2) + (x2r**2)

    return y

def barajar(lista):
  N = len(lista)

  lista1 = random.sample(lista,N )
  lista2 = random.sample(lista1,N)
  lista3 = random.sample(lista2,N)

  return lista3

def Aptipob(pob,b1,b2):

    poba = []

    for i in range(len(pob)):
        y = funcAptitud(pob[i],b1,b2)

        poba.append(y)

    return poba


def Torneo(pob,b1,b2):

    #Realizamos un barajeo para cada poblacion
    #Necesitamos una poblacion para hacer el torneo

    pob1 = barajar(pob)
    pob1a = Aptipob(pob1,b1,b2)
    torneo1 = []

    for i in range(int(len(pob1)/2)):

        if pob1a[2*i] <= pob1a[2*i+1]:
            torneo1.append(pob1[2*i])

        else:
            torneo1.append(pob1[2*i+1])




    return torneo1

def cruza(pob1,pob2,b1,b2,p,pf):

    #Vamos a cortar en el bit b1+b2-3

    print(f"Poblacion en cruza {pob1}")

    #Cortamos aqui
    #       |
    #       |
    # 0 0 1 | 0 1 0 0 1   0 1 1 1 1 1 0 1
    #      x1                x2


    #Aqui si necesitamos dos poblaciones
    pobc = []
    s = random.randint(0, b1 + b2)



    for i in range(pf):

        if pob2[i] == pob1[i]:
            pobc.append(pob1[i])
        else:

            a = random.random()
            if a < p:

                h1 = pob1[i] & (((2 ** (b1 + b2)) - 1) - ((2 ** (b1 + b2 - s)) - 1))
                h1 = h1 ^ (pob2[i] & (((2 ** (b1 + b2 - s)) - 1)))

                h2 = pob2[i] & (((2 ** (b1 + b2)) - 1) - ((2 ** (b1 + b2 - s)) - 1))
                h2 = h2 ^ (pob1[i] & (((2 ** (b1 + b2 - s)) - 1)))

                pobc.append(h1)
                pobc.append(h2)

            else:

                pobc.append(pob1[i])
                pobc.append(pob2[i])




    return pobc


def hijos(pob1,pob2,b1,b2):

    hij = []

    for i in range(len(pob1)):

        h1 , h2 = cruza(pob1[i],pob2[i],b1,b2,random.random())
        hij.append(h1)
        hij.append(h2)


    return hij


def mutacion(pob,p):

    #Generamos un numero aleatorio entre 0 y 1 para ver si mutamos o no al individuo

    for i in range(len(pob)):
        a = random.random()
        if a < p:

            # Mutamos el bit numero 10
            m = random.randint(0,b1+b2)

            # Vemos si esta prendido el bit 10

            a = pob[i] & (2**(m))

            # Si el bit esta prendido lo quitamos si no lo agregamos

            if a > 0:
                pob[i] = pob[i] - a

            else:
                pob[i] = pob[i] + (2 ** (m))

    return pob

def estrategiaevol(pob,b1,b2):

    pob1 = pob.copy()
    """
    if len(pob1)<20:
        for i in range(20-len(pob1)):
            pob1.append( random.randint(0,(2**(b1+b2))-1))
    """

    poba = Aptipob(pob1,b1,b2)

    #Vemos a los mas aptos
    pobma = sorted(poba)



    pobf = []

    for i in range(int(len(pobma)/2)):

        pobf.append( pob[  poba.index( pobma[i] )  ]  )

    return pobf


def epoca(pob, p1,p2,u1,l1,u2,l2,b1,b2):

    #Esta funcion nos genera una epoca


    #Primero se barajea la población dos veces


    #Despues Realizamos el torneo

    pob1 = Torneo(pob,b1,b2)
    pob2 = Torneo(pob,b1,b2)


    #Enseguida se realiza la cruza (si hay valores repetidos se almacena un valor , no los dos padres)
    pobc = cruza(pob1,pob2,b1,b2,p1, len(pob1))


    #Si la poblacion cruzada es menor entonces se realizara mas torneo hasta llenar a los 20 individuos

    for i in range(len(pob)-len(pobc)):
        x3 = random.randint(0, (2 ** (b1 + b2)) - 1)
        pobc.append(x3)


    # Mutacion
    pobbm = mutacion(pobc,p2)

    # Ahora mezclamos a padres y hijos escogemos a los mas aptos

    pobe = pob+ pobbm



    #pobs = list(set(pob))

    #Escogemos a los mas aptos de los 40 nos quedamos con 20.

    poblacionfinal = estrategiaevol(pobe,b1,b2)


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

    #Los bits correspondientes
    b1 = ObtenerBits(u1, l1, 2)
    b2 = ObtenerBits(u2, l2, 2)


    pob = PoblacionI()


    #Vamos a realizar 10 epocas o generaciones

    for i in range(100):
        print(f"===========================================Epocaaaaa {i} =========================================")

        pob = epoca(pob,p1,p2,u1,l1,u2,l2,b1,b2)
        print(f"\n Esta es la poblacion de la epoca {i + 1} : {pob}")
        print(f"Esta aptitud es la poblacion de la epoca {i + 1}: {Aptipob(pob,b1,b2)} \n")

        print("===============================================================================================")








    





