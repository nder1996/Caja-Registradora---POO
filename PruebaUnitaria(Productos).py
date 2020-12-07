from CajaRegistradora import Producto
import string , unittest


class Test_CajaRegistradora_Producto(unittest.TestCase):

    def test_Validar_Cantidad_True(self):
        Producto_Cliente = Producto(0,"500",[],[],[])
        self.assertTrue(True,bool(Producto_Cliente.Validar_P()) is True) 
    
    def test_Validar_Cantidad_False(self):
        Producto_Cliente = Producto(0,"500.7",[],[],[])
        self.assertFalse(False,bool(Producto_Cliente.Validar_P()) is False) 

    def test_Validar_Valor_True(self):
        Producto_Cliente = Producto(1,"500.35",[],[],[])
        self.assertTrue(True,bool(Producto_Cliente.Validar_P()) is True) 

    def test_Validar_Valor_False(self):
        Producto_Cliente = Producto(1,"500.7AS",[],[],[])
        self.assertFalse(False,bool(Producto_Cliente.Validar_P()) is False) 

    def test_Validar_Descuento_True(self):
        Producto_Cliente = Producto(2,"50.35",[],[],[])
        self.assertTrue(True,bool(Producto_Cliente.Validar_P()) is True) 

    def test_Validar_Descuento_False(self):
        Producto_Cliente = Producto(2,"50.7ASp",[],[],[])
        self.assertFalse(False,bool(Producto_Cliente.Validar_P()) is False) 
    
    def test_CrearProducto_ARROZ_None(self):
        Articulos = ["A65SD6SD","1","ARROZ","100","10"] ; Sub_Total = [] ; Compra_Total = [] ; Sub_Total.append("500")
        Producto_Cliente = Producto(-1,"100",Sub_Total,Articulos,Compra_Total)
        self.assertIsNone(None,Producto_Cliente.Validar_P() is  None) 
    
    def test_CrearProducto_PERA_None(self):
        Articulos = ["123PERASDFDF","1","PERA","20","45"] ; Sub_Total = [] ; Compra_Total = [] ; Sub_Total.append("700")
        Producto_Cliente = Producto(-1,"110",Sub_Total,Articulos,Compra_Total)
        self.assertIsNone(None,Producto_Cliente.Validar_P() is  None)     
    
    def test_CrearProducto_ARROZ_NotNone(self):
        Articulos = ["A65SD6SD","1","ARROZ","100","10"] ; Sub_Total = [] ; Compra_Total = []
        Producto_Cliente = Producto(-1,"90",Sub_Total,Articulos,Compra_Total)
        self.assertIsNotNone(Producto_Cliente.Validar_P() is not None) 
    
    def test_CrearProducto_PERA_NotNone(self):
        Articulos = ["A65SD6SD","1","PERA","200","45"] ; Sub_Total = [] ; Compra_Total = []
        Producto_Cliente = Producto(-1,"110",Sub_Total,Articulos,Compra_Total)
        self.assertIsNotNone(Producto_Cliente.Validar_P() is not None)    
        

if __name__ == "__main__":
    unittest.main(exit=False)
    
    
    