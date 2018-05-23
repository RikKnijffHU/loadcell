import unittest
import sys
import MeasureInventory
from Mock import GPIO
from Model.Product import Product
from unittest.mock import patch
from Mock.HX711 import HX711


class Test_MeasureInventory(unittest.TestCase):
    @patch('MeasureInventory.GPIO', new = GPIO)
    @patch('MeasureInventory.HX711', new = HX711)
    def test_InitSchouldCreateMeasureInventoryObjectWithProductList(self):
        productList = []
        product = Product('thee grey','2','14','15','19')
        productList.append(product)
        measureInventory = MeasureInventory.MeasureInventory(productList)
        
        self.assertEqual(measureInventory.products, productList)

    @patch('MeasureInventory.GPIO', new = GPIO)
    @patch('MeasureInventory.HX711' , new = HX711)
    def test_setGPIOofProductSchouldReturnCorrectDoutAndPD_SCK(self):
        productList = []
        product = Product('thee grey','2','14','15','19')
        
        productList.append(product)
        measureInventory = MeasureInventory.MeasureInventory(productList)
        
        hx= measureInventory.setGPIOofProduct(product)
        self.assertEqual(hx.DOUT, 14)
        self.assertEqual(hx.PD_SCK, 15)

    @patch('MeasureInventory.GPIO', new = GPIO)
    @patch('MeasureInventory.HX711' , new = HX711)
    def test_setGPIOofProductSchouldReturnCorrectDoutAndPD_SCK(self):
        productList = []
        product = Product('thee grey','2','14','15','19')
        
        productList.append(product)
        measureInventory = MeasureInventory.MeasureInventory(productList)
        
        hx= measureInventory.setGPIOofProduct(product)
        self.assertEqual(hx.DOUT, 14)
        self.assertEqual(hx.PD_SCK, 15)

    @patch('MeasureInventory.GPIO', new = GPIO)
    @patch('MeasureInventory.HX711' , new = HX711)
    def test_calculateTotalAverageInGramsSchouldReturnCorrectTotalWeight(self):
        productList = []
        product = Product('thee grey','2','14','15','19')
        MeasurementList=[29,30,29,30,31,31,30,29,31,30]
        productList.append(product)
        measureInventory = MeasureInventory.MeasureInventory(productList)
        
        totalWeight= measureInventory.calculateTotalAverageInGrams(MeasurementList)
        self.assertEqual(totalWeight, 30)

    @patch('MeasureInventory.GPIO', new = GPIO)
    @patch('MeasureInventory.HX711.get_weight' ,return_value = 30)
    @patch('MeasureInventory.HX711' , new = HX711)
    def test_ReadMultipleMeasurementsSchouldReturnListWithLenghtTen(self, mock_method):
        productList = []
        product = Product('thee grey','2','14','15','19')
        
        productList.append(product)
        measureInventory = MeasureInventory.MeasureInventory(productList)
        hx= measureInventory.setGPIOofProduct(product)
        

        MeasurementList = measureInventory.ReadMultipleMeasurements(hx,10)
        self.assertEqual(len(MeasurementList), 10)

    @patch('MeasureInventory.GPIO', new = GPIO)
    @patch('MeasureInventory.HX711.get_weight' ,return_value = 30)
    @patch('MeasureInventory.HX711' , new = HX711)
    def test_ReadMultipleMeasurementsSchouldReturnListWithLenghtFive(self, mock_method):
        productList = []
        product = Product('thee grey',2,'14','15','19')
        
        productList.append(product)
        measureInventory = MeasureInventory.MeasureInventory(productList)
        hx= measureInventory.setGPIOofProduct(product)
        

        MeasurementList = measureInventory.ReadMultipleMeasurements(hx,5)
        self.assertEqual(len(MeasurementList), 5)

    @patch('MeasureInventory.GPIO', new = GPIO)
    @patch('MeasureInventory.HX711' , new = HX711)
    def test_calculateUnitsSchouldReturnTenUnits(self):
        productList = []
        product = Product('thee grey',4.1,'14','15',19)
        
        productList.append(product)
        measureInventory = MeasureInventory.MeasureInventory(productList)     

        Units= measureInventory.calculateUnits(59,product.container,product.weight)
        self.assertEqual(Units,9)

    @patch('MeasureInventory.GPIO', new = GPIO)
    @patch('MeasureInventory.HX711' , new = HX711)
    def test_calculateUnitsSchouldReturnSixUnits(self):
        productList = []
        product = Product('thee grey',4.1,'14','15',19.0)
        
        productList.append(product)
        measureInventory = MeasureInventory.MeasureInventory(productList)     

        Units = measureInventory.calculateUnits(41,product.container,product.weight)
        self.assertEqual(Units, 5)

    @patch('MeasureInventory.GPIO', new = GPIO)
    @patch('MeasureInventory.HX711' , new = HX711)
    def test_setupProductHxListSchouldReturnCorrectAttributeValues(self):
        productList = []
        product = Product('thee grey',4.1,14,15,19)
        
        productList.append(product)
        measureInventory = MeasureInventory.MeasureInventory(productList)     

        productHXList = measureInventory.setupProductHxList()
        self.assertEqual(productHXList[0].product.name, 'thee grey')
        self.assertEqual(productHXList[0].product.container, 19)
        self.assertEqual(productHXList[0].product.DT, 14)
        self.assertEqual(productHXList[0].product.SCK, 15)

    @patch('MeasureInventory.GPIO', new = GPIO)
    @patch('MeasureInventory.HX711' , new = HX711)
    def test_setupProductHxListSchouldReturnListWithTwoProductHX(self):
        productList = []
        product = Product('thee grey',4.1,14,15,19)
        product2= Product('thee aardbei',2,16,17,12)
        
        productList.append(product)
        productList.append(product2)
        measureInventory = MeasureInventory.MeasureInventory(productList)     

        productHXList = measureInventory.setupProductHxList()
        self.assertEqual(len(productHXList), 2)
        

        
    @patch('MeasureInventory.GPIO', new = GPIO)
    @patch('MeasureInventory.HX711' , new = HX711)
    def test_reject_outliersSchouldReturnListWithoutOutliers(self):
        productList = []
        product = Product('thee grey',4.1,14,15,19)
        measurementList=[29,30,1029,30,31,31,1,29,31,30]      
        productList.append(product)
        
        measureInventory = MeasureInventory.MeasureInventory(productList)     

        result = measureInventory.reject_outliers(measurementList)
        self.assertEqual(len(result), 8)

if __name__ == '__main__':
    unittest.main()
