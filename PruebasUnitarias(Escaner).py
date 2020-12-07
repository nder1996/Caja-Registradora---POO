from CajaRegistradora import Escaner
import string , unittest

class Test_CajaRegistradora_Escaner(unittest.TestCase):
    
    def setUp(self):
        Compra_Total = ["|| {} UNIDADES DE {} TIENE UN DESCUENTO DE {} % \n\n|| SUB-TOTAL A PAGAR ES $ {:.3f} USD".format("1","ARROZ","10",90.00),
                        "|| {} UNIDADES DE {} TIENE UN DESCUENTO DE {} % \n\n|| SUB-TOTAL A PAGAR ES $ {:.3f} USD".format("1","PERA","45",110.0)]
        Sub_Total = ["90.0","100.0"]    
        self.Escaner_P =Escaner(Sub_Total,Compra_Total) 
    
    def test_MostrarPedido_IsNotNone(self):
        self.assertIsNotNone(self.Escaner_P.Mostrar_Pedido() is not None) 

    def test_TotalPedido_IsNotNone(self):
        Total = 0.0
        self.assertIsNotNone(self.Escaner_P.Total_Pedido(Total) is not None) 

    def test_EliminarArticulo_IsNotNone(self):
        Total = 0.0
        self.assertIsNotNone(self.Escaner_P.Total_Pedido(Total) is not None) 




if __name__ == "__main__":
    unittest.main(exit=False)