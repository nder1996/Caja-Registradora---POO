from CajaRegistradora import Producto
import string , unittest


class Test_CajaRegistradora_Producto(unittest.TestCase):

    def test_Validar_Cantidad_True(self):
        Producto_Cliente = Producto(0,"500",[],[],[])
        Validar  = Producto_Cliente.Validar_P()
        self.assertTrue(True,bool(Validar) is True) 
    
    def test_Validar_Cantidad_False(self):
        Producto_Cliente = Producto(0,"500.7",[],[],[])
        Validar  = Producto_Cliente.Validar_P()
        self.assertFalse(False,bool(Validar) is False) 

    def test_Validar_Valor_True(self):
        Producto_Cliente = Producto(1,"500.35",[],[],[])
        Validar  = Producto_Cliente.Validar_P()
        self.assertTrue(True,bool(Validar) is True) 

    def test_Validar_Valor_False(self):
        Producto_Cliente = Producto(1,"500.7AS",[],[],[])
        Validar  = Producto_Cliente.Validar_P()
        self.assertFalse(False,bool(Validar) is False) 

    def test_Validar_Descuento_True(self):
        Producto_Cliente = Producto(2,"50.35",[],[],[])
        Validar  = Producto_Cliente.Validar_P()
        self.assertTrue(True,bool(Validar) is True) 


    def test_Validar_Valor_False(self):
        Producto_Cliente = Producto(2,"50.7ASp",[],[],[])
        Validar  = Producto_Cliente.Validar_P()
        self.assertFalse(False,bool(Validar) is False) 






if __name__ == "__main__":
    unittest.main()