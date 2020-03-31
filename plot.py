import folium

import os
import json
import requests
import glob
import random


"""

{
  "axes": [
    {
      "scale": "x",
      "title": "Time",
      "type": "x"
    },
    {
      "scale": "y",
      "title": "Dominant Wave Period (s)",
      "type": "y"
    }
  ],
  "data": [
    {
      "name": "table",
      "values": [
        {
          "col": "dominant_wave_period (s)",
          "idx": 1366257000000,
          "val": 8.0
        },
        {
          "col": "dominant_wave_period (s)",
          "idx": 1366260600000,
          "val": 6.0
        },
        {
          "col": "dominant_wave_period (s)",
          "idx": 1366264200000,
          "val": 7.0
        },
        {
          "col": "dominant_wave_period (s)",
          "idx": 1366267800000,
          "val": 6.0
        },
        {
          "col": "dominant_wave_period (s)",
          "idx": 1368877800000,
          "val": 8.0
        },
        {
          "col": "dominant_wave_period (s)",
          "idx": 1368881400000,
          "val": 9.0
        }
      ]
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
      "nice": true,
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
"""



def get_lat():
    return random.uniform(59.292880, 59.362499)

def get_lon():
    return random.uniform(17.965891, 18.165572)


# %%
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
                #print(line)
            #print(line_data)
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

# %%


url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
vis1 = json.loads(requests.get(f'{url}/vis1.json').text)
st = requests.get(f'{url}/vis1.json').text
#print(st)
#print(type(st))
#print(vis1)

#vis2 = json.loads(requests.get(f'{url}/vis2.json').text)
#vis3 = json.loads(requests.get(f'{url}/vis3.json').text)







m = folium.Map(
    location=[59.3242, 18.0659],    # Stockholm
    zoom_start=12,
    #tiles='Stamen Terrain'
)

# folium.Marker(
#     # location=[59.332486, 18.037671],
#     location=[get_lat(), get_lon()],
#     popup=folium.Popup(max_width=450).add_child(
#         folium.Vega(vis1, width=450, height=250))
# ).add_to(m)


for data in marker_data:
    folium.Marker(
        location=[get_lat(), get_lon()],
        popup=folium.Popup(max_width=450).add_child(
            folium.Vega(data, width=450, height=250))
    ).add_to(m)

m
#m.save('map.html')
