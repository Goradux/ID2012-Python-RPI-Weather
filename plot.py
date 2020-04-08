import folium

import os
import json
import requests
import glob
import random


def get_lat():
    return random.uniform(59.292880, 59.362499)

def get_lon():
    return random.uniform(17.965891, 18.165572)


marker_data = []


def get_data():
    for text_log in glob.glob('data/*.txt'):
        with open(text_log) as log:
            line_data = []
            lines = log.readlines()
            first = True
            for line in lines:
                if first:
                    first = False
                    continue
                parsed = line.split(',')
                line_data.append((parsed[0], parsed[1]))
                print(line)
            print(line_data)
            data = {
                "axes": [
                    {
                    "scale": "x",
                    "title": "Time",
                    "type": "x"
                    },
                    {
                    "scale": "y",
                    "title": "Temperature (C)",
                    "type": "y"
                    }
                ],
                
                "data": [
                    {
                    "name": "table",
                    "values": [
                        {
                            "col": "Temperature (C)",
                            "idx": line[0], # time
                            "val": line[1]  # value
                        } for line in line_data]
                    }
                ],
                "height": 200,
                "legends": [],
                "marks": [
                    {
                    "from": {
                        "data": "table",
                        "transform": [
                        {
                            "keys": [
                            "data.col"
                            ],
                            "type": "facet"
                        }
                        ]
                    },
                    "marks": [
                        {
                        "properties": {
                            "enter": {
                            "stroke": {
                                "field": "data.col",
                                "scale": "color"
                            },
                            "strokeWidth": {
                                "value": 2
                            },
                            "x": {
                                "field": "data.idx",
                                "scale": "x"
                            },
                            "y": {
                                "field": "data.val",
                                "scale": "y"
                            }
                            }
                        },
                        "type": "line"
                        }
                    ],
                    "type": "group"
                    }
                ],
                "padding": "auto",
                "scales": [
                    {
                    "domain": {
                        "data": "table",
                        "field": "data.idx"
                    },
                    "name": "x",
                    "range": "width",
                    "type": "time"
                    },
                    {
                    "domain": {
                        "data": "table",
                        "field": "data.val"
                    },
                    "name": "y",
                    "nice": True,
                    "range": "height"
                    },
                    {
                    "domain": {
                        "data": "table",
                        "field": "data.col"
                    },
                    "name": "color",
                    "range": "category20",
                    "type": "ordinal"
                    }
                ],
                "width": 400
            }
            #print(data)
            marker_data.append(json.dumps(data))
        #print('done')


get_data()


m = folium.Map(
    location=[59.3242, 18.0659],    # Stockholm
    zoom_start=12
)


for data in marker_data:
    folium.Marker(
        location=[get_lat(), get_lon()],
        popup=folium.Popup(max_width=450).add_child(
            folium.Vega(data, width=450, height=250))
    ).add_to(m)


#m
m.save('map.html')
