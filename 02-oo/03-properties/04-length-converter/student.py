class LengthConverter:
    FEET_PER_METER = 3.28084
    INCH_PER_METER = 39.3701

    def __init__(self):
        self.__distance_in_meter = 0

    @property
    def meter(self):
        return self.__distance_in_meter

    @property
    def feet(self):
        return self.meter * LengthConverter.FEET_PER_METER

    @property
    def inch(self):
        return self.meter * LengthConverter.INCH_PER_METER

    @meter.setter
    def meter(self, value):
        self.__distance_in_meter = value

    @feet.setter
    def feet(self, value):
        self.__distance_in_meter = value / LengthConverter.FEET_PER_METER

    @inch.setter
    def inch(self, value):
        self.__distance_in_meter = value / LengthConverter.INCH_PER_METER
