import string , time , sys , os

class Producto:
    def __init__(self,Item,Atributo,Sub_Total,Articulo,Compra_Total):
        self.Item         = Item
        self.Atributo     = Atributo
        self.Sub_Total    = Sub_Total
        self.Articulo     = Articulo
        self.Compra_Total = Compra_Total
        
        
    def Validar_P(self):
        if self.Item!=0:
            Punto = int(self.Atributo.find("."))
            if len(self.Atributo)>Punto+1 or Punto==-1:
                if self.Atributo.count(".")<=1:                   
                    Aux = self.Atributo.replace(".","")
                    if Aux.isdigit()==True:
                        if self.Item==2:
                            if float(self.Atributo)<=100:
                                return True
                                sys.exit(0)
                        else:
                            return True
                            sys.exit(0)
        else: 
            if self.Atributo.isdigit()==True:
                return True
                sys.exit(0)

    def Crear_Producto(self):
        Pedido = "\n\n||{} UNIDADES DE {} TIENE UN DESCUENTO DE {} % \n\n|| SUB-TOTAL A PAGAR ES $ {} USD".format(self.Articulo[1],self.Articulo[2],self.Articulo[4],self.Sub_Total)
        self.Compra_Total.append(Pedido)
        self.Articulo.clear()
        
class Escaner(Producto):
    def __init__(self,Item,Atributo,Sub_Total,Articulo,Compra_Total,Total):
        super().__init__(Item,Atributo,Sub_Total,Articulo,Compra_Total)
        self.Total  = Total
        
    def Mostrar_Pedido(self):
        for i in self.Compra_Total:
            print(i)
        
    def Total_Pedido(self):
        self.Total =  float(self.Total) + float(self.Sub_Total)

    def Validar_Item_ELiminado(self):
        if self.Item!="0":
            if self.Item.isdigit()==True:
                if int(self.Item) <= len(self.Compra):
                    return True
                    sys.exit(0)

Lista1 = ["Arroz","Papa","Pera","Azucar","Malteada"]


List_1 = [] ; Item = 0 ; Atributo = "400" ; Sub_Total = "500" ; Total = 0.0

List_3 = []

Producto_Cliente = Producto(Item,Atributo,Sub_Total,Lista1,List_1)
Validar = Producto_Cliente.Validar_P()
if Validar == True:
    Producto_Cliente.Crear_Producto() 
    Escaner_Producto = Escaner(Item,Atributo,Sub_Total,Lista1,List_1,Total)
    Escaner_Producto.Mostrar_Pedido()
    print("ESTE ES EL TOTAL : ",Total)

