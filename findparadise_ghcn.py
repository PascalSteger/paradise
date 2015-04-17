#!/usr/bin/env python3

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

def split(line):
    offset = 21
    values = []
    for k in range(31):
        values.append(int(line[offset:offset+5]))
        offset += 8
    values = np.array(values)
    return values, values.sum()

def find_TSUN_monthlymean():
    fname = './ghcn/ghcnd_all/'+'FMW00040505.dly'
    # does file exist?
    if not os.path.isfile(fname):
        print("File "+fname+" does not exist!")
        exit(1)
    # now we know that file exists

    # we open the file and read from it:
    monthly_median_tsun = [] # [h] <= measured in units of hours
    total_sunshine = 0 # [h]
    with open(fname , "r") as fi:
        for line in fi.readlines():
            #print(line[17:21])
            #continue

            if line[17:21] == 'TSUN':
                values, total = split(line) # [min]
                total_sunshine += total/60 # [h]

                median_tsun = np.median(values)/60
                #print(line[11:17]+" had a median sunshine duration of "+str(median_tsun)+" hours.")
                monthly_median_tsun.append(median_tsun)
    #print(monthly_median_tsun)
    median_tsun = np.median(monthly_median_tsun[-12:])
    print(fname+" has a "+str(pretty(median_tsun))+" hours of sunlight on a normal day in a normal month and a total of "+str(int(total_sunshine))+" hours in a year.")
    print(total_sunshine/median_tsun/365.25)

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


if __name__=="__main__":
    find_TSUN_monthlymean()
    #step2() # for finding the stations with agreeable temperature range
