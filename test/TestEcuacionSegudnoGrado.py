import unittest
from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado


class TestEcuacionSegundoGrado(unittest.TestCase):
    def setUp(self):
        self.calculoRaices = EcuacionSegundoGrado()

    def tearDown(self):
        self.calculoRaices = None

    def test_calculoESG_dosNumeros_retornaSolucion(self):
        # arrange
        a = 3
        b = -5
        c = 1
        resultadoEsperadoRaiz1 = 1.43
        resultadoEsperadoRaiz2 = 0.23

        # do
        resultadoActualRaiz1, resultadoActualRaiz2 = self.calculoRaices.calculoESG(a, b, c)

        # assert
        self.assertAlmostEqual(resultadoEsperadoRaiz1, resultadoEsperadoRaiz1, 2)
        self.assertAlmostEqual(resultadoEsperadoRaiz2, resultadoEsperadoRaiz2, 2)

    def test_calculoESG_dosNumeros_retornaSolucion(self):
        # arrange

        items = (
            {"Case": "Caso 01", "a": 3, "b": -5, "c": 1, "RaizEsperada1": 1.43, "RaizEsperada2": 0.23},
            {"Case": "Caso 02", "a": 1, "b": 2, "c": 1, "RaizEsperada1": -1.00, "RaizEsperada2": -1.00},
            {"Case": "Caso 03", "a": -1, "b": 2, "c": -1, "RaizEsperada1": 1.0, "RaizEsperada2": 1.00},
            {"Case": "Caso 04", "a": 1, "b": 0, "c": -18, "RaizEsperada1": 4.2, "RaizEsperada2": -4.24},
            {"Case": "Caso 05", "a": 1, "b": 4, "c": 0, "RaizEsperada1": 0.0, "RaizEsperada2": -4.00},
            {"Case": "Caso 06", "a": 1, "b": 4, "c": 4, "RaizEsperada1": -2.0, "RaizEsperada2": -2.00},
            {"Case": "Caso 07", "a": 1, "b": 3, "c": 2, "RaizEsperada1": -1.0, "RaizEsperada2": -2.00},
        )
        # do
        for item in items:
            with self.subTest(item["Case"]):
                resultadoActualRaiz1, resultadoActualRaiz2 = self.calculoRaices.calculoESG(item["a"], item["b"],
                                                                                           item["c"])
                resultadoEsperadoRaiz1 = item["RaizEsperado1"]
                resultadoEsperadoRaiz2 = item["RaizEsperado2"]

        # assert
        self.assertAlmostEqual(resultadoEsperadoRaiz1, resultadoActualRaiz1, 2)
        self.assertAlmostEqual(resultadoEsperadoRaiz2, resultadoActualRaiz2, 2)


if __name__ == "__main__":
    unittest.main()
