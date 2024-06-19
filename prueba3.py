import csv
lista=[]

def cambio_equipo():
    op=input("Seguro desea cambiar el nombre?").lower()
    if op=="si":
        return 1
    if op=="no":
        return 0
    else:
        print("ingrese una opción válida")

try:    
    while True:
        print("1.-Agregar equipo")
        print("2.-Listar equipo")
        print("3.-Actualizar el nombre por id")
        print("4.-Generar BBDD")
        print("5.-Cargar BBDD")
        print("6.-Estadísticas")
        print("0.-Salir")
        op=int(input("Ingrese una opción\n"))

        if op==1:
            print("")
            id=int(input("Ingrese el id del equipo"))
            nombre=input("Ingrese el nombre del equipo")
            puntos=int(input("Ingrese los puntos del equipo"))
            if puntos>=0 and puntos<=40:
                    categoria="amateur"
            elif puntos>40 and puntos<=80:
                    categoria="principiante"
            elif puntos>80 and puntos<=120:
                    categoria="avanzado"
            elif puntos>120:
                    categoria="idolo"
            
            listita=[id,nombre,puntos,categoria]
            lista.append(listita)

        elif op==2:
            print("")
            print("===========================================")
            for x in lista:
                print("id : ", x[0],"nombre: ", x[1], "puntos: ", x[2],"categoria: ", x[3])
            print("===========================================")

        elif op==3:
            encontrado=False
            print("")
            id=input("Ingrese el id del equipo que quiere modificar")
            op3=cambio_equipo()
            if op3==1:
                for x in lista:
                    if id==x[0]:
                        print("Datos del equipo a modificar")
                        print("id : ", x[0],"nombre: ", x[1], "puntos: ", x[2],"categoria: ", x[3])
                        nuevo_nombre=input("Ingrese el nuevo nombre :")
                        x[1]=nuevo_nombre
                        encontrado=True
                        break
                if encontrado==False:
                    print("El equipo no está registrado")
            if op3==0:
                print("Nombre no cambiado")
                

        elif op==4:
            print("")
            print("------- GENERANDO BASE DE DATOS -------")
            print("")
            with open('bbdd_equipos.csv','w',newline='') as bbdd_equipos:
                escritor_csv = csv.writer(bbdd_equipos)
                escritor_csv.writerow(['ID','NOMBRE','PUNTOS','CATEGORIA'])
                escritor_csv.writerows(lista)
                print("Archivo generado")

        elif op==5:
            print("")
            print("------- CARGANDO BASE DE DATOS -------")
            print("")
            with open('bbdd_equipos.csv','r',newline='') as bbdd_equipos:
                lector_csv=csv.reader(bbdd_equipos)
                for x in lector_csv:
                    lista.append(x)
                print("Archivo cargado con éxito")

        elif op==6:
            acum=0
            cont=0
            puntitos=0
            print("")
            print("------- ESTADÍSTICAS -------")
            print("")
            for x in lista:
                cont=cont+1
                acum=int(acum+x[2])
            prom = acum/cont
            print("El promedio de puntos es de: ", prom)
            for x in lista:
                p=x[2]
                if puntitos<p:
                    puntitos=x[2]
            print("El puntaje más alto es de :",puntitos)
                

        elif op==0:
            print("gracias por todo")
            break
except:
    print("ERROR REDIRIGIENDO AL MENU")
