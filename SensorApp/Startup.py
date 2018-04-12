from MeasureInventory import MeasureInventory
from Model.EnvironmentVariableMapper import EnvironmentVariableMapper as mapper
from EnvironmentVariableReader import EnvironmentVariableReader as reader
class Startup(object):
    """description of class"""
    variablesList = reader.ReadEnvironmentVariables()
    productList = mapper.MapEnvironmentVariables(variablesList)
    measureInventory = MeasureInventory(productList)
    measureInventory.measureProducts()
    
if __name__ == '__main__':
 Startup.main()