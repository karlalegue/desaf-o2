N = int (input ("Ingrese la cantidad máxima de contenedores por pila: "))
M = int (input("Ingrese la cantidad  máxima de pilas: "))
puerto = []
contenedor_no_encontrado = True

for i in range (N):
    puerto.append ([])
    for j in range (M):
        puerto[i].append (None)

for i in range (N):
    for j in range (M):
        print ("|",puerto [i] [j],"|", end = " ")
    print (" ")
print (" ")

print ("    -----MENÚ-----   \n   OPCIONES DE MENÚ     \n1.Para buscar su contenedor, ingrese 1.\n2.Para incluir un contenedor, ingrese 2.\n3.Para retirar un contenedor, ingrese 3.\n4. Para cerrar jornada laboral, ingrese 4." )
opcion = int (input ("Ingrese la opción que desea: "))
while opcion != 4: 
    if opcion == 2: 
        print ("2. Para inlcuir un contenedor")
        contenedor = (input("Ingrese Numero/NombreEmpresa del contenedor a incluir: "))
        puerto[N-1][M-1]=contenedor
        for i in range (N):
            for j in range (M):
                print ("|",puerto [i] [j],"|", end = " ")
            print ()
        opcion = int (input ("Ingrese la opción que desea: "))   
    if opcion == 1: 
        print ("1. Para bucar su contenedor")
        contenedor = (input("Ingrese Numero/NombreEmpresa del contenedor a buscar: "))
        posicion = contenedor

        for i in range (N):
            for j in range (M):
                if (puerto [i] [j] == posicion): 
                    print ("El contenedor se encuentra en la pila", j, "y en la posición de contenedores", i, "del puerto")
                contenedor_no_encontrado = False  
        if contenedor_no_encontrado ==True:
            print ("El contenedor no se ha encontrado en el puerto")
        opcion = int (input ("Ingrese la opción que desea: "))
    if opcion == 3: 
        print ("3. Para retirar un contenedor")
        contenedor =(input("Ingrese Numero/NombreEmpresa del contenedor a retirar "))
        if contenedor != puerto [0] [0]:
            print ("El contenedor no puede ser removido")
        elif puerto [i] [j]== contenedor:
            puerto[i] [j] = None
        
        for i in range (N):
            for j in range (M):
                print ("|",puerto [i] [j],"|", end = " ")
            print (" ")
        print (" ")
        opcion = int (input ("Ingrese la opción que desea: "))
print ("Ha cerrado su jonada laboral")

        



