import os
class EnvironmentVariableReader(object):
    """description of class"""

    def ReadEnvironmentVariables():
        enviromentList: List[str] = os.environ.get('Products').split(',')
        #enviromentList = 'thee:4:14:15:19'.split(',')
        return enviromentList

