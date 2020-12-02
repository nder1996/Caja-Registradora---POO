import sys,string


def Validar_Item_ELiminado(self,Eliminar):
    if self.Item!="0":
        if Eliminar.isdigit()==True:
            if int(self.Item) <= len(self.Compra_Total):
                Eliminar   = Eliminar - 1
                Compra_Total.pop(int(Eliminar))
                sys.exit(0)
    return False


