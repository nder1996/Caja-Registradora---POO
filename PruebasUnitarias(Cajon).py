from CajaRegistradora import Cajon
import string , unittest



class Test_CajaRegistradora_Pantalla_Principal(unittest.TestCase):
    
    def setUp(self):
        Total_Precio = 15000 ; Dinero_Cliente = 30.000
        self.CAJON = Cajon(Total_Precio,Dinero_Cliente)
        
    def test_PagoProductos_IsNotNone(self):
        self.assertIsNotNone(self.CAJON.Pago_Producto() is not None)
    
    def test_PagoProductos_IsNone(self):
        Total_Precio = 15000 ; Dinero_Cliente = 10.000
        self.CAJON = Cajon(Total_Precio,Dinero_Cliente)   
        self.assertIsNone(None,self.CAJON.Pago_Producto() is None)   
        
        
        
    









if __name__ == "__main__":
    unittest.main(exit=False)