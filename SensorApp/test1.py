import unittest
from Startup import Startup
import mock

class Test_Startup(unittest.TestCase):

    @mock.patch('Startup.os.environ.get')
    @mock.patch('Startup.MeasureInventory')
    @mock.patch('Startup.MeasureInventory.RPi.GPIO')
    def test_SchouldreturnOneProduct(self, os_eviron_get):
        os_eviron_get.return_value ='thee grey:2:14:15'
        test: Startup = Startup()
        nummer = len(test.ReadEnviromentVariables())
        self.assertEqual(nummer, 1)

    @mock.patch('Startup.os.environ.get')
    @mock.patch('Startup.MeasureInventory')
    def test_SchouldreturnTwoProduct(self, os_eviron_get):
        os_eviron_get.return_value ='thee grey:2:14:15,thee aardbei:2:16:17'
        test: Startup = Startup()
        nummer = len(test.ReadEnviromentVariables())
        self.assertEqual(nummer, 2)

    @mock.patch('Startup.os.environ.get')
    @mock.patch('Startup.MeasureInventory')
    def test_SchouldreturnCorrectProductParameters(self, os_eviron_get):
        os_eviron_get.return_value ='thee grey:2:14:15'
        test: Startup = Startup()
        product = test.ReadEnviromentVariables()[0]
        self.assertEqual(product.name, 'thee grey')
        self.assertEqual(product.weight, '2')
        self.assertEqual(product.DT, '14')
        self.assertEqual(product.SCK, '15')

if __name__ == '__main__':
    unittest.main()
