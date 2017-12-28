# -*- coding: utf-8 -*-
HHV = 1.482
uF = 0.95
F=96500
R1=8.314
InputParams = {"T": "Cell Operation Temperature [K]", "PH2": "Partial Pressure [atm]", "PO2": "Partial Pressure [atm]",
               "i-start": "Cell operating current start point [A]", "i-step": "Cell operating current step",
               "i-stop": "Cell operating current end point [A]",
               "lambda": "is an adjustable parameter with a min value of 14 and max value of 23",
               "N": "Number Of Single Cells", "R": "R-Electronic [ohm] (*Optional)",
               "alpha": "charge transfer coefficient",
               "I_N": "maximum current density [A/cm2]",
               "I_0":"maximum current density [A/cm2]",
               "I_Lim":"maximum current density [A/cm2]"}
OutputParams = {"Enernst": "V","Vcell": "V", "PEM Efficiency": "", "Power": "W", "VStack": "V"}