__depends__ = ["data/vel_time-averaged.npz","data/vel_snapshot_daily-averaged.npz"]
__dest__    = []

import numpy as np
import scipy as sp
from scipy import ndimage
import matplotlib.pyplot as plt
plt.rcParams['lines.linewidth'] = 2
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset
import seawater as sw


data = np.load(__depends__[0])
snap = np.load(__depends__[1])

lonlim = [data['lon'].min(),data['lon'].max()]
latlim = [data['lat'].min(),data['lat'].max()]

m = Basemap(projection='merc',llcrnrlat=latlim[0],urcrnrlat=latlim[1],\
            llcrnrlon=lonlim[0],urcrnrlon=lonlim[1],lat_ts=-25.,resolution='i')

loni,lati = np.meshgrid(data['lon'],data['lat'])
x,y = m(loni,lati)
dec = 5
iz = 20
fig = plt.figure(figsize = (20,6))
m.etopo()
m.quiver(x[::dec,::dec],y[::dec,::dec],data['u'][iz,::dec,::dec],data['v'][iz,::dec,::dec])
#plt.plot([x0,x1],[y0,y1],'r',linewidth=4,alpha=.5)
#plt.plot([x0_cf,x1_cf],[y0_cf,y1_cf],'r',linewidth=4,alpha=.5)
#plt.plot([x0_ub,x1_ub],[y0_ub,y1_ub],'r',linewidth=4,alpha=.5)
#plt.plot([x0_sa,x1_sa],[y0_sa,y1_sa],'r',linewidth=4,alpha=.5)

m.drawparallels(np.arange(latlim[0],latlim[1],1.5),labels=[1,0,0,0],fontsize=14,linewidth=0)
m.drawmeridians(np.arange(lonlim[0],lonlim[1],2.5),labels=[0,0,0,1],fontsize=14,linewidth=0)
m.fillcontinents(color='.5',lake_color=None)


