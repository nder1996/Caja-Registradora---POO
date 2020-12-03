import math,string




def Validar(Atributo,Item):
    if Item!=0:
        
        
        if Item==1 and type(Atributo)!=str:
            if type(Atributo) == float:
                return True
        if Item==2:
            if type(Atributo) == float and type(Atributo)!=str:
                if Atributo <= 100.0:
                    return True
                else:
                    return False
        if type(Atributo)==str:
            return False
            
        
        



Entero = input("\n\n\nIngrese un numero : ")

Validar(Entero,1)



