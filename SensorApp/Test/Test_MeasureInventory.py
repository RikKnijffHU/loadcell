import unittest
import MeasureInventory
from Mock import GPIO
from Model.Product import Product
from unittest.mock import patch
from Mock import HX711


class Test_MeasureInventory(unittest.TestCase):
    @patch('MeasureInventory.GPIO', new = GPIO)
    def test_InitSchouldCreateMeasureInventoryObjectWithProductList(self):
        productList = []
        product = Product('thee grey','2','14','15')
        productList.append(product)
        measureInventory = MeasureInventory.MeasureInventory(productList)
        
        self.assertEqual(measureInventory.products, productList)

    @patch('MeasureInventory.GPIO', new = GPIO)
    
    @patch('MeasureInventory.HX711', return_value= HX711.HX711)
    def test_setGPIOofProductSchouldReturnCorrectDoutAndSCK(self, hx711):
        productList = []
        product = Product('thee grey','2','14','15')
        productList.append(product)
        measureInventory = MeasureInventory.MeasureInventory(productList)
        hx= measureInventory.setGPIOPofProduct(product)
        self.assertEqual(hx, 14)
        
        
        
if __name__ == '__main__':
    unittest.main()
