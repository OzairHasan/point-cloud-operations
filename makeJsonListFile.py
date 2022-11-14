from pointcloudrw import PointCloudReader
from cloudpoint import CloudPoint
from jsonlistwriter import JSONListWriter



fileName = 'livingroom_50k'
fileExt = '.txt'
outputJSONFileName = fileName + '_js'
jsFileExt = '.js'
listName = 'data'

pcr = PointCloudReader()
pointCloud = []
pcr.readPointCloudFile(fileName + fileExt, pointCloud)

pcw = JSONListWriter()
pcw.writePointCloudFile(outputJSONFileName + jsFileExt , pointCloud, listName)