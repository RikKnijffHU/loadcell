import os
from Product import Product
from MeasureInventory import MeasureInventory
class Startup(object):
    """description of class"""
   
    def ReadEnviromentVariables(self):
        productList: List[Product] = []
        #enviromentList: List[str] = os.environ.get('Products').split(',')
        enviromentList: List[str] = 'thee:2:14:15'.split(',')
        for enviromentVariables in enviromentList:
            print(enviromentVariables) 
            variable: List[str]  = enviromentVariables.split(':')
            product = Product(variable[0],variable[1],variable[2],variable[3])
            productList.append(product)
            print(len(enviromentList))    

        return productList
    
if __name__ == '__main__':
 measureInventory = MeasureInventory(Startup().ReadEnviromentVariables())
 measureInventory.measureProducts()