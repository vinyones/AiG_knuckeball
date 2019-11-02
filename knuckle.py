import math

def waktu_tertinggi(kecepatan, radius, gravitasi):
    tmaks = 0
    tmaks = kecepatan * math.sin(radius) / gravitasi
    return tmaks


def titik_tertinggi(kecepatan, radius, gravitasi):
    ymaks = 0
    ymaks = pow(kecepatan,2) * pow(math.sin(radius),2)/(2*gravitasi)
    return ymaks


def total_Height(height_awal, height_akhir):
    total_Height = height_awal + height_akhir
    return total_Height

def waktu_jatuh( total_height, grativasi):
    tAkhir = math.sqrt(2*total_height/grativasi)
    return tAkhir

def waktu_total(waktu_tertinggi, waktu_akhir):
    tTotal = waktu_tertinggi + waktu_akhir
    return tTotal

def longitude( kecepatan,  radius, waktu_total, height):
    longitude = kecepatan * waktu_total * math.cos(radius)
    return longitude


def result( waktu_total, height, longitude):
    print("\nWaktu yang dibutuhkan untuk mencapai Tanah : {} sekon\n".format(waktu_total))
    print("\nJarak Peluru :\n")
    print("Initial Longitude = 0 m\n")
    print("Initial Latitude = {}  m\n\n".format(height))
    print("Final Longitude = {} m\n".format(longitude))
    print("Final Latitude = 0 m")

g = 9.8
phi = 3.14
sudut = 0
rad = 0
wind = 0
direction = ""
v = 0
height = 0
totalHeight = 0

print("================\n")
print("KALKULASI PELURU\n")
print("================\n\n")
print("Masukkan kecepatan peluru (m/s) : ")
# v = float(input())
v = 130
# print("Masukkan ketinggian (m) : ")
# height = float(input())
height = 20
# print("Masukkan sudut tembak : ")
# sudut = float(input())
sudut = 15

if(sudut == 0):
    sudut = 1

rad = sudut*phi/180
while(wind >= v and ( direction != "Barat" or direction != "Timur" or direction != "Utara" or direction != "Selatan")):
    wind = (int(input("Masukan kecepatan angin [m/s] : ")))
    direction = input("Masukan arah angin [ Barat/Timur/Utara/Selatan ] : ")


if(direction == "Barat" or direction == "Timur"):
    v = math.sqrt(pow(v,2) + pow(wind,2))
elif(direction == "Utara"):
    v = v + wind
elif(direction == "Selatan"):
    v = v - wind

waktu_tertinggi(v,rad,g)
titik_tertinggi(v,rad,g)
total_Height(height,titik_tertinggi(v,rad,g))
waktu_jatuh(total_Height(height,titik_tertinggi(v,rad,g)),g)
waktu_total(waktu_tertinggi(v,rad,g),waktu_jatuh(total_Height(height,titik_tertinggi(v,rad,g)),g))
longitude(v,rad,waktu_total(waktu_tertinggi(v,rad,g),waktu_jatuh(total_Height(height,titik_tertinggi(v,rad,g)),g)),height)
result(waktu_total(waktu_tertinggi(v,rad,g),waktu_jatuh(total_Height(height,titik_tertinggi(v,rad,g)),g)),height,longitude(v,rad,waktu_total(waktu_tertinggi(v,rad,g),waktu_jatuh(total_Height(height,titik_tertinggi(v,rad,g)),g)),height))

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

tinggi = titik_tertinggi(v,rad,g)

X=np.array([[0,tinggi,tinggi+tinggi]])
Y=np.array([[0,tinggi,tinggi+tinggi]])
Z=np.array([[0,tinggi,0]])


ax.plot_wireframe(X,Y,Z)

plt.show()