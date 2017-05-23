# shp2geojson
Python script for converting ESRI shapefiles to geojson for the web

## Introduction

A FeatureCollection in GeoJSON looks like this:


```
{ "type": "FeatureCollection",
    "features": [
      { "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [102.0, 0.5]},
          "properties": {
            "prop0": "value0"
          }
        },
      { "type": "Feature",
        "geometry": {
          "type": "LineString",
          "coordinates": [
            [102.0, 0.0], [103.0, 1.0], [104.0, 0.0], [105.0, 1.0]
            ]
          },
        "properties": {
          "prop0": "value0",
          "prop1": 0.0
          }
        },
      { "type": "Feature",
         "geometry": {
           "type": "Polygon",
           "coordinates": [
             [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0],
               [100.0, 1.0], [100.0, 0.0] ]
             ]
         },
         "properties": {
           "prop0": "value0",
           "prop1": {"this": "that"}
           }
         }
       ]
     }
```


It's made up of features which can be polygons, lines, points, multipart polygons, etc.

## Converting
Popular interactive mapping tools for the web seem to prefer geojson files (.json, .geojson) for their maps but the Canadian government only supplies ESRI shapefiles (.shp) of Federal Electoral Districts and other products.

Using the python3 module `pyshp` we can read shapefiles and adjust the syntax to build a geojson file using the python3 module `geojson`.

## Some Options
* Read shapefiles, see the feature fields (properties) and select which properties to include in the final geojson
* Select the numerical precision with which to output the geojson to optimize file size
* Optionally split multipart polygons into separate polygons

## Current Hangups
It's possible that multipart polygons contain holes. How to determine if this is the case and what to do with it is something to be figured out.