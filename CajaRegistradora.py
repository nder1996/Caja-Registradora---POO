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
        Pedido = "\n\n|| {} UNIDADES DE {} TIENE UN DESCUENTO DE {} % \n\n|| SUB-TOTAL A PAGAR ES $ {:.3f} USD".format(self.Articulo[1],self.Articulo[2],self.Articulo[4],float(self.Sub_Total[len(self.Sub_Total)-1]))
        self.Compra_Total.append(Pedido)
        self.Articulo.clear()

class Escaner:
    def __init__(self,Sub_Total,Compra_Total):
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
            
    def Total_Pedido(self,Total):
        for i in range(len(self.Sub_Total)):
            Total = Total + float(self.Sub_Total[i])
        return Total

    def Validar_Item_ELiminado(self,Eliminar):
        if Eliminar!="0":
            if Eliminar.isdigit()==True:
                if int(Eliminar) <= len(self.Compra_Total):
                    Eliminar  = int(Eliminar) - 1
                    self.Compra_Total.pop(int(Eliminar))
                    self.Sub_Total.pop(int(Eliminar))
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

class Pantalla_Principal:
    def Inicio(self):
        print("\n")
        print("\n\n\t\t\t|***|  CAJA REGISTRADORA  |***|")
        print("\t\t\t|***|         V2.0        |***|")
        print("\n\n")
        
    def Instruccion_P(self):
        print("\n\n\t   | I N G R E S A  L O S   D A T O S  D E  L A  C O M P R A | \n")
        print("\t\t\t\t      *|* \n")         
    
    def Error_Validar(self):
        print("\n\n\n\t     | P O R  F A V O R  I N G R E S E  U N  P R O D U C T O  V A L I D O |")
        print("\n\t\t\t\t      *|* \n")  

    def Articulo_F(self):
        print("\n\n\t\t       |P E D I D O  F I N A L I Z A D O| ")
        print("\n\t\t\t\t      *|* \n")
    
    def Agregado_P(self):
        print("\n\t\t    | P R O D U C T O S  A G R E G A DO S |")
        print("\n\n")
        
    def Total(self,Total):
        print("\n\n\t\t\t  | TOTAL : $ {:.3f} USD |\n".format(float(Total)))
        print("\n\n")
    
    def Finalizada_Compra(self):
        print("\n\n\t\t       | P A G O  F I N A L I Z A D O | ")
        print("\n\t\t\t\t      *|* \n")
        
    
    def Gracias_Compra(self):
        print("\n\n\t\t       | G R A C I A S  P O R   S U  C O M P R A | ")
        print("\n\t\t\t\t      *|* \n")

    def Eliminar_Producto(self):
        print("\n\n\t| E L I M I N A  E L (L O S)  P R O D U C T O (S)  D E  L A  C O M P R A | ")
        print("\n\t\t\t\t      *|* \n")
        
    def Eliminar_Error(self):
        print("\n\n\t\t   | I N G R E S E  D A T O S  C O R R E C T O S | ")
        print("\n\t\t\t\t      *|* \n")
        
        
        
class Cajon:
    def __init__(self,Total_Precio,Dinero_Cliente):
        self.Total_Precio   = Total_Precio
        self.Dinero_Cliente = Dinero_Cliente
    
    def Pago_Producto(self):
        if float(self.Dinero_Cliente) >=float(Total_Precio):
            return float(self.Total_Precio) - float(self.Dinero_Cliente)
        else:
            return False
    
class Registradora_Caja:
    def __init__(self,Articulos,Total_Compra,Sub_Total,Total_Precio):
        self.Articulos     = Articulos        
        self.Total_Compra  = Total_Compra
        self.Sub_Total     = Sub_Total
        self.Total_Precio  = Total_Precio

    def Proceso_Compra(self):
        Menu = Pantalla_Principal() ; Producto_Cliente = Producto(-1,"",self.Sub_Total,self.Articulos,self.Total_Compra) ; Escaner_Producto =  Escaner(self.Sub_Total,self.Total_Compra) ;Continue="0"
        while Continue!="-1":   
            Stop="0" ; os.system ("cls") ; sys.stdout.flush() ; time.sleep(0.2) 
            while Stop!="-1":
                os.system ("cls") ; sys.stdout.flush() ; time.sleep(0.2)
                if len(self.Total_Compra) != 0: Menu.Inicio() ; Menu.Agregado_P() ; Escaner_Producto.Mostrar_Pedido() 
                else: Menu.Inicio()
                Menu.Instruccion_P()
                Codigo = input("\n Ingrese El Codigo Del Producto : ")
                if Codigo=="": Menu.Error_Validar() ; time.sleep(1)
                else:
                    N_Unidad  = input("\n Ingrese El Numero De Unidades (Numeros Enteros) Del Producto : ")  ;Producto_Cliente = Producto(0,N_Unidad,self.Sub_Total,self.Articulos,self.Total_Compra)
                    if Producto_Cliente.Validar_P() !=True: Menu.Error_Validar() ; time.sleep(1)
                    else:
                        Name_Producto = input("\n Ingrese El Nombre Del Producto : ")
                        if Name_Producto=="": Menu.Error_Validar() ; time.sleep(1)
                        else:    
                            Valor = input("\n Ingrese El Valor Del Producto x Unidad : $ ") ; Producto_Cliente = Producto(1,Valor,self.Sub_Total,self.Articulos,self.Total_Compra) 
                            if Producto_Cliente.Validar_P() !=True: Menu.Error_Validar() ; time.sleep(1)
                            else:
                                Descuento  = input("\n Ingrese El Porcentaje Del Descuento Si Existe : ")  ;Producto_Cliente = Producto(2,Descuento,self.Sub_Total,self.Articulos,self.Total_Compra)
                                if Producto_Cliente.Validar_P() !=True: Menu.Error_Validar ; time.sleep(1)
                                else: 
                                    self.Articulos.append(Codigo) ; self.Articulos.append(N_Unidad) ; self.Articulos.append(Name_Producto) ; self.Articulos.append(Valor) ; self.Articulos.append(Descuento)
                                    self.Sub_Total.append((int(N_Unidad) * float(Valor)) - ((float(Descuento)/100) * (int(N_Unidad) * float(Valor))))
                                    Producto_Cliente = Producto(-1,"",self.Sub_Total,self.Articulos,self.Total_Compra)
                                    Producto_Cliente.Crear_Producto() ; Escaner_Producto =  Escaner(self.Sub_Total,self.Total_Compra)
                                    self.Total_Precio = 0.0 ; self.Total_Precio = Escaner_Producto.Total_Pedido(self.Total_Precio) 
                Stop = input("\n\t\t Ingrese El Numero -1 Si Desea Terminar El Pedido : ")
            Continue = input("\n\n\t DESEA AGREGAR OTRO PRODUCTO(S) A SU COMPRA, DE LO CONTRARIO INGRESE -1 : ")


    def Eliminar_Articulo_Producto(self):
        os.system ("cls") ; sys.stdout.flush() ; time.sleep(0.2)
        Menu = Pantalla_Principal() ; Escaner_Producto =  Escaner(self.Sub_Total,self.Total_Compra) ; Continue="0"
        Menu.Inicio() ; Menu.Articulo_F() ; Menu.Agregado_P() 
        while Continue!="-1" or len(Total_Compra)!=0:
            Stop="0" ; os.system ("cls") ; sys.stdout.flush() ; time.sleep(0.2) 
            while Stop!="-1" or len(Total_Compra)!=0:
                Menu.Inicio()
                Menu.Eliminar_Producto()    
                Escaner_Producto.Mostrar_Pedido() 
                self.Total_Precio = 0.0 
                self.Total_Precio = Escaner_Producto.Total_Pedido(self.Total_Precio)
                Menu.Total(self.Total_Precio)
                Eliminar = input("\n\t\tIngrese El Numero Del Articulo Que Desea Eliminar : ")
                if Escaner_Producto.Validar_Item_ELiminado(Eliminar)==False: 
                    os.system ("cls") ; Menu.Inicio() ;Menu.Eliminar_Error() ; Menu.Eliminar_Producto() ; Escaner_Producto.Mostrar_Pedido() 
                    Eliminar = input("\n\t\tIngrese El Numero Del Articulo Que Desea Eliminar : ")
                else:
                    Total_Precio = 0.0
                    Total_Precio = Escaner_Producto.Total_Pedido(Total_Precio)
                    Stop = "-1"
            if len(self.Compra_Total)!=0:
                Continue = input("\n\n\t DESEA ELIMINAR OTRO PRODUCTO(S) DE LA COMPRA, DE LO CONTRARIO INGRESE -1 : ")
                os.system ("cls")
            else:
                print("\n\n\t T O D A  T U  C O M P R A  H A  S I D O  B O R R A D A : ")
                Continue="-1"
                




"""
while Dinero!=0:
    os.system ("cls") 
    Menu.Inicio()
    Menu.Agregado_P() 
    Escaner_Producto.Mostrar_Pedido()
    Menu.Total(Total_Precio)
    print("PARTE _ 2 - TOTAL")
    Dinero = input("\n\n\tINGRESE LA CANTIDAD DE DINERO CORRESPONDIENDTE USD PARA VALIDAR SU COMRA : $ ")   
    Producto_Cliente = Producto(1,Dinero,[],[],[])
    if Producto_Cliente.Validar_P()!=True: Menu.Error_P() ; time.sleep(1)
    else:
        Recibo = Cajon(Total_Precio,Dinero) 
        if Recibo.Pago_Producto()!=True: Menu.Error_P() ; time.sleep(1)
        else:
            os.system ("cls")
            Menu.Finalizada_Compra() 
            Escaner_Producto.Mostrar_Pedido()
            Menu.Gracias_Compra()
            Dinero="0"
    """
    
if __name__ == "__main__":
    os.system ("cls") ; sys.stdout.flush() ; time.sleep(0.2)  
    Articulos = [] ; Total_Compra = [] ; Sub_Total = [] ; Total_Precio = 0.0 ; Continuar ="0"
    Registradora = Registradora_Caja(Articulos,Total_Compra,Sub_Total,Total_Precio)
    Registradora.Proceso_Compra()
    Registradora.Eliminar_Articulo_Producto()
    

        
    
    
    
    
    
    