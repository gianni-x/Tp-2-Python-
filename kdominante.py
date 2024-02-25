from typing import List

def cantidad_de_0(s:str) -> int:
    '''
    Requiere: Un string
    Devuelve: Ocurrencias de 0 en el string.
    '''
    i:int = 0
    cantcero:int = 0
    while i < len(s):
        if s[i] == '0':
            cantcero = cantcero + 1
        i = i + 1 
    return cantcero

    
def cantidad_de_1(s:str) -> int:
    '''
    Requiere: Un string
    Devuelve: Ocurrencias de 1 en el string.
    '''
    cantuno:int = 0
    i:int = 0
    while i < len(s):
        if s[i] == '1':
            cantuno = cantuno + 1
        i = i + 1
        
    return cantuno

def es_kdominante(k:int , n:int) -> bool:
    '''
    Requiere: k ∈ {0, 1}, n ∈ N
    Devuelve: True si el número es k-dominante, False en caso contrario.
    '''
    binario = bin(n)[2:]
    ceros = cantidad_de_0(str(binario))
    unos = cantidad_de_1(str(binario))
  
    if k == 1 and unos > ceros:
            return True
    if k == 0 and ceros > unos:
            return True
    else:
        return False

def cero_dominantes_entre(n:int, m:int) -> List[int]:
    '''
    Requiere: n ≤ m, n y m ∈ N.
    Devuelve: Lista de números 0-dominantes entre n y m, inclusive en ambos
    casos (es decir, mayores o iguales a n, y menores o iguales a m), ordenada de menor a mayor por el .append().
    '''
    i:int = n
    vr:List[int] = []
    while i <= m:
        if es_kdominante(0, i) == True:
            vr.append(i)
        i = i + 1
    return vr

def suma_cero_dominantes_menores(n:int) -> int:
    '''
    Requiere: n ∈ N
    Devuelve: La suma de todos los números 0-dominantes estrictamente menores que n.
    '''
    i:int = 0
    vr:int = 0
    while i < n:
        if es_kdominante(0, i) == True: 
            vr = vr + i
        i = i + 1
    return vr