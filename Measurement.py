import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import physipy
from physipy import units

def FindU(it):
    output = 0
    for item in it:
        output += item ** 2
    return output * 0.5

class Quantity:
    def __init__(self):
        self.name = None
        self.value = None
        self.unit = None
        self.uncertainty = None

    def __add__(self, other):
        if self.unit != other.unit:
            raise Exception("Wrong units!")
        output = Measurement()
        output.value = self.value + other.value
        output.uncertainty = self.uncertainty + other.uncertainty
        return output

    def __repr__(self):
        unc = ""
        if self.uncertainty:
            unc = f"+-{self.uncertanty}"
        return f"Quantity: {self.quantity} = {self.value}{unc}{self.unit.str_SI_unit()}"

    def __add__(self, other):
        if self.unit != other.unit:
            raise Exception("Wrong units!")
        output = Quantity()
        output.name = self.quantity
        output.value = self.value + other.value
        if self.uncertainty and other.uncertainty:
            output.uncertainty = self.uncertainty + other.uncertainty
        elif self.uncertainty:
            output.uncertainty = self.uncertainty
        elif other.uncertainty:
            output.uncertainty = other.uncertainty
        return output

    def __sub__(self, other):
        if self.unit != other.unit:
            raise Exception("Wrong units!")
        output = Quantity()
        output.name = self.quantity
        output.value = self.value - other.value
        if self.uncertainty and other.uncertainty:
            output.uncertainty = self.uncertainty + other.uncertainty
        elif self.uncertainty:
            output.uncertainty = self.uncertainty
        elif other.uncertainty:
            output.uncertainty = other.uncertainty
        return output

    def __mul__(self, other):
        if type(other) == type(Quantity()) or type(other) == type(Measurement()):
            output = Quantity()
            output.value = self.value * other.value

            if self.uncertainty and other.uncertainty:
                output.uncertainty = (self.uncertainty/self.value + other.uncertainty/other.value) * self.value
            elif self.uncertainty:
                output.uncertainty = self.uncertainty * other.value
            elif other.uncertainty:
                output.uncertainty = other.uncertainty * self.value

            if self.unit and other.unit:
                output.unit = other.unit * self.unit
            elif self.unit:
                output = self.unit
            elif other.unit:
                output = other.unit
            return output
        else:
            output = Quantity()
            output.value = self.value * other
            if self.uncertainty:
                output.uncertainty = self.uncertainty * other
            if self.unit:
                output.unit = self.unit
            return output

    def __truediv__(self, other):
        if type(other) == type(Quantity()) or type(other) == type(Measurement()):
            output = Quantity()
            output.value = self.value / other.value
            output.uncertainty = (self.uncertainty/self.value + other.uncertainty/other.value) * output.value
            if self.unit and other.unit:
                output.unit = other.unit / self.unit
            elif self.unit:
                output = self.unit
            elif other.unit:
                output = 1 / other.unit
            return output
        else:
            output = Quantity()
            output.value = self.value / other
            output.uncertainty = self.uncertainty / other
            if self.unit:
                output.unit = self.unit
            return output



class Measurement(Quantity):
    def __init__(self):
        super().__init__()
        self.time = datetime.now()
        self.quantity = None

    def __repr__(self):
        unc = ""
        if self.uncertainty:
            unc = f"+-{self.uncertanty}"
        return f"Measeured {self.quantity} = {self.value}{unc}{self.unit} at {self.time}"



class Measurements:
    def __init__(self):
        self.table = []
        self.name = None
        self.units = None
        self.uncertainty = None
        self.np = np.array([])

    def save_np(self):
        for item in self.table:
            self.np = np.append(self.np, item.value)

    def graph(self):
        plt.bar(range(len(self.np)), self.np, yerr=self.uncertainty)
        plt.show()

    def calc_uncertainty(self):
        self.uncertainty = FindU([item.uncertainty for item in self.table])
        # print(self.uncertainty)

    def add_uncertanty(self, unc):
        self.uncertainty = FindU([self.uncertainty, unc])
