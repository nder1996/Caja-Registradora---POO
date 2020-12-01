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
        Pedido = "\n\n|| {} UNIDADES DE {} TIENE UN DESCUENTO DE {} % \n\n|| SUB-TOTAL A PAGAR ES $ {} USD".format(self.Articulo[1],self.Articulo[2],self.Articulo[4],self.Sub_Total[len(self.Sub_Total)-1])
        self.Compra_Total.append(Pedido)
        self.Articulo.clear()
        return self.Compra_Total
    
    def Sub_Total(self):
        return self.Sub_Total        
class Escaner():
    def __init__(self,Total,Eliminar_Articulo,Sub_Total,Compra_Total):
        self.Total              = Total
        self.Eliminar_Articulo  = Eliminar_Articulo
        self.Sub_Total          = Sub_Total
        self.Compra_Total       = Compra_Total
        
        
    def Mostrar_Pedido(self):
        Contador = 0
        print("SUB TOTAL : {} -  - Productos : {} - Eliminar_Item : {} ".format(self.Sub_Total,self.Total,self.Eliminar_Articulo))
        for i in self.Compra_Total:
            Contador+=1
            print("\nPRODUCTO : ",Contador,"\n\n",i)
        
    def Total_Pedido(self):
        for i in range(len(self.Sub_Total)):
            self.Total = self.Total + float(self.Sub_Total[i])
        return self.Total
    
    def Validar_Item_ELiminado(self):
        if self.Item!="0":
            if int(self.Item) <= len(self.Compra_Total):
                self.Eliminar_Articulo = self.Eliminar_Articulo - 1
                self.Compra_Total.pop(int(self.Eliminar_Articulo))
                sys.exit(0)
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

    def Articulo_C(self):
        print("\n\n\n\t\t\t| PRODUCTO AGREGADO CON EXITO |")
        print("\n\t\t\t\t      *|* \n")  
    
    def Articulo_F(self):
        print("\n\n\t\t       |P E D I D O  F I N A L I Z A D O| ")
        print("\n\t\t\t\t      *|* \n")
    
    def Agregado_P(self):
        print("\n\n\n\t\t\t    | PRODUCTOS AGREGADOS|")
        print("\n\n")
        
    def Total(self,Total):
        print("\n\n\t\t\t    | TOTAL : $ {} USD |\n".format(float(Total)))
        print("\n\n")


Articulos= [] ;Total_Compra = [] ; Item = [] ; Atributo = "" ; Sub_Total = [] ; Total_Precio = 0.0 ; Eliminar = "-1" ; Stop="0"

Menu = Pantalla_Principal("Encendido") ; Producto_Cliente = Producto(-1,"",[],[],[]) ; Escaner_Producto =  Escaner([],0,[],[])

while Stop!="-1":
    os.system ("cls")
    Menu.Inicio()
    if len(Total_Compra) != 0: Escaner_Producto.Mostrar_Pedido() 
    Codigo    = input("\nIngrese El Codigo Del Producto : ")  
    N_Unidad  = input("\nIngrese El Numero De Unidades (Numeros Enteros) Del Producto : ")
    Producto_Cliente = Producto(0,N_Unidad,[],[],[])
    if Producto_Cliente.Validar_P() !=True: Menu.Error_P()
    else:
        Name_Producto = input("\nIngrese El Nombre Del Producto : ")
        Valor         = input("\nIngrese El Valor Del Producto x Unidad : $ ")
        Producto_Cliente = Producto(1,Valor,[],[],[]) 
        if Producto_Cliente.Validar_P() !=True: Menu.Error_P()
        else:
            Descuento  = input("\nIngrese El Porcentaje Del Descuento Si Existe : ")
            Producto_Cliente = Producto(2,Descuento,[],[],[])
            if Producto_Cliente.Validar_P() !=True: Menu.Error_P()
            else:
                Articulos.append(Codigo) ; Articulos.append(N_Unidad) ; Articulos.append(Name_Producto) ; Articulos.append(Valor) ; Articulos.append(Descuento)
                Sub_Total.append((int(N_Unidad) * int(Valor)) - ((float(Descuento)/100) * (int(N_Unidad) * int(Valor))))
                Producto_Cliente = Producto(-1,"",Sub_Total,Articulos,Total_Compra)
                Compra_Total = Producto_Cliente.Crear_Producto() ; Sub_Total = Producto_Cliente.Sub_Total()
                print("SUB TOTAL : {} -  - Productos : {} - Eliminar_Item : {} ".format(Sub_Total,Total_Precio,Eliminar))
                time.sleep(10)
                #Escaner_Produto =  Escaner(Total_Precio,"-1",Sub_Total,Total_Compra)
                #Escaner_Producto.Mostrar_Pedido()
                #time.sleep(3)
                
                
                
                #("Ola_Mundo")
                #Total_Precio    = Escaner_Producto.Total_Pedido()
                #print("TOTAL_PRECIO : ",Total_Precio)
            
        
    
    
    
    
    #N_Unidad  = input("\nIngrese El Numero De Unidades (Numeros Enteros) Del Producto : ")
   # Producto_Cliente.Validar_P()
   # N_Unidad  = input("\nIngrese El Numero De Unidades (Numeros Enteros) Del Producto : ")
   # Producto_Cliente.Validar_P() 
    
    

    #Producto_Cliente = Producto(Item,Atributo,Sub_Total,Lista1,List_1)
   # if Producto_Cliente.Validar_P() == True:
    #    Producto_Cliente.Crear_Producto() 
    #    Escaner_P = Escaner(Item,Atributo,Sub_Total,Lista1,List_1,Eliminar,Total)
   #     Total = Escaner_P.Total_Pedido()
  #      Escaner_P.Mostrar_Pedido()
    
    



    

