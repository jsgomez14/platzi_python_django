import unittest

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

class CajaCristalTest(unittest.TestCase):
    def test_es_mayor_de_edad(self):
        edad = 20
        respuesta = es_mayor_de_edad(edad)
        self.assertEqual(respuesta, True)
        
    def test_es_menor_de_edad(self):
        edad = 15
        respuesta = es_mayor_de_edad(edad)
        self.assertEqual(respuesta,False)

if __name__ == '__main__':
    unittest.main()