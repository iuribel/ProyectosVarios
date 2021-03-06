# -*- coding: utf-8 -*-
"""huga.ipynb laberinto ratón

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pEmDv0jZe2-CEvKrPm67H5YtX831nTRU
"""


import random



def fueraDeMatriz(x,y,cuadro):
  if x<0 or x > len(cuadro)-1 or y < 0 or y > len(cuadro)-1:
    return True

def cuadroAux (n):
  l = [(['0'] * n) for i in range(n)]  # se hace la matriz y se llena de ceros
  return l

def cuadro (n, porcAz, porcGu, porcVe ):

  l=[(['0']*n) for i in range(n)] # se hace la matriz y se llena de ceros    

  Azucar= int(0.01*porcAz*n*n) # cantidad de cassilas con azucar
  Guaro= int(0.01*porcGu*n*n) # cantidad de cassilas con guaro
  Veneno= int(0.01*porcVe*n*n) #cantidad de casillas con veneno

  l[0][0]= 'E'
  l[n-1][n-1]= 'S'

  for i in range(Azucar):
    x=random.randint(1,n-2)
    y=random.randint(1,n-2)
    l[x][y] = 'A'

  for i in range(Guaro):
    while True:
      x=random.randint(1,n-2)
      y=random.randint(1,n-2)
      if l[x][y] != 'A':
        l[x][y] = 'G'
        break
  
  for i in range(Veneno):
    while True:
     x=random.randint(1,n-2)
     y=random.randint(1,n-2)
     if l[x][y] != 'A' and l[x][y] != 'G':
       l[x][y] = "V"
       break
  
  return l

def imprimirCuadro(cuadro,cuadroAux):
  for i in range(len(cuadro)):
    print(cuadroAux[i] , "  ||  ", cuadro[i])


def juego (cuadro , cuadroAux):
  numChichones=0
  numAzucares=0
  numGuaros=0
  numVeneno=0
  count=0
  posicion=[0,0] # posicion.index(0) ->x   posicion.index(1) ->y
  Result=""
  com= ''
  while True:
    imprimirCuadro(cuadro, cuadroAux)
    print("Chichones: ",numChichones," Azucares: ",numAzucares," Guaros: ",numGuaros, " Venenos: ",numVeneno)
    print("Cuenta: ", count)
    print("Posicion: ", posicion)
    print("¿Que dirección quiere tomar? ")
    print("1. izquierda")
    print("2. derecha")
    print("3. abajo")
    print("4. arriba")
    print("5. salir de la partida")
    decision = int(input ( "escriba el numero: "))

    if decision==1:
      posicion[1] = posicion[1] - 1
      if fueraDeMatriz(posicion[0], posicion[1], cuadro):
        numChichones += 1
        posicion[1] = posicion[1] + 1
        if numChichones >= 10 :
          Result="el raton muere por daño cerebral"
          break
      else:
        count += 1
        if cuadro[posicion[0]][posicion[1]] == 'A':
          numAzucares += 1
          if numGuaros>0:
            numGuaros-=1
            numAzucares-=1
        elif cuadro[posicion[0]][posicion[1]] == 'G':
          numGuaros += 1
          if numAzucares > 0:
            numAzucares -= 1
            numGuaros -= 1
          elif numGuaros >= 3 and numVeneno > 0:
            numGuaros -= 3
            numVeneno -= 1
          elif numGuaros >= 5:
            Result = "el raton muere por cirrosis "
            break
        elif cuadro[posicion[0]][posicion[1]] == 'V':
          numVeneno += 1
          if numGuaros<3:
            Result = "el raton muere envenenado "
            break
        elif cuadro[posicion[0]][posicion[1]] == 'S':
          Result = "El raton logró salir del laberinto "
          break
        cuadro[posicion[0]][posicion[1]] = com + str(count) + com
        cuadroAux[posicion[0]][posicion[1]] = com + str(count) + com
    elif decision == 2:
      posicion[1] = posicion[1] + 1
      if fueraDeMatriz(posicion[0], posicion[1], cuadro):
        numChichones += 1
        posicion[1] = posicion[1] - 1
        if numChichones >= 10:
          Result = "el raton muere por daño cerebral"
          break
      else:
        count += 1
        if cuadro[posicion[0]][posicion[1]] == 'A':
          numAzucares += 1
          if numGuaros > 0:
            numGuaros -= 1
            numAzucares -= 1
        elif cuadro[posicion[0]][posicion[1]] == 'G':
          numGuaros += 1
          if numAzucares > 0:
            numAzucares -= 1
            numGuaros -= 1
          elif numGuaros >= 3 and numVeneno > 0:
            numGuaros -= 3
            numVeneno -= 1
          elif numGuaros >= 5:
            Result = "el raton muere por cirrosis "
            break
        elif cuadro[posicion[0]][posicion[1]] == 'V':
          numVeneno += 1
          if numGuaros < 3:
            Result = "el raton muere envenenado "
            break
        elif cuadro[posicion[0]][posicion[1]] == 'S':
          cuadro[posicion[0]][posicion[1]] = com + str(count) + com
          Result = "El raton logró salir del laberinto "
          break
        cuadro[posicion[0]][posicion[1]] = com + str(count) + com
        cuadroAux[posicion[0]][posicion[1]] = com + str(count) + com
    elif decision == 3:
      posicion[0] = posicion[0] + 1
      if fueraDeMatriz(posicion[0], posicion[1], cuadro):
        numChichones += 1
        posicion[0] = posicion[0] - 1
        if numChichones >= 10:
          Result = "el raton muere por daño cerebral"
          break
      else:
        count += 1
        if cuadro[posicion[0]][posicion[1]] == 'A':
          numAzucares += 1
          if numGuaros > 0:
            numGuaros -= 1
            numAzucares -= 1
        elif cuadro[posicion[0]][posicion[1]] == 'G':
          numGuaros += 1
          if numAzucares > 0:
            numAzucares -= 1
            numGuaros -= 1
          elif numGuaros >= 3 and numVeneno > 0:
            numGuaros -= 3
            numVeneno -= 1
          elif numGuaros >= 5:
            Result = "el raton muere por cirrosis "
            break
        elif cuadro[posicion[0]][posicion[1]] == 'V':
          numVeneno += 1
          if numGuaros < 3:
            Result = "el raton muere envenenado "
            break
        elif cuadro[posicion[0]][posicion[1]] == 'S':
          cuadro[posicion[0]][posicion[1]] = com + str(count) + com
          cuadroAux[posicion[0]][posicion[1]] = com + str(count) + com
          Result = "El raton logró salir del laberinto "
          break
        cuadro[posicion[0]][posicion[1]] = com + str(count) + com
        cuadroAux[posicion[0]][posicion[1]] = com + str(count) + com
    elif decision == 4:
      posicion[0] = posicion[0] - 1
      if fueraDeMatriz(posicion[0], posicion[1], cuadro):
        numChichones += 1
        posicion[0] = posicion[0] + 1
        if numChichones >= 10:
          Result = "el raton muere por daño cerebral"
          break
      else:
        count += 1
        if cuadro[posicion[0]][posicion[1]] == 'A':
          numAzucares += 1
          if numGuaros > 0:
            numGuaros -= 1
            numAzucares -= 1
        elif cuadro[posicion[0]][posicion[1]] == 'G':
          numGuaros += 1
          if numAzucares > 0:
            numAzucares -= 1
            numGuaros -= 1
          elif numGuaros >= 3 and numVeneno > 0:
            numGuaros -= 3
            numVeneno -= 1
          elif numGuaros >= 5:
            Result = "el raton muere por cirrosis "
            break
        elif cuadro[posicion[0]][posicion[1]] == 'V':
          numVeneno += 1
          if numGuaros < 3:
            Result = "el raton muere envenenado "
            break
        elif cuadro[posicion[0]][posicion[1]] == 'S':
          cuadro[posicion[0]][posicion[1]] = com + str(count) + com
          cuadroAux[posicion[0]][posicion[1]] = com + str(count) + com
          Result = "El raton logró salir del laberinto "
          break
        cuadro[posicion[0]][posicion[1]] = com + str(count) + com
        cuadroAux[posicion[0]][posicion[1]] = com + str(count) + com
    elif decision == 5:
      print("partida interrumpida y finalizada")
      break
    else:
      print("solo es valida la entrada 1 , 2 ,3, 4 o 5")
  print(Result)

def juegoAutomatico (cuadro , cuadroAux):
  numChichones=0
  numAzucares=0
  numGuaros=0
  numVeneno=0
  count=0
  posicion=[0,0] # posicion.index(0) ->x   posicion.index(1) ->y
  Result=""
  com= ''
  while True:
    imprimirCuadro(cuadro, cuadroAux)
    print("Chichones: ",numChichones," Azucares: ",numAzucares," Guaros: ",numGuaros, " Venenos: ",numVeneno)
    print("Cuenta: ", count)
    print("Posicion: ", posicion)
    print("¿Que dirección quiere tomar? ")
    print("1. izquierda")
    print("2. derecha")
    print("3. abajo")
    print("4. arriba")
    decision = random.randint(1, 4)

    if decision==1:
      posicion[1] = posicion[1] - 1
      if fueraDeMatriz(posicion[0], posicion[1], cuadro):
        numChichones += 1
        posicion[1] = posicion[1] + 1
        if numChichones >= 10 :
          Result="el raton muere por daño cerebral"
          break
      else:
        count += 1
        if cuadro[posicion[0]][posicion[1]] == 'A':
          numAzucares += 1
          if numGuaros>0:
            numGuaros-=1
            numAzucares-=1
        elif cuadro[posicion[0]][posicion[1]] == 'G':
          numGuaros += 1
          if numAzucares > 0:
            numAzucares -= 1
            numGuaros -= 1
          elif numGuaros >= 3 and numVeneno > 0:
            numGuaros -= 3
            numVeneno -= 1
          elif numGuaros >= 5:
            Result = "el raton muere por cirrosis "
            break
        elif cuadro[posicion[0]][posicion[1]] == 'V':
          numVeneno += 1
          if numGuaros<3:
            Result = "el raton muere envenenado "
            break
        elif cuadro[posicion[0]][posicion[1]] == 'S':
          Result = "El raton logró salir del laberinto "
          break
        cuadro[posicion[0]][posicion[1]] = com + str(count) + com
        cuadroAux[posicion[0]][posicion[1]] = com + str(count) + com
    elif decision == 2:
      posicion[1] = posicion[1] + 1
      if fueraDeMatriz(posicion[0], posicion[1], cuadro):
        numChichones += 1
        posicion[1] = posicion[1] - 1
        if numChichones >= 10:
          Result = "el raton muere por daño cerebral"
          break
      else:
        count += 1
        if cuadro[posicion[0]][posicion[1]] == 'A':
          numAzucares += 1
          if numGuaros > 0:
            numGuaros -= 1
            numAzucares -= 1
        elif cuadro[posicion[0]][posicion[1]] == 'G':
          numGuaros += 1
          if numAzucares > 0:
            numAzucares -= 1
            numGuaros -= 1
          elif numGuaros >= 3 and numVeneno > 0:
            numGuaros -= 3
            numVeneno -= 1
          elif numGuaros >= 5:
            Result = "el raton muere por cirrosis "
            break
        elif cuadro[posicion[0]][posicion[1]] == 'V':
          numVeneno += 1
          if numGuaros < 3:
            Result = "el raton muere envenenado "
            break
        elif cuadro[posicion[0]][posicion[1]] == 'S':
          cuadro[posicion[0]][posicion[1]] = com + str(count) + com
          Result = "El raton logró salir del laberinto "
          break
        cuadro[posicion[0]][posicion[1]] = com + str(count) + com
        cuadroAux[posicion[0]][posicion[1]] = com + str(count) + com
    elif decision == 3:
      posicion[0] = posicion[0] + 1
      if fueraDeMatriz(posicion[0], posicion[1], cuadro):
        numChichones += 1
        posicion[0] = posicion[0] - 1
        if numChichones >= 10:
          Result = "el raton muere por daño cerebral"
          break
      else:
        count += 1
        if cuadro[posicion[0]][posicion[1]] == 'A':
          numAzucares += 1
          if numGuaros > 0:
            numGuaros -= 1
            numAzucares -= 1
        elif cuadro[posicion[0]][posicion[1]] == 'G':
          numGuaros += 1
          if numAzucares > 0:
            numAzucares -= 1
            numGuaros -= 1
          elif numGuaros >= 3 and numVeneno > 0:
            numGuaros -= 3
            numVeneno -= 1
          elif numGuaros >= 5:
            Result = "el raton muere por cirrosis "
            break
        elif cuadro[posicion[0]][posicion[1]] == 'V':
          numVeneno += 1
          if numGuaros < 3:
            Result = "el raton muere envenenado "
            break
        elif cuadro[posicion[0]][posicion[1]] == 'S':
          cuadro[posicion[0]][posicion[1]] = com + str(count) + com
          cuadroAux[posicion[0]][posicion[1]] = com + str(count) + com
          Result = "El raton logró salir del laberinto "
          break
        cuadro[posicion[0]][posicion[1]] = com + str(count) + com
        cuadroAux[posicion[0]][posicion[1]] = com + str(count) + com
    elif decision == 4:
      posicion[0] = posicion[0] - 1
      if fueraDeMatriz(posicion[0], posicion[1], cuadro):
        numChichones += 1
        posicion[0] = posicion[0] + 1
        if numChichones >= 10:
          Result = "el raton muere por daño cerebral"
          break
      else:
        count += 1
        if cuadro[posicion[0]][posicion[1]] == 'A':
          numAzucares += 1
          if numGuaros > 0:
            numGuaros -= 1
            numAzucares -= 1
        elif cuadro[posicion[0]][posicion[1]] == 'G':
          numGuaros += 1
          if numAzucares > 0:
            numAzucares -= 1
            numGuaros -= 1
          elif numGuaros >= 3 and numVeneno > 0:
            numGuaros -= 3
            numVeneno -= 1
          elif numGuaros >= 5:
            Result = "el raton muere por cirrosis "
            break
        elif cuadro[posicion[0]][posicion[1]] == 'V':
          numVeneno += 1
          if numGuaros < 3:
            Result = "el raton muere envenenado "
            break
        elif cuadro[posicion[0]][posicion[1]] == 'S':
          cuadro[posicion[0]][posicion[1]] = com + str(count) + com
          cuadroAux[posicion[0]][posicion[1]] = com + str(count) + com
          Result = "El raton logró salir del laberinto "
          break
        cuadro[posicion[0]][posicion[1]] = com + str(count) + com
        cuadroAux[posicion[0]][posicion[1]] = com + str(count) + com
    else:
      print("solo es valida la entrada 1 , 2 ,3 o 4")
  print(Result)


def partida():
  hayCuadro = False
  cuadrito = [(['0'] * 0) for i in range(0)]
  cuadritoAux = [(['0'] * 0) for i in range(0)]
  n = 0
  a = 0
  g = 0
  v = 0
  while True:
    print("menu:")
    print("1. configurar laberinto")
    print("2. ver configuración")
    print("3. jugar Manualmente")
    print("4. jugar Automaticamente")
    print("5. salir")
    dec=int(input("que desea hacer? : "))
    if dec == 1:
      n = int(input("cual es el ancho y alto del laberinto: "))
      a = int(input("que % de azucares desea: "))
      g = int(input("que % de guaros desea: "))
      v = int(input("que % de venenos desea: "))
      cuadrito = cuadro(n,a,g,v)
      cuadritoAux=cuadroAux(n)
      hayCuadro = True
    elif dec == 2:
      if hayCuadro == False:
        print("Debe configurar el laberinto primero")
      else:
        print("el laberinto es de tamaño ",n," por ",n)
        print("tiene un ", a," % de azucares")
        print("tiene un ", g, " % de guaros")
        print("tiene un ", a, " % de venenos")
    elif dec == 3:
      if hayCuadro == False:
        print("Debe configurar el laberinto primero")
      else:
        juego(cuadrito,cuadritoAux)
        hayCuadro=False
    elif dec == 4:
      if hayCuadro == False:
        print("Debe configurar el laberinto primero")
      else:
        juegoAutomatico(cuadrito,cuadritoAux)
        hayCuadro = False
    elif dec == 5:
      print("Gracias por jugar , hasta luego")
      break
    else:
      print("porfavor introduzca un numero del 1 al 5 ")





partida()

