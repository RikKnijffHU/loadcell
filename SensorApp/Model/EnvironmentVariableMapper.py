from Model.Product import Product
class EnvironmentVariableMapper(object):
    """description of class"""
    @staticmethod
    def MapEnvironmentVariables(enviromentList):
        productList = []
        for enviromentVariables in enviromentList:
                print(enviromentVariables) 
                variable = enviromentVariables.split(':')
                product = Product(variable[0],float(variable[1]),variable[2],variable[3],float(variable[4]))
                productList.append(product)
                print(len(enviromentList))    

        return productList
