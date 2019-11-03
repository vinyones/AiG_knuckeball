from matplotlib import pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import axes3d

diameter_bola = 22
jari_bola = 11
berat_bola = 450
phi = 3.14
massa_jenis_udara = 1.2
kecepatan_bola = 130
gravitasi = 9.8
drag_coef = 0.2
magnus_coef = 1
sudut = 45
rotasi = 9

time = 2

luas_permukaan_bola = 4 * phi * (jari_bola ** 2)

percepatan_x = ((massa_jenis_udara * luas_permukaan_bola) / 2 * berat_bola) * ((drag_coef * kecepatan_bola * (kecepatan_bola * math.cos(sudut))) - (magnus_coef * jari_bola * rotasi * (kecepatan_bola * math.sin(sudut))))
percepatan_z = ((massa_jenis_udara * luas_permukaan_bola) / 2 * berat_bola) * ((drag_coef * kecepatan_bola * (kecepatan_bola * math.sin(sudut))) + (drag_coef * jari_bola * rotasi * (kecepatan_bola * math.cos(sudut))- gravitasi)) 

x_coor = []
z_coor = []
y_coor = []

x = 0
z = 0

for i in range(0, time + 1):
    kecepatan_x = kecepatan_bola + percepatan_x * time
    kecepatan_z = kecepatan_bola + percepatan_z * time

    x = (x + (kecepatan_bola * (time - i))) + (0.5 * percepatan_x * ((time - i) ** 2))
    x_coor.append(x)
    z = (z + (kecepatan_bola * (time - i))) + (0.5 * percepatan_z * ((time - i) ** 2))
    z_coor.append(z)

    y = (kecepatan_bola * (time- i)) - (gravitasi * ((time - i) ** 2))
    y_coor.append(y)


fig = plt.figure(figsize=(8,8))
ax = plt.axes(projection="3d")

ax.plot3D(x_coor, y_coor, z_coor)
plt.show()