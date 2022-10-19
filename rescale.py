from pointcloudrw import PointCloudReader, PointCloudWriter
from cloudpoint import CloudPoint



fileName = 'plafondbleu'
fileExt = '.txt'
outputPointCloudDict = {}
pcr = PointCloudReader()
pointCloud = []
pcr.readPointCloudFile(fileName + fileExt, pointCloud)
for point in pointCloud:
    lowres_x = round(point.x, 2)
    lowres_y = round(point.y, 2)
    key = (lowres_x, lowres_y)
    if key in outputPointCloudDict:
        if point.z < outputPointCloudDict[key].z:
            continue
    outputPointCloudDict[key] = point
pcw = PointCloudWriter()
pcw.writePointCloudFileFromDict(fileName + '_new' + fileExt, outputPointCloudDict)