from kdominante import cantidad_de_0, cantidad_de_1, es_kdominante, cero_dominantes_entre, suma_cero_dominantes_menores
from typing import List

def elegir_funcion() -> str:
    '''
    Despliega el menú de funciones disponibles en la pantalla y devuelve
    la opción elegida por el usuario.
    Requiere: Nada.
    Devuelve: La opción elegida por el usuario, en mayúscula y sin espacios 
    adelante y atrás según la siguiente codificación:
        A -> Contar las ocurrencias de '0' en un string;
        B -> Contar las ocurrencias de '1' en un string;
        C -> Determinar si un número es k-dominante;
        D -> Devolver 0-dominantes entre dos números;
        E -> Devolver la suma de los 0-dominantes menores que un número;
        X -> Finalizar;
    '''
    print()
    print('Funciones disponibles')
    print('---------------------')
    print('A. Cantidad de 0 [s]')
    print('B. Cantidad de 1 [s]')
    print('C. Es k-dominante? [k, n]')
    print('D. 0-dominantes entre [n,m]')
    print('E. Suma de 0-dominantes menores que [n]')
    print('X. Finalizar')
    
    # input permite al usuario ingresar su opción, strip le saca caracteres 
    # de fin de línea, upper la pasa a mayúsculas.
    opción_elegida:str = input('Seleccione una opción: ').upper().strip()
    return opción_elegida


# Cuerpo principal del programa
finalizar:bool = False
while not finalizar:
    opcion_seleccionada:str = elegir_funcion()

    # Se analiza la opción elegida
    if opcion_seleccionada == 'A':
        s:str = input('Ingrese s: ')
        cant_cero:int = cantidad_de_0(s)
        if cant_cero > 1:
            print("'0' aparece " + str(cant_cero) + " veces en " + s)
        else: 
            print("'0' aparece " + str(cant_cero) + " vez en " + s)
        
        
    elif opcion_seleccionada == 'B':
        s:str = input('Ingrese s: ')
        cant_unos: int = cantidad_de_1(s)
        if cant_unos > 1:
            print("'1' aparece " + str(cant_unos) + " veces en " + s)
        else: 
            print("'1' aparece " + str(cant_unos) + " vez en " + s)
        
    elif opcion_seleccionada == 'C':
        k:int = int(input('Ingrese k: '))
        n:int = int(input('Ingrese n: '))
        kDom:bool = es_kdominante(k, n)
        if kDom:
            print("El número " + str(n) + " es " + str(k) + "-dominante")
        else:
            print("El número " + str(n) + " no es " + str(k) + "-dominante")
       
    elif opcion_seleccionada == 'D':
        n:int = int(input('Ingrese n: '))
        m:int = int(input('Ingrese m: '))
        domEntre:List[int] = cero_dominantes_entre(n, m)
        print("0-dominantes entre " + str(n) + " y " + str(m) + ": " + str(domEntre))
        
        
    elif opcion_seleccionada == 'E':
        n:int = int(input('Ingrese n: '))
        sumaCero:int = suma_cero_dominantes_menores(n)
        print("Suma de 0-dominantes menores que " + str(n) + ": " + str(sumaCero))
    
    
    elif opcion_seleccionada == 'X':
        finalizar = True
    else:
        print('Opción inválida.')

    if opcion_seleccionada != 'X':
        input('Presione ENTER para continuar.')
