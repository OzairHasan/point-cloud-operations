from pointcloudrw import PointCloudReader, PointCloudWriter
from cloudpoint import CloudPoint

def getReducedColours(R, G, B):
    if R > G and R > B:
        return [R, 0, 0]
    elif G > R and G > B:
        return [0, G, 0]
    elif B > G and B > R:
        return [0, 0, B]
    else:
        return [R, G, B]

fileName = 'plafondbleu_50k'
fileExt = '.txt'
pcr = PointCloudReader()
pointCloud = []
pcr.readPointCloudFile(fileName + fileExt, pointCloud)
for point in pointCloud:
    [newR, newG, newB] = getReducedColours(point.R, point.G, point.B)
    point.R = newR
    point.G = newG
    point.B = newB
pcw = PointCloudWriter()
pcw.writePointCloudFile(fileName + '_contrast' + fileExt, pointCloud)