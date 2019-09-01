# -*- coding: utf-8 -*-
# curveplot2.py
import matplotlib.pyplot as plt
import numpy as np
from  math import*

A = pi/360000*416285
B = pi/360000*357500
C = 1000
pp1 = -0.010378
pp2 = -94.79208
O = 0

sON     = (0<np.sin(200*pi*t+pi/360000*416285)) * (0>np.sin(200*pi*t+pi/360000*357500))

sSINrec = abs(sin(100*pi* t ))

sDECH   = -0.010378 * (atan(tan(100*pi* t)) -94.79208)


#y      = C * (sON*(sSINrec-sDECH) + sDECH) + O

This goes into "new curve formula input field"
1000*((0<sin(200*pi*t+pi/360000*416285)) * (0>sin(200*pi*t+pi/360000*357500))*(abs(sin(100*pi* t ))+0.010378 * (atan(tan(100*pi* t)) -94.79208))-0.010378 * (atan(tan(100*pi* t)) -94.79208))
