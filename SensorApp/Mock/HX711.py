class HX711(object):
    """description of class"""
    
    def __init__(self, dout, pd_sck, gain=128):
        self.PD_SCK = pd_sck
        self.DOUT = dout
        

    def set_reference_unit(*args, **xargs):
        pass
    
    def get_weight(*args, **xargs):
        value = self.get_value(times)
        value = value / self.REFERENCE_UNIT
        return value

    def tare(*args, **xargs):   
        pass

    def reset(*args, **xargs):
        pass
    
    def set_reading_format(self, byte_format="LSB", bit_format="MSB"):
        pass