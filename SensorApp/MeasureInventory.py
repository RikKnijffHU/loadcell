import RPi.GPIO as GPIO
import time
import sys
import numpy as np
from hx711 import HX711

class MeasureInventory(object):
   
    def __init__(self, products):
        self.products = products

    def cleanAndExit(self):
        print("Cleaning...")
        GPIO.cleanup()
        print("Bye!")
        sys.exit()

    def reject_outliers(self, data, m=2):
      return data[abs(data - np.mean(data)) < m * np.std(data)]

    def setGPIOPofProduct(self, product):
        hx = HX711(int(product.DT), int(product.SCK))
        
    # I've found out that, for some reason, the order of the bytes is not always the same between versions of python, numpy and the hx711 itself.
    # Still need to figure out why does it change.
    # If you're experiencing super random values, change these values to MSB or LSB until to get more stable values.
    # There is some code below to debug and log the order of the bits and the bytes.
    # The first parameter is the order in which the bytes are used to build the "long" value.
    # The second paramter is the order of the bits inside each byte.
    # According to the HX711 Datasheet, the second parameter is MSB so you shouldn't need to modify it.
        hx.set_reading_format("LSB", "MSB")

    # HOW TO CALCULATE THE REFFERENCE UNIT
    # To set the reference unit to 1. Put 1kg on your sensor or anything you have and know exactly how much it weights.
    # In this case, 92 is 1 gram because, with 1 as a reference unit I got numbers near 0 without any weight
    # and I got numbers around 184000 when I added 2kg. So, according to the rule of thirds:
    # If 2000 grams is 184000 then 1000 grams is 184000 / 2000 = 92.
    #hx.set_reference_unit(113)
        hx.set_reference_unit(1104)

        hx.reset()
        hx.tare()
        return hx

    def measureProducts(self):
       productHXList = []
       for product in self.products:
           productHXList.append(self.setGPIOPofProduct(product))
       while True:
        for hx in productHXList:
            try:
            # These three lines are usefull to debug wether to use MSB or LSB in the reading formats
            # for the first parameter of "hx.set_reading_format("LSB", "MSB")".
            # Comment the two lines "val = hx.get_weight(5)" and "print val" and uncomment the three lines to see what it prints.
            #np_arr8_string = hx.get_np_arr8_string()
            #binary_string = hx.get_binary_string()
            #print binary_string + " " + np_arr8_string
        
            # Prints the weight. Comment if you're debbuging the MSB and LSB issue.
                val_array = np.empty((0))
                for x in range(0, 9): 
                    val = max(0, int(hx.get_weight(5)))
                    print(val)
                    val_array = np.append(val_array, [val])
                    
                    hx.power_down()
                    hx.power_up()
                    time.sleep(1)
                print(val_array)
                results = self.reject_outliers(val_array)
                print(results)
                weight = np.sum(results)/len(results)
                print(weight)
                inventory = round((weight - 19)/4)
                print(inventory + 'g')
            except (self,KeyboardInterrupt, SystemExit):
                self.cleanAndExit()