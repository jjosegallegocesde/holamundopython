#Esto es un comentario de linea

'''
Comentario de bloque

'''

#SALIDA CONSOLA
#print("HOLA MUNDO PYTHON OME")

#VARIABLES O ENTRADAS
#nombreUsuario:str='Juan'
#edad:int=32
#estatura:float=1.62
#eshinchaVerde:bool=True

#salida
#print(nombreUsuario)
#print('Buenos dias',nombreUsuario)
#print(f'Buenos dias {nombreUsuario}')

#RECIBIENDO VARIABLES DESDE LA CONSOLA
#numero1=int(input("Digita un número entero: "))
#print(f'usted digito el numero {numero1}')

#numero2=int(input("Digita un segundo número entero: "))
#print(f'usted digito el numero {numero2}')

#suma=numero1+numero2
#print(f'la suma de {numero1} + {numero2} = {suma}')

#numero:int="juan"
#print(numero)


#TOMANDO DECISIONES
#numero = int (input("Ingrese un numero : "))
#print(f'El numero digitado fue {numero}')

#if(numero>=0):
    #print("el numero es positivo")
#else:
    #print("el numero es negativo")
    
    #print("oe.. fuck you men")

#Ejemplo 2
'''
nivelAgua=int(input("digite el nivel de agua: "))

if(nivelAgua<200):
    print("hay muy poca agua en la represa")
elif(nivelAgua>=200 and nivelAgua<450):
    print("el nivel de agua el el adecuado")
else:
    print("hay mucha agua, ojo...")
'''
'''
mes = input("digite el mes: ")

if( mes == "enero" or mes =="febrero" or mes =="marzo"):
    print(f"estamos en invierno")
elif( mes == "abril" or mes =="mayo" or mes=="junio"):
    print(f"estamos en verano")
elif( mes == "julio" or mes == "agosto" or mes == "septiembre"):
    print(f"estamos en otoño")
else:
    print(f"estamos en primavera")
'''

#bucles/ciclos/loops/repeticion

contador=0

while(contador<10):
    contador+=1
    print(contador)
else:
    print("termino el ciclo")
    