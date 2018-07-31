import matplotlib.pyplot as plt
import numpy as np
from  math import*

"""

sON     =  "abs(   (0>sin(200*pi*Ch(""t"")+A )) AND   (0>sin(200*pi*Ch(""t"")+B )))"
sOFF    =  "abs(NOT(0>sin(200*pi*Ch(""t"")+A )) OR NOT(0>sin(200*pi*Ch(""t"")+B )))"
sSINrec =  "abs(sin(100*pi*Ch(""t"")))"
sDECH   = "pp1* (arctan(tan(100*pi*Ch(""t""))) + pp2)"

 sFormula1 = "C*(" & sON  & "*" & sSINrec & "+" & sOFF & " * " & sDECH & ") + O"

Sub setDCI(iCurve,sSymbols,sValues,sUnit,Pts,t0,dt)
'      sSymbols = array("Ampl" , "Start"     ,  "Stop"         , "pp1"     , "pp2"     , "sUnit", "O"   , "Pts", "t0", "dt")
       sSymbols = array("C"    , "A"         ,  "B"            , "pp1"     , "pp2"     , "sUnit", "O"   , "Pts", "t0", "dt")
select case iCurve
 Case 1 sValues = array("0"    , pi/3600*3575, pi/360000*56285 , -0.010378 , -94.79208 , "A"    ,  1000 , 10001,  0.0, 2E-5)
 Case 2 sValues = array("1000" , pi/3600*3575, pi/360000*56285 , -0.010378 , -94.79208 , "A"    ,  0    , 10001,  0.0, 2E-5)
"""
A = pi/3600*3575
B = pi/360000*56285
C = 1000
pp1 = -0.010378
pp2 = -94.79208
O = 0

Fs = 1000000
f = 100
sample = 20000
x = np.arange(sample)
#y = np.sin(2 * np.pi * f * x / Fs)

sON     =  abs((0>np.sin(100*pi*x/Fs+A)) * (0>np.sin(100*pi*x/Fs+B)) )
sOFF    =  abs((0<np.sin(100*pi*x/Fs+A)) * (0>np.sin(100*pi*x/Fs+B)) )
sSINrec =  abs(np.sin(100*pi* x/Fs ))
sDECH   =  pp1* (np.arctan(np.tan(100*pi* x/Fs )) + pp2)

# sFormula1 = "C*(" & sON  & "*" & sSINrec & "+" & sOFF & " * " & sDECH & ") + O"        
y           =  sON
#y1          =  sOFF
#y            =  C*                  sSINrec + O
#y1           =  C*(    sON     *    sSINrec    +    sOFF     *     sDECH    ) + O
#y1          =  C*  sSINrec + O


plt.plot(x, y) #, y1)
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()
