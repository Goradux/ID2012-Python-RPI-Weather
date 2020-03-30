import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.txt')

print(df.head())
print()
print(df)
print()
#print(df['longitude'])
#print()

lon = list(df['longitude'])
lat = list(df['latitude'])

BBox = (min(lon), max(lon),
        min(lat), max(lat))

print(BBox)

ruh_m = plt.imread('./map.png')

fig, ax = plt.subplots(figsize = (8,7))
#fig, ax = plt.subplots()
ax.scatter(lon, lat, zorder=1, alpha= 0.2, c='b', s=10)
ax.set_title('Plotting Spatial Data on Riyadh Map')
# ax.set_xlim(BBox[0],BBox[1])
# ax.set_ylim(BBox[2],BBox[3])

ax.set_xlim(46.5691, 46.8398)
ax.set_ylim(24.6128, 24.8256)

ax.imshow(ruh_m, zorder=0, extent = BBox, aspect= 'equal')
#ax.imshow(ruh_m, interpolation='nearest', extent = BBox, aspect= 'auto')