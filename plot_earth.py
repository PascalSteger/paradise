#!/usr/bin/python2

import matplotlib.pyplot as plt
import pdb
import numpy as np
import pandas as pd

import mpl_toolkits
from mpl_toolkits.basemap import Basemap, cm
import matplotlib.pyplot as plt
import numpy as np

#fig = plt.figure(facecolor='black')
#fig.subplots_adjust(wspace=.005,left=.001,bottom=.001)
#ax = fig.add_subplot(1,1,1,axisbg='b')
#ax.cla()

# set up orthographic map projection with
# perspective of satellite looking down at 50N, 100W.
# use low resolution coastlines.
# don't plot features that are smaller than 1000 square km.
# projection = 'ortho' gives round earth
# moll, hammer, robin (best)
map = Basemap(projection='robin', lat_0 = 45, lon_0 = 7, resolution = 'c')
#NZ:
#map = Basemap(projection='cass', lat_0 = -42, lon_0 = 174, resolution = 'i', width=1591185,height=3115557)
#map = Basemap(projection='cass', lat_0 = 10, lon_0 = -83, resolution = 'i', width=2091185,height=1315557)

# use data from
#http://gcmd.gsfc.nasa.gov/KeywordSearch/Metadata.do?Portal=GCMD&KeywordPath=|[Freetext%3D%27sunshine+hours%27]|Refine+By+Locations|GEOGRAPHIC+REGION|GLOBAL&OrigMetadataNode=GCMD&EntryId=CRAMERLEEMANS&MetadataView=Full&MetadataType=0&lbnode=mdlb2

# http://daac.ornl.gov/cgi-bin/dsviewer.pl?ds_id=416

def read_tmean():
    tmean = [pd.read_table(open('data/tmean/tmean_1.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/tmean/tmean_2.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/tmean/tmean_3.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/tmean/tmean_4.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/tmean/tmean_5.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/tmean/tmean_6.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/tmean/tmean_7.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/tmean/tmean_8.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/tmean/tmean_9.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/tmean/tmean_10.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/tmean/tmean_11.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/tmean/tmean_12.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999)
        ]
    return tmean

def read_sunshine():
    sunshine = [pd.read_table(open('data/cloud/cloud_1.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/cloud/cloud_2.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/cloud/cloud_3.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/cloud/cloud_4.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/cloud/cloud_5.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/cloud/cloud_6.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/cloud/cloud_7.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/cloud/cloud_8.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/cloud/cloud_9.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/cloud/cloud_10.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/cloud/cloud_11.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999),
            pd.read_table(open('data/cloud/cloud_12.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999)
        ]
    return sunshine

def read_precip():
    precip = [(pd.read_table(open('data/precip/precip_1.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999)),
            (pd.read_table(open('data/precip/precip_2.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999)),
            (pd.read_table(open('data/precip/precip_3.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999)),
            (pd.read_table(open('data/precip/precip_4.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999)),
            (pd.read_table(open('data/precip/precip_5.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999)),
            (pd.read_table(open('data/precip/precip_6.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999)),
            (pd.read_table(open('data/precip/precip_7.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999)),
            (pd.read_table(open('data/precip/precip_8.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999)),
            (pd.read_table(open('data/precip/precip_9.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999)),
            (pd.read_table(open('data/precip/precip_10.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999)),
            (pd.read_table(open('data/precip/precip_11.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999)),
            (pd.read_table(open('data/precip/precip_12.dat','rb'), skiprows=6, header=None, sep=' ', na_values=-9999))
        ]
    return precip


tmean    = read_tmean()
sunshine = read_sunshine()
precip   = read_precip()

lat = np.arange(-180, 180.5, 0.5)
lon = np.arange(89.5, -90.5, -0.5)
lon, lat = np.meshgrid(lon, lat)

tmin = -100
tmax = 100
tclefs = np.arange(tmin, tmax+1)
tsel = tmean[0] > -100
tottemp = tmean[0].multiply(0.)
for y in tmean:
    tminsel = y.loc[:] >= tmin
    tmaxsel = y.loc[:] <= tmax
    tsel = tsel & (tminsel & tmaxsel)
    tottemp += y
tannmean = (tottemp.divide(12.))
toptimum = tannmean.where(tsel, np.nan)

smin = 0.
smax = 100.
sclefs = np.arange(smin, smax+1, smax/50)
ssel = sunshine[0]>0
stot = sunshine[0].multiply(0.)
for y in sunshine:
    sminsel = y.loc[:] >= smin
    ssel = ssel & sminsel
    stot += y
sannmean = (stot.divide(12.))
soptimum = sannmean.where(ssel, np.nan)

pmin = -1.0
pmax = 12.0
pclefs = np.arange(pmin, pmax+1, pmax/100)
psel = precip[0]>-1.
ptot = precip[0].multiply(0.)
for y in precip:
    pminsel = y.loc[:] >= pmin
    pmaxsel = y.loc[:] <= pmax
    psel = psel & pminsel & pmaxsel
    ptot += y
pannmean = (ptot.divide(12.))
poptimum = pannmean.where(psel, np.nan)

def tgauss(x):
    best = 15.
    sdev = 10.
    return 1.* np.exp(-(x-best)**2/(2.*sdev**2))

def sgauss(x):
    best = 80.
    sdev = 15.
    return 1.* np.exp(-(x-best)**2/(2.*sdev**2))

def pgauss(x):
    best = np.exp(4.)
    sdev = 40.
    return 1.* np.exp(-(x-best)**2/(2.*sdev**2))

sel = psel**0 # tsel # & ssel & psel
toptimum = tannmean.where(sel, np.nan)
tpleasant = toptimum.applymap(tgauss) #.subtract(tmin).divide(tmax-tmin)
soptimum = sannmean.where(sel, np.nan)
spleasant = soptimum.applymap(sgauss) #.subtract(smin).divide(smax-smin)
poptimum = pannmean.where(sel, np.nan)
ppleasant = poptimum.applymap(pgauss) #subtract(pmin).divide(pmax-pmin)
#pleasant = 100*(sel>0)
#pleasant = 100.*min(tpleasant,ppleasant) #(sel>0) #(tpleasant+spleasant+ppleasant)/3.

tp_comp = tpleasant.lt(ppleasant)
tppleasant = (tpleasant.mul(tp_comp)).add(ppleasant.mul(1-tp_comp))

tps_comp = tppleasant.lt(spleasant)
tpspleasant = (tppleasant.mul(tps_comp)).add(spleasant.mul(1-tps_comp))

pleasant = tpspleasant

def plot_earth():
    # draw coastlines, country boundaries, fill continents.
    map.drawcoastlines(linewidth=0.5, color='gray')
    map.drawcountries(linewidth=0.5, color='#aaaaaa')
    #map.fillcontinents() #color = 'coral')
    # or instead, use imagery from NASA
    #map.bluemarble()

    # draw the edge of the map projection region (the projection limb)
    map.drawmapboundary()
    # draw lat/lon grid lines every 30 degrees.
    #map.drawmeridians(np.arange(0, 360, 15))
    #map.drawparallels(np.arange(-90, 90, 15))
    return

def plot_month(mon):
    return map.contourf(lat, lon, year[mon-1].T, tclefs, latlon=True, cm=plt.cm.jet)

def plot_nice_temp():
    map.contour(lat,lon, toptimum.T, tclefs, latlon=True, cm=plt.cm.jet, lw=1.0)
    return map.contourf(lat,lon, toptimum.T, tclefs, latlon=True, cm=plt.cm.jet)
def plot_nice_sun():
    map.contour(lat,lon, soptimum.T, sclefs, latlon=True, cm=plt.cm.jet, lw=1.0)
    return map.contourf(lat,lon, soptimum.T, sclefs, latlon=True, cm=plt.cm.jet)
def plot_nice_precip():
    map.contour(lat,lon, poptimum.T, pclefs, latlon=True, cm=plt.cm.jet, lw=1.0)
    return map.contourf(lat,lon, poptimum.T, pclefs, latlon=True, cm=plt.cm.jet)
def plot_pleasantness():
    map.contour(lat,lon, pleasant.T, 50, latlon=True, cm=plt.cm.jet, lw=1.0)
    return map.contourf(lat,lon, pleasant.T, 70, latlon=True, cm=plt.cm.jet)

plot_earth()
#cont = plot_nice_temp()
#cont = plot_nice_sun()
#cont = plot_nice_precip()
cont = plot_pleasantness()

cbar = map.colorbar(cont, location='bottom', pad="5%")
#cbar.set_label('mm')
#plt.title('Mean Monthly Precipitation')

#cbar.set_label('Mean Pleasantness, in Percent')
#plt.title('Combined Mean Pleasantness from Sunshine, Temperature, and Precipitation')
plt.show()
