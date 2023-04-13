import csv
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import timeit
from collections import defaultdict as ddict

path = "C:/Users/qfada/Desktop/QFA_FGA_Abaque/Run33/"

def lecture(filename):
    a = []
    data = []
    with open(path + filename,'r') as f:
        data = []
        for x in f:
            data.append(x.strip('\n'))
        f.close()
    data_output = [[] for _ in range(len(data))]
    for i in range(len(data)):
        data[i] = data[i].split(" ")
        for j in range(len(data[i])):
            if data[i][j] != '':
                data_output[i].append(float(data[i][j]))
    return(data_output)

list_FF_summary = []
list_Rayleigh_summary = []
list_FI_summary = []
list_thickness_FGA_summary = []
list_thickness_AC_summary = []
list_thickness_MG20_summary = []
list_thickness_MG112_summary = []
list_condu_avg_FGA = []

#a = lecture("Tdepth.0.dat")

#print(a[320][1])

number_of_files = 240

for i in range(number_of_files):
    a = []
    a = lecture("Tdepth." + str(i) + ".dat")
    list_FF = []
    list_Rayleigh = []
    list_FI = []
    list_thickness_FGA = []
    list_thickness_AC = []
    list_thickness_MG20 = []
    list_thickness_MG112 = []
    air_temp_avg = a[1][4]
    conductivity_FGA = 0.0
    conductivity_FGA_index = -6.2118*air_temp_avg + 183.41
    conductivity_FGA_début = int(-3.1091*air_temp_avg + 181.73)
    conductivity_FGA_fin = int(-3.1727*air_temp_avg + 365.14) + 1 
    #print(conductivity_FGA_début,conductivity_FGA_fin)
    for j in range(len(a)):
        list_FF.append(a[j][1])
        list_Rayleigh.append(a[j][3])
        list_FI.append(a[j][10])
        list_thickness_FGA.append(a[j][8])
        list_thickness_AC.append(a[j][16])
        list_thickness_MG20.append(a[j][17])
        list_thickness_MG112.append(a[j][18])
    list_FF_summary.append(min(list_FF))
    if max(list_Rayleigh) > 4.0*(np.pi)**2.0:
        list_Rayleigh_summary.append(1)
    else:
        list_Rayleigh_summary.append(0)
    for j in range(conductivity_FGA_début,conductivity_FGA_fin):
        conductivity_FGA = conductivity_FGA + a[j][9]
    conductivity_FGA = conductivity_FGA/(conductivity_FGA_fin - conductivity_FGA_début)
    #print(list_temp_surf)
    #input()
    list_condu_avg_FGA.append(conductivity_FGA)
    list_FI_summary.append(list_FI[0])
    list_thickness_FGA_summary.append(list_thickness_FGA[0])
    list_thickness_AC_summary.append(list_thickness_AC[0])
    list_thickness_MG20_summary.append(list_thickness_MG20[0])
    list_thickness_MG112_summary.append(list_thickness_MG112[0])

"""print(list_FF_summary)
print(list_Rayleigh_summary)
print(list_FI_summary)
print(list_thickness_FGA_summary)"""

for i in range(number_of_files):
    list_FF_summary[i] = round(-1.0*list_FF_summary[i],2)
    list_FI_summary[i] = round(list_FI_summary[i],1)
    list_thickness_FGA_summary[i] = round(list_thickness_FGA_summary[i],2)
    list_thickness_AC_summary[i] = round(list_thickness_AC_summary[i],2)
    list_thickness_MG20_summary[i] = round(list_thickness_MG20_summary[i],2)
    list_thickness_MG112_summary[i] = round(list_thickness_MG112_summary[i],2)

list_FF_565 = [list_FF_summary[i] for i in range(0,10)]
list_FF_661 = [list_FF_summary[i] for i in range(10,20)]
list_FF_701 = [list_FF_summary[i] for i in range(20,30)]
list_FF_784 = [list_FF_summary[i] for i in range(30,40)]
list_FF_854 = [list_FF_summary[i] for i in range(40,50)]
list_FF_926 = [list_FF_summary[i] for i in range(50,60)]
list_FF_981 = [list_FF_summary[i] for i in range(60,70)]
list_FF_1076 = [list_FF_summary[i] for i in range(70,80)]
list_FF_1172 = [list_FF_summary[i] for i in range(80,90)]
list_FF_1222 = [list_FF_summary[i] for i in range(90,100)]
list_FF_1302 = [list_FF_summary[i] for i in range(100,110)]
list_FF_1316 = [list_FF_summary[i] for i in range(110,120)]
list_FF_1408 = [list_FF_summary[i] for i in range(120,130)]
list_FF_1476 = [list_FF_summary[i] for i in range(130,140)]
list_FF_1537 = [list_FF_summary[i] for i in range(140,150)]
list_FF_1616 = [list_FF_summary[i] for i in range(150,160)]
list_FF_1673 = [list_FF_summary[i] for i in range(160,170)]
list_FF_1737 = [list_FF_summary[i] for i in range(170,180)]
list_FF_1791 = [list_FF_summary[i] for i in range(180,190)]
list_FF_1847 = [list_FF_summary[i] for i in range(190,200)]
list_FF_1902 = [list_FF_summary[i] for i in range(200,210)]
list_FF_1958 = [list_FF_summary[i] for i in range(210,220)]
list_FF_2031 = [list_FF_summary[i] for i in range(220,230)]
list_FF_2247 = [list_FF_summary[i] for i in range(230,240)]

print(list_FF_565)
print(list_FF_661)

outputfile = open(path + 'Summary.dat', "w")
outputfile.write("Cas [--]" + "\t" + "Thickness BB [m]" + "\t" + "Thickness MG20 [m]" + "\t" + "Thickness GVC [m]" + "\t" + "Thickness MG112 [m]" + "\t" + "Freezing index [C*day]" + "\t" + "Frost depth [m]" + "\t" + "Convection 1 / No convection 0 [--]" + "\t" + "FGA conductivity while T_surf<0 [W/m/K]" + "\n")
for i in range(number_of_files):
    outputfile.write(str(i) + "\t" + str(list_thickness_AC_summary[i]) + "\t" + str(list_thickness_MG20_summary[i]) + "\t" + str(list_thickness_FGA_summary[i]) + "\t" + str(list_thickness_MG112_summary[i]) + "\t" + str(list_FI_summary[i]) + "\t" + str(list_FF_summary[i]) + "\t" + str(list_Rayleigh_summary[i]) + "\t" + str(list_condu_avg_FGA[i]) + "\n")
outputfile.close()


