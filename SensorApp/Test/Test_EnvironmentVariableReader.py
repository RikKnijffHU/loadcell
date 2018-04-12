import unittest
import os
from unittest.mock import patch
from EnvironmentVariableReader import EnvironmentVariableReader as Reader


class Test_EnvironmentVariableReader(unittest.TestCase):
    
    @patch('EnvironmentVariableReader.os.environ.get')
    def test_SchouldreturnListWithOneString(self, os_eviron_get):
        os_eviron_get.return_value ='thee grey:2:14:15:19'
        
        nummer = len(Reader.ReadEnvironmentVariables())
        self.assertEqual(nummer, 1)

    @patch('EnvironmentVariableReader.os.environ.get')
    def test_SchouldreturnListWithTwoStrings(self, os_eviron_get):
        os_eviron_get.return_value ='thee grey:2:14:15:19,thee aardbei:2:16:17:19'
        
        nummer = len(Reader.ReadEnvironmentVariables())
        self.assertEqual(nummer, 2)

if __name__ == '__main__':
    unittest.main()
