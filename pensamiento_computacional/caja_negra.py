import unittest

def suma(num_1, num_2):
    return num_1 + num_2

class CajaNegraTest(unittest.TestCase):
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        respuesta = suma(num_1, num_2)

        self.assertEqual(respuesta,15)

    def test_suma_dos_negativos(self):
            num_1 = -10
            num_2 = -7

            respuesta = suma(num_1, num_2)

            self.assertEqual(respuesta,-17)

    def test_suma_pos_neg(self):
            num_1 = -14
            num_2 = 7

            respuesta = suma(num_1, num_2)

            self.assertEqual(respuesta,-7)        

if __name__ == '__main__':
    unittest.main()