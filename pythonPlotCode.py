#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 10:20:39 2021

@author: aaronipsa
"""

import matplotlib.pyplot as plt
import numpy as np


BUCKET_VOLUME = 4.2 #liters
SECONDS_PER_MINUTE = 60

## miliwatts generated for each of seven trials
power_readings =np.array([ [170,190,200,147,225],
                           [290,300,370,390,280],
                           [230,230,270,245,290],
                           [150,140,120,160,155],
                           [160,170,190,200,170],
                           [100, 95, 70 ,90,100],
                           [150,130,160,170,200] ])

power = np.average(power_readings,axis=1)

## time for water to fill bucket
seconds_to_fill = [17,9.5,13,15,19,24,20]

## convert liters per minute
water_flow = [BUCKET_VOLUME/x*SECONDS_PER_MINUTE for x in seconds_to_fill]

# clear current plot
plt.clf()

# 'r*' means red stars. 'ko' would give you black circles.
plt.scatter(water_flow, power, marker='o', color='r')

plt.xlabel('Water Flow (liters/minute)')
plt.ylabel('Power (miliwatts)')
plt.title('Power Generated from Waterwheel')
# plt.legend(['Ezra','Aaron'])


""" Plot Best Fit Line """
## Convert data to column vectors
X = np.array([water_flow]).T
Y = np.array([power]).T

## add a column of 'ones' to the independent variable
n,_ = X.shape
# X = np.hstack([X, np.ones([n,1])])

## solve the regression
B = np.linalg.inv(X.T@X)@(X.T@Y)
slope = float(B[0,0])
# intercept = float(B[1,0])
intercept = 0

## plot line
line_points = [x*slope+intercept for x in water_flow]
plt.plot(water_flow,line_points,linestyle='-', color='k')

##plot slope
# plt.text(20, 150, 'Slope:', horizontalalignment='left',
#      verticalalignment='center', transform=ax.transAxes)
plt.text(20,220, 'Slope: {:2.2f}'.format(slope))


"""
85 gallons per person per day
2550 gallons/month

166 kwatt-hours per person per month

results show 12 milliwatts/(litter/minute)
12 mw-min/liter *1h/60 min
0.2mw-hours/liter *3.8 liters/gallon
.76 mw-hours/gallon * 1 w/1000mw * 1kw/1000w
=.76/100000 kw-h/gallon * 2550 gal/month
= .001938 kw-hours


20 liters/min 1 gal/3.8  * 60 min/hour =  316 gallons/hour

200 lpm ~ 316 gallons/hour ~ 238 miliwatts
At that rate, a perons would use his/her monthly water in 8 hours
238*8 = 1904 mw-hours = .001904 kw-hours

for a 15 watt led bulb, that's about 0.001904*1000*60 116 watt-minutes, or
enough to pwer the bulb for 7.7 minutes/month



"""
