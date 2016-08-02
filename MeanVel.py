import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset

if __name__ == "__main__":

    __datapath__ = "ECCOv4/"
    __fileu__ = __datapath__+"EVELMASS.0001.nc"
    __filev__ = __datapath__+"NVELMASS.0001.nc"

    udata, vdata = Dataset(__fileu__), Dataset(__filev__)

    # grid
    z = udata['dep'][:]
    loni, lati = udata['lon'][:], udata['lat'][:]
    lon, lat = loni[0], lati[...,0]

    # get regional fields
    #lonmin,lonmax = -55, -35
    #latmin,latmax = -32, -20
    lonmin,lonmax = -65, 20
    latmin,latmax = -50, -5

    lonlim,latlim = [lonmin,lonmax], [latmin,latmax]
    flon = (lon>=lonmin)&(lon<=lonmax)
    flat = (lat>=latmin)&(lat<=latmax)

    um = udata['EVELMASS'][:][...,flat,:].mean(axis=0)
    vm = vdata['NVELMASS'][:][...,flat,:].mean(axis=0)
    um, vm = um[...,flon], vm[...,flon]
    lon, lat = lon[flon], lat[flat]
