###
# ArcGIS Tile Script
# 
# MTRL lab - Technion institute of technology
# 
# Instructions
# This code runs in an ArcGIS notebook.
# Create two layout named `layouteEmptyArea` and `layoutFullTile` (15cm x 15cm)
# In each layout create a mapframe named `view`
# Choose the scale of the map
# Edit the parameters bellow
# 
# Copyright Anna Boim
# License MIT
###
import os

# Set up the area of the first tile
# [minX, minY, maxX, maxY]
bbox = [[191627.95,715130.73],[192327.95,715830.73]]
mapOffset = 30
iterationsX = 20
iterationsY = 20
savePath = r"C:\Users\mtrl\Desktop\test"


def createTile(bbox, mapOffset, iterationsX, iterationsY, savePath):
    proj = arcpy._mp.ArcGISProject("CURRENT")

    layouteEmptyArea = proj.listLayouts('layouteEmptyArea')[0]
    layoutFullTile = proj.listLayouts('layoutFullTile')[0]

    mframe1 = layouteEmptyArea.listElements('MAPFRAME_ELEMENT', 'view')[0]
    mframe2 = layoutFullTile.listElements('MAPFRAME_ELEMENT', 'view')[0]

    # create dataset directories
    pathA = savePath+r'\train_A'
    if not os.path.exists(pathA):
        os.makedirs(pathA)
    pathB = savePath+r'\train_B'
    if not os.path.exists(pathB):
        os.makedirs(pathB)

    nameNumerator = 1
    ### EXPORT LOOP BEGINS ###
    for x in range(0, iterationsX):
        for y in range(0, iterationsY):

            ex = arcpy.Extent(
                bbox[0][0] - x * 30, # X min
                bbox[0][1] + y * 30, # X max
                bbox[1][0] - x * 30, # Y min
                bbox[1][1] + y * 30 # Y max
                )

            mframe1.camera.setExtent(ex)
            mframe2.camera.setExtent(ex)

            name = '0'+str(nameNumerator)
        
            # setting the export names and paths
            layouteEmptyArea.exportToJPEG(pathA + '\\' + name, 100)
            layoutFullTile.exportToJPEG(pathB + '\\' + name, 100)

            nameNumerator = nameNumerator + 1
        
createTile(bbox, mapOffset, iterationsX, iterationsY, savePath)

