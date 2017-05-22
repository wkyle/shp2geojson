# shp2geojson
Python script for converting ESRI shapefiles to geojson for the web

## Introduction

A feature in GeoJSON looks like this:


`{
    "type": "Feature",
    "properties": {
        "name": "Alberta",
        "density": 94.65
    },
    "geometry": ...
    ...
}`


Put them together, one after the other, and you have a GeoJSON file