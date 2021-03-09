from tkinter import Tk
from tkinter.filedialog import askopenfilename
import re


class Operations(object):
    
    def __init__(self):
        self.orderPath = 'Empty'#Almacena la ruta de ordenes
        self.restaurantName = 'Empty Restaurant'#Nombre restaura
        self.saveListInFirstPosition = ' '#Lista de 1.er posicion de la lista de listas[0][0], con esto no tengo problema porque es la primer linea, no tengo que tener pierde en teoria
        self.finalRN = ' '#Aqui guardo el nombre del restaurante, este valor se obtiene del retorno de la cierta funcion
    
    def uploadOrder(self):
        Tk().withdraw()
        self.orderPath = askopenfilename()

        if self.orderPath:
            print(self.orderPath)
        else:
            print('No se selecciono ningun archivo')
            """
            Me parece que aquí deberé de crear una
            variable booleana para así detectar que 
            no hay ningun archivo seleccionado, para 
            así despues jugar con la misma de manera
            que se pueda saber que no se detecto nada
            para que así se pueda hacer el reporte respectivo
            """

    #------------------Generating menu ---------------
    def threeOption(self):#This is going to work to save all the methods for option 3
        Operations.readOrderFile(self)
        Operations.listingOrders(self)
        self.finalRN = Operations.gettingRestaurantName(self)
        print('nombre del restaurante: ',self.finalRN)
    
    @staticmethod
    def readOrderFile(self):
        self.readingOrder = open(self.orderPath, 'r')
        self.linesInlist = []
        
        for line in self.readingOrder:
            self.linesInlist.append(line)
        self.readingOrder.close()
        print('-----------------------------')
        print('Archivo cargado exitosamente!')
        print('-----------------------------')
        # print(self.linesInlist)

        # print(self.orderPath)
    
    @staticmethod
    def listingOrders(self):
        self.listOfOrders = []
        
        for i in range(len(self.linesInlist)):
            self.listOfOrders.append([self.linesInlist[i]])
        print(self.listOfOrders)
    
    @staticmethod
    def gettingRestaurantName(self):
        self.saveListInFirstPosition = self.listOfOrders[0][0]
        rn = re.findall(r"'(.*?)'", self.saveListInFirstPosition, re.DOTALL)
        finalRN = rn[0]
        return finalRN
