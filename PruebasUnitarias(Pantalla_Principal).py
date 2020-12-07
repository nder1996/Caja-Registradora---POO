from CajaRegistradora import Pantalla_Principal
import string , unittest


class Test_CajaRegistradora_Pantalla_Principal(unittest.TestCase):

    def setUp(self):
        self.Menu = Pantalla_Principal()

    def test_MostrarTotal_IsNotNone(self):
        self.assertIsNotNone(self.Menu.Total(153.045) is not None)

    def test_MostrarTotal_IsNone(self):
        self.assertIsNone(None,self.Menu.Total(0.0) is not None)


if __name__ == "__main__":
    unittest.main(exit=False)