#!/usr/bin/python3

#import packages
import numpy as np
import shapefile as shp
from geojson import Polygon, MultiPolygon, Feature, FeatureCollection
import geojson



#######################################################################
"""                                                                  ##
A feature in GeoJSON looks like this:                                ##
                                                                     ##
{                                                                    ##
    "type": "Feature",                                               ##
    "properties": {                                                  ##
        "name": "Alabama",                                           ##
        "density": 94.65                                             ##
    },                                                               ##
    "geometry": ...                                                  ##
    ...                                                              ##
}                                                                    ##
                                                                     ##
Put them together, one after the other, and you have a GeoJSON file  ##
"""                                                                  ##
#######################################################################








class Shp2GeoJson():
    '''
    docstring
    '''

    def __init__(self):
        self.shapefilepath = ""
        self.shapefile = None
        self.properties = []
        self.selectedproperties = []
        self.coordprecision = 5
        self.features = []


    def import_shp_file(self, filename):
        self.shapefile = shp.Reader(filename)
        return self.shapefile
    

    def set_coord_precision(self, numdecimals):
        self.coordprecision = numdecimals


    def _convert(self):
        features = []
        for record, shape in zip(self.shapefile.records(), self.shapefile.shapeRecords()):
            if len(shape.shape.parts) == 1: #make a polygon
                properties = {}
                for selection in self.selectedproperties:
                    properties[selection] = str(record[self.properties.index(selection)])
                polygon = Polygon([[tuple([round(i[0], self.coordprecision),
                                           round(i[1], self.coordprecision)]) for i in shape.shape.points]])
                feature = Feature(geometry=polygon, properties=properties)

            elif len(shape.shape.parts) > 1: #make a multipart polygon
                properties = {}
                for selection in self.selectedproperties:
                    properties[selection] = str(record[self.properties.index(selection)])
                indices = list(shape.shape.parts)
                coords = [[tuple([round(i[0], self.coordprecision),
                                  round(i[1], self.coordprecision)]) for i in shape.shape.points]]
                parts = []
                for i, index in enumerate(indices):
                    try:
                        parts.append(coords[index:indices[i+1]])
                    except:
                        parts.append(coords[index:])
                parts = [(i) for i in parts]
                multipolygon = MultiPolygon(parts)
                feature = Feature(geometry=multipolygon, properties=properties)

            else:
                print("no record made for ", record)
                feature = None

            if feature:
                features.append(feature)
        collection = FeatureCollection(features)
    
    def get_properties(self, shapefile):
        self.properties = [i[0] for i in shapefile.fields]
        return self.properties
    

    
    def set_properties(self, properties):
        self.selectedproperties = properties

    
    def save(self, filename):
        pass





if __name__ == "__main__":

    shpf = "/home/wes/Personal/website/interactMap/maps/CA-FED-WebMercator.shp"
    converter = Shp2GeoJson()
    shpfile = converter.import_shp_file(shpf)
    properties = converter.get_properties(shpfile)
    converter._convert()
