from MeasureInventory import MeasureInventory
from Model.EnvironmentVariableMapper import EnvironmentVariableMapper as mapper
from EnvironmentVariableReader import EnvironmentVariableReader as reader
from MessageController import MessageController as con
class Startup(object):
    """startup class"""
    variablesList = reader.ReadEnvironmentVariables()
    productList = mapper.MapEnvironmentVariables(variablesList)
    measureInventory = MeasureInventory(productList)
    productHxList = measureInventory.setupProductHxList()
    while True:
        try:
            productMeasurementList = measureInventory.measureProducts(productHxList)
            for product in productMeasurementList:
                con.sendMeasurement(product)
        except (measureInventory,KeyboardInterrupt, SystemExit):
                measureInventory.cleanAndExit()
    
if __name__ == '__main__':
 Startup.main()