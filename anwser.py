#Variables

acuPeso = 0

cant = abs(float(input("¿Cuantos paquetes desea ingresar?\n")))
dist = float(input("¿A que distancia?\n"))
naci = abs(int(input("¿Es nacional o intercontinental? \n0 -> nacional\n1 -> intercontinental\n")))

precio = 0
for i in range(1, int(cant)+1):
    peso = float(input("¿Cuanto pesa el paquete numero "+str(i)+"?\n"))
    
    if (acuPeso + peso) > (250000*0.95):
        print("Se ha superado el peso maximo de carga recomendado, se dejará de recibir paquetes. \n")
        i = cant+1
    else:
        if (peso < 10):
            print("El peso del paquete no es aceptable. \n")
        else:
            acuPeso = acuPeso + peso;
            precio = 4500*peso
				
            if (naci == 0): #nacional
                precio = 4000*dist
            else: #intercontinental
                precio = 8000*(dist* 0.62137) #convertir a millas
				
			#descuentos
            if (peso > 100) and (naci == 0):
                precio = precio - precio*0.15
			
            if (dist > 8000) and (naci == 1) and (peso > 400):
                precio = precio - precio*0.1
print("El precio a pagar es de: ",precio, "$")

    