#!/usr/bin/python
# -*- coding: utf-8 -*-

from geopy.distance import geodesic
from datetime import datetime, timezone
import json
import urllib.request
import requests
import re


class piawarepython:

    def __init__(self):
        self.urlbase="https://www.flightaware.com/live/"
        self.adsbip="192.168.1.8"
        self.adsbdataurl="http://"+adsbip+":8080/data/aircraft.json"
        self.myloc = (13.05863, 80.19345)
        self.flightcoord = (0, 0)
        self.order = False

    def adsbdata(self):
        self.aircraftslist = []
        self.trackerdata = requests.get(self.adsbdataurl)
        self.trackerdata = trackerdata.json()
        self.recdata = self.trackerdata
        self.datalen = len(self.recdata['aircraft'])
        for i in range(0, datalen):
            if 'lat' not in self.recdata['aircraft'][i]:
                continue
            else:
                self.flightcoord = (self.recdata['aircraft'][i]['lat'],
                                    recdata['aircraft'][i]['lon'])
                self.recdata['aircraft'][i]['distance'] = \
                    geodesic(myloc, flightcoord).nm
        self.dwb = self.recdata
        self.dwblen = len(self.dwb['aircraft'])
        for i in range(0, self.dwblen):
            if 'squawk' not in self.dwb['aircraft'][i] or 'flight' \
                not in self.dwb['aircraft'][i]:
                continue
            else:
                self.aircraftslist.append(self.dwb['aircraft'][i])
        return self.aircraftslist

    def refresh(self):
        self.refadsbdata = self.adsbdata()
        return self.refadsbdata

    def adsbdatasort(
        self,
        datalist,
        sortby,
        sortorder,
        ):
        self.unsortedlist = datalist
        if sortorder == 'asc':
            self.order = False
        elif sortorder == 'dec':
            self.order = True
        convert = lambda text: (int(text) if text.isdigit() else text)
        alphanum_key = lambda key: [convert(c) for c in
                                    re.split('([0-9]+)',
                                    key.get('flight', 0))]
        if sortby == 'flight':
            self.sortedlist = sorted(self.unsortedlist,
                    key=alphanum_key, reverse=order)
        else:
            self.sortedlist = sorted(self.unsortedlist, key=lambda k: \
                    k.get(sortby, 0), reverse=order)
        return self.sortedlist

    def adsbdatafilter(
        self,
        datalist,
        filterby,
        filtermin,
        filtermax,
        ):
        self.filteredlist = []
        self.filteredflightlist = []
        self.unfilteredlist = datalist
        self.unfilteredlistlen = len(self.unfilteredlist)
        for i in range(0, self.unfilteredlistlen):
            if self.unfilteredlist[i][filterby] > filtermin \
                and self.unfilteredlist[i][filterby] < filtermax:
                self.filteredlist.append(self.unfilteredlist[i])
                if 'flight' in unfilteredlist[i]:
                    self.filteredflightlist.append(self.unfilteredlist[i]['flight'
                            ])
                else:
                    self.filteredflightlist.append(self.unfilteredlist[i]['hex'
                            ])
        return (self.filteredlist, self.filteredflightlist)
