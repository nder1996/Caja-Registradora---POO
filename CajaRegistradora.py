import string , time , sys , os

class Producto:
    def __init__(self,Item,Atributo,Sub_Total,Articulo,Compra_Total):
        self.Item         = Item
        self.Atributo     = Atributo
        self.Sub_Total    = Sub_Total
        self.Articulo     = Articulo
        self.Compra_Total = Compra_Total
        
        
    def Validar_P(self):
        if self.Item!=0 and self.Atributo!="":
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
        if self.Item == 0 and self.Atributo!="": 
            if self.Atributo.isdigit()==True:
                return True
                sys.exit(0)

    def Crear_Producto(self):
        Pedido = "\n\n|| {} UNIDADES DE {} TIENE UN DESCUENTO DE {} % \n\n|| SUB-TOTAL A PAGAR ES $ {} USD".format(self.Articulo[1],self.Articulo[2],self.Articulo[4],self.Sub_Total[len(self.Sub_Total)-1])
        self.Compra_Total.append(Pedido)
        self.Articulo.clear()

class Escaner:
    def __init__(self,Total,Sub_Total,Compra_Total):
        self.Total              = Total
        self.Sub_Total          = Sub_Total
        self.Compra_Total       = Compra_Total
        
    def Mostrar_Pedido(self):
        Contador = 0
        for i in self.Compra_Total:
            Contador+=1
            print("\n\n\t\t\t   °°°°°°°°°°°°°°°°°°°°°°°°")
            print("\t\t\t        ARTICULO : ",Contador)
            print("\t\t\t   °°°°°°°°°°°°°°°°°°°°°°°°")
            print(i)
            
    def Total_Pedido(self):
        for i in range(len(self.Sub_Total)):
            self.Total = self.Total + float(self.Sub_Total[i])
        return self.Total
 
    def Validar_Item_ELiminado(self,Eliminar):
        if Eliminar!="0":
            if Eliminar.isdigit()==True:
                if int(Eliminar) <= len(self.Compra_Total):
                    Eliminar  = int(Eliminar) - 1
                    self.Compra_Total.pop(int(Eliminar))
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

class Pantalla_Principal:
    def __init__(self,Encedido):
        self.Encendido    = Encedido

    def Inicio(self):
        print("\n")
        print("\t\t\t|***|  CAJA REGISTRADORA  |***|")
        print("\t\t\t|***|         V2.0        |***|")
        print("\n\n")
        
    def Error_Validar(self):
        print("\n\n\t\t\t| ERROR   DATOS   INCORRECTO |\n")

    def Instruccion_P(self):
        print("\n\n\t\t\t   INGRESAR DATOS DE LA COMPRA\n")
        print("\t\t\t\t      *|* \n")         
    
    def Error_P(self):
        print("\n\n\n\t\t     | POR FAVOR INGRESE UN PRODUCTO VALIDO |")
        print("\n\t\t\t\t      *|* \n")  

    def Articulo_F(self):
        print("\n\n\t\t       |P E D I D O  F I N A L I Z A D O| ")
        print("\n\t\t\t\t      *|* \n")
    
    def Agregado_P(self):
        print("\n\t\t\t    |PRODUCTOS AGREGADOS|")
        print("\n\n")
        
    def Total(self,Total):
        print("\n\n\t\t\t    | TOTAL : $ {} USD |\n".format(float(Total)))
        print("\n\n")


Articulos= [] ;Total_Compra = [] ; Item = [] ; Atributo = "" ; Sub_Total = [] ; Total_Precio = 0.0 ; Eliminar = "-1" ; Stop="0"

Menu = Pantalla_Principal("Encendido") ; Producto_Cliente = Producto(-1,"",[],[],[]) ; Escaner_Producto =  Escaner(0.0,[],[])

while Stop!="-1":
    sys.stdout.flush()
    time.sleep(1)
    os.system ("cls")
    Menu.Inicio()
    if len(Total_Compra) != 0:  Menu.Agregado_P() ; Escaner_Producto.Mostrar_Pedido() 
    Menu.Instruccion_P()
    Codigo    = input("\nIngrese El Codigo Del Producto : ")  
    N_Unidad  = input("\nIngrese El Numero De Unidades (Numeros Enteros) Del Producto : ")
    Producto_Cliente = Producto(0,N_Unidad,[],[],[])
    if Producto_Cliente.Validar_P() !=True: Menu.Error_P() ; time.sleep(1)
    else:
        Name_Producto = input("\nIngrese El Nombre Del Producto : ")
        Valor         = input("\nIngrese El Valor Del Producto x Unidad : $ ")
        Producto_Cliente = Producto(1,Valor,[],[],[]) 
        if Producto_Cliente.Validar_P() !=True: Menu.Error_P() ; time.sleep(1)
        else:
            Descuento  = input("\nIngrese El Porcentaje Del Descuento Si Existe : ")
            Producto_Cliente = Producto(2,Descuento,[],[],[])
            if Producto_Cliente.Validar_P() !=True: Menu.Error_P() ; time.sleep(1)
            else:            
                Articulos.append(Codigo) ; Articulos.append(N_Unidad) ; Articulos.append(Name_Producto) ; Articulos.append(Valor) ; Articulos.append(Descuento)
                Sub_Total.append((int(N_Unidad) * float(Valor)) - ((float(Descuento)/100) * (int(N_Unidad) * float(Valor))))
                Producto_Cliente = Producto(-1,"",Sub_Total,Articulos,Total_Compra)
                Producto_Cliente.Crear_Producto() 
                Escaner_Producto =  Escaner(Total_Precio,Sub_Total,Total_Compra)
                Total_Precio = Escaner_Producto.Total_Pedido()
    Stop = input("\n\t\tIngrese El Numero -1 Si Desea Terminar El Pedido : ")

os.system ("cls") ; sys.stdout.flush() ; time.sleep(1) ; Menu.Articulo_F() ; Menu.Agregado_P() ; Escaner_Producto.Mostrar_Pedido()

Eliminar = input("\n\n\tPARA CONTINUAR INGRESE 0 , PARA ELIMINAR UN ARTICULO INGRESE EL NUMERO DEL ARTICULO : ")
if Eliminar!="0":
    if Escaner_Producto.Validar_Item_ELiminado(Eliminar)==False:
        while Eliminar!="0":
            Eliminar = input("\n\n\tPARA CONTINUAR INGRESE 0 , PARA ELIMINAR UN ARTICULO INGRESE EL NUMERO DEL ARTICULO : ")
            if Escaner_Producto.Validar_Item_ELiminado(Eliminar)!=False:
                Escaner_Producto.Validar_Item_ELiminado(Eliminar)
                Eliminar = "0"



os.system ("cls")
Menu.Articulo_F() ; Menu.Agregado_P() ; Escaner_Producto.Mostrar_Pedido()



    



    

