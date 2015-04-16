#!/usr/bin/env ipython3

##
# @file
# find min, max temp
# run via
# python findparadise.py > minmedmax.dat

# (c) GPL v3 2015 ETHZ Pascal S.P. Steger pascal@steger.aero

import pdb
import numpy as np
import os

def pretty(scal, dig=2):
    return "%.*f" % (dig-1, scal)

def step1():
    stations = np.loadtxt('ish-history.txt', skiprows=19, usecols=(0,1), dtype=str)
    for station1, station2 in stations:
        station1 = station1[2:-1]
        station2 = station2[2:-1]

        allT = np.array([])
        for yint in range(1929, 2010):
            year = str(yint)
            fname = 'gsod/'+year+'/'+station1+'-'+station2+'-'+year+'.op'

            #P = np.loadtxt(fname, skiprows=1)
            if not os.path.isfile(fname):
                continue
            T = np.genfromtxt(fname, skiprows = 1, unpack = True, usecols=(3), dtype="d17")
            allT = np.hstack([allT, T])

        if len(allT) > 0:
            Tmax = (max(allT)-32)*5/9
            Tmin = (min(allT)-32)*5/9
            Tmedian = (np.median(allT)-32)*5/9

            print(station1, station2, pretty(Tmin), pretty(Tmax), pretty(Tmedian))

def step2():
    dat = 'minmaxmed.dat'
    id1,id2,Tmin,Tmax,Tmed = np.loadtxt(dat,usecols=(0,1,2,3,4), unpack=True, dtype=str)

    Tminn = np.zeros(len(id1), dtype=float)
    Tmaxn = np.zeros(len(id1), dtype=float)
    Tmedn = np.zeros(len(id1), dtype=float)
    for k in range(0,len(id1)):
        id1[k] = id1[k][2:-1]
        id2[k] = id2[k][2:-1]
        Tminn[k] = float(Tmin[k][2:-1])
        Tmaxn[k] = float(Tmax[k][2:-1])
        Tmedn[k] = float(Tmed[k][2:-1])

    sel1 = (Tminn > 10.)
    sel2 = (Tmaxn < 30.)
    sel3 = (Tmedn > 18.)

    sel = sel1 * sel2 * sel3



    id1 = id1[sel]
    id2 = id2[sel]
    for k in range(len(id1)):
        print(id1[k], id2[k])

    with open("ish-history.txt" , "r") as fi:
        for line in fi.readlines():
            for k in range(len(id1)):
                if line[0:12] == id1[k]+' '+id2[k]:
                    print(line[:-1])

    print(sum(sel), 'stations fulfill our criteria')



# step1() # for finding the min, max, median temperature over all history
step2() # for finding the stations with agreeable temperature range
