import unittest
from unittest.mock import patch
from Model.EnvironmentVariableMapper import EnvironmentVariableMapper as Mapper

class Test_Test_EnvironmentVariableMapper(unittest.TestCase):
   
     
     def test_SchouldreturnCorrectProductParameters(self):
            variableList = []
            variableList.append('thee grey:2:14:15:19')
            
            product = Mapper.MapEnvironmentVariables(variableList)[0]
            self.assertEqual(product.name, 'thee grey')
            self.assertEqual(product.weight, '2')
            self.assertEqual(product.DT, '14')
            self.assertEqual(product.SCK, '15')

     def test_SchouldreturnListWithOneProduct(self):
            variableList = []
            variableList.append('thee grey:2:14:15:19')
            
            list = Mapper.MapEnvironmentVariables(variableList)
            self.assertEqual(1,len(list))

     def test_SchouldreturnListWithTwoProducts(self):
            variableList = []
            variableList.append('thee grey:2:14:15:19')
            variableList.append('thee aardbei:2:16:17:19')
            
            list = Mapper.MapEnvironmentVariables(variableList)
            self.assertEqual(2,len(list))
           

if __name__ == '__main__':
    unittest.main()
