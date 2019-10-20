import numpy as np

vel_max = 5.8
vel_min = -32.6   
perc = 50
delta = vel_max - vel_min

result = (delta*perc)/100

print('Max = [{}]\nMin = [{}]\nDelta = [{}]\nPorcentagem = [{}]\n-------------------\nResultado = [{}]'.format(vel_max,vel_min,delta,perc,result))

