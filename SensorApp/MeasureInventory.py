import RPi.GPIO as GPIO
import time
import sys
import numpy as np
from outliers import smirnov_grubbs as grubbs
from Model.Product import Product
from Model.ProductHX import ProductHX
from hx711 import HX711

class MeasureInventory(object):
   
    def __init__(self, products):
        self.products = products

    def cleanAndExit(self):
        print("Cleaning...")
        GPIO.cleanup()
        print("Bye!")
        sys.exit()

    def setGPIOofProduct(self, product):
        hx = HX711(int(product.DT), int(product.SCK))
        hx.set_reading_format("LSB", "MSB")
        hx.set_reference_unit(1104)
        hx.reset()
        hx.tare()
        return hx

    def ReadMultipleMeasurements(self, hx, measurements):
        val_array = np.empty((0))
        for x in range(0, measurements): 
            val = max(0, int(hx.get_weight(5)))
            print(val)
            val_array = np.append(val_array, [val])
            
            hx.power_down()
            hx.power_up()
            time.sleep(1)
        return val_array

    def reject_outliers(self, val_array):
        results = grubbs.test(val_array, alpha=0.05)
        return results

    def calculateTotalAverageInGrams(self, results):
        weight = np.sum(results)/len(results)
        return weight

    def calculateUnits(self, totalWeight, containerWeight, productWeight):
        inventory = round((totalWeight - containerWeight)/productWeight)
        return inventory

    def setupProductHxList(self):
        productHXList = []
        for product in self.products:
            productHXList.append(ProductHX(product, self.setGPIOofProduct(product)))
        return productHXList

    def measureProducts(self, productHXList):
        productAmountList = []
        for productHX in productHXList:
                val_array = self.ReadMultipleMeasurements(productHX.hx711, 10)
                print(val_array)
                results = self.reject_outliers(val_array)
                print(results)
                totalWeight = self.calculateTotalAverageInGrams(results)
                print("{}{}".format(totalWeight , 'gram'))
                amount = self.calculateUnits(totalWeight,productHX.product.containter, productHX.product.weight)
                print("{}{}".format(amount , 'theezakjes'))
                productHX.product.amount = amount
                productAmountList.append(productHX.product)
        return productAmountList
            