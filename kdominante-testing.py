import unittest

# Se importa el codigo a testear.
from kdominante import cantidad_de_0, cantidad_de_1, es_kdominante, cero_dominantes_entre, suma_cero_dominantes_menores

#####################################################################

class TestKDominante(unittest.TestCase):
    def test_cantidad_de_0(self):
        self.assertEqual(cantidad_de_0('1111'), 0) #Caso solo de 1.
        self.assertEqual(cantidad_de_0('0000'), 4) #Caso solo de 0.
        self.assertEqual(cantidad_de_0('101010'), 3) #Caso mezclando 0 y 1.
        self.assertEqual(cantidad_de_0("LaRevolucionFrancesa"), 0) #Caso solo str.
        self.assertEqual(cantidad_de_0("2023HolaAgustin2023"), 2) #Caso str(int) + str + str(int).
        self.assertEqual(cantidad_de_0(""), 0) #Caso str vacio.
        self.assertNotEqual(cantidad_de_0('1111'), 2) #Caso solo de 1 Falso, donde cantcero = 0.
        self.assertNotEqual(cantidad_de_0('000000'), 3) #Caso solo de 0 Falso, donde cantcero = 6.
        self.assertNotEqual(cantidad_de_0('1010101'), 8) #Caso mezclando 0 y 1 Falso, donde cantcero = 4.
        self.assertNotEqual(cantidad_de_0(""), 1) #Caso str vacio.
      
    def test_cantidad_de_1(self):
        self.assertEqual(cantidad_de_1('1111'), 4) #Caso solo de 1.
        self.assertEqual(cantidad_de_1('0000'), 0) #Caso solo de 0.
        self.assertEqual(cantidad_de_1('101010'), 3) #Caso mezclando 0 y 1.
        self.assertEqual(cantidad_de_1("LaRevolucionFrancesa"), 0) #Caso solo str.
        self.assertEqual(cantidad_de_1("2023HolaAgustin2023"), 0) #Caso str(int) + str + str(int).
        self.assertEqual(cantidad_de_1(""), 0) #Caso str vacio.
        self.assertNotEqual(cantidad_de_1('1111'), 100) #Caso solo de 1 Falso, donde cantuno = 4.
        self.assertNotEqual(cantidad_de_1('000000'), 7) #Caso solo de 0 Falso, donde cantuno = 0.
        self.assertNotEqual(cantidad_de_1('1010101'), 5) #Caso mezclando 0 y 1 Falso, donde cantuno = 4.
        self.assertNotEqual(cantidad_de_1(""), 1) #Caso str vacio.

  
    def test_es_kdominante(self):
        self.assertTrue(es_kdominante(1, 7)) #Caso True donde 7bin = 111, 2(uno) > 1(cero).
        self.assertTrue(es_kdominante(0, 0)) #Caso True donde 0bin = 0, 0(uno) < 1(cero).
        self.assertTrue(es_kdominante(1, 1000)) #Caso True donde 1000bin = 1111101000, 6(uno) > 4(cero).
        self.assertFalse(es_kdominante(0, 7)) #Caso False por contrario a caso uno.
        self.assertFalse(es_kdominante(1, 0)) #Caso False por contrario a caso dos. 
        self.assertFalse(es_kdominante(0, 1000)) #Caso False por contrario al caso tres.

  
    def test_cero_dominantes_entre(self):
        self.assertEqual(cero_dominantes_entre(1, 1), []) #Caso sin argumentos para testear, 1bin = 1 por lo que no tiene dominantes entre 1 y 1.Retorna vacia.
        self.assertEqual(cero_dominantes_entre(1, 17), [4, 8, 16, 17]) #Caso donde 4bin = 100, 8bin = 101, 16bin = 10000, 17bin = 10001. Todos cumplen que ceros > unos.
        self.assertEqual(cero_dominantes_entre(10, 32), [16, 17, 18, 20, 24, 32]) #Caso donde 16bin = 10000 , 17bin = 10001 , 18bin = 10010 , 20bin = 10100, 24bin = 11000 , 32bin = 100000.  Todos cumplen que ceros                                                                                                               >unos).
        self.assertNotEqual(cero_dominantes_entre(0, 0), []) #Caso donde recibimos una lista vacia al no tener cero dominantes desde 0 hasta 0 incluido. Comprobando asi que deben ser menor o igual al valor n pero que al ser "NotEqual" , 0bin = 0. Por lo que seria 0 dominante, no encontrado en la lista. 
        self.assertNotEqual(cero_dominantes_entre(1, 1), [12]) #Caso donde consideramos los 0 dominantes entre 1 y 1 incluido. Comprobando que deben ser menor o igual al valor n pero q al ser "NotEqual", 1bin = 1. Por lo que seria 1 dominante, no 0. Independientemente lo que pongamos en la lista, siempre devolvera sin errores.

  
    def test_suma_cero_dominantes_menores(self):
        self.assertEqual(suma_cero_dominantes_menores(8), 4) #Caso donde consideramos los estrictamente menores a 8, estos incluyen nada mas el 4. Debido a que el siguiente cero dominante seria igual a 8, pero al ser estrictamente menor no es incluido. 
        self.assertEqual(suma_cero_dominantes_menores(10), 12) #Caso donde consideramos los menores a 10, estos incluyen el 4bin = 100 y el 8bin = 1000. Por lo que seria 8+4 = 12.
        self.assertEqual(suma_cero_dominantes_menores(20), 63) #Caso donde encontramos los valores menores a 20 que incluyen: 4 + 8 + 16 + 17 + 18 = 63.
        self.assertEqual(suma_cero_dominantes_menores(3), 0) #Caso donde retorna 0, donde 0 es el unico cero dominante menor a 3. 
        self.assertNotEqual(suma_cero_dominantes_menores(8), 3) #Caso donde encontramos la suma de los 0 dominantes menores a 5, los cuales son: 4. Al usar un assertNotEqual, mostramos que la respuesta no es 3, sino seria 4.
        self.assertNotEqual(suma_cero_dominantes_menores(10), 0)#Caso donde tenemos los mismos valores a la linea 46 comprobando que su return es correcto. 
        self.assertNotEqual(suma_cero_dominantes_menores(20), 64) #Caso donde encontramos los mismos valores a la linea 47, demostrando que su return es correcto. 
        self.assertNotEqual(suma_cero_dominantes_menores(3), 1) #Caso donde tenemos los mismos valores a la linea 4 comprobando que su return es correcto.
      

unittest.main()