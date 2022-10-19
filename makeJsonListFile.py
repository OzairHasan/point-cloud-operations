from pointcloudrw import PointCloudReader
from cloudpoint import CloudPoint
from jsonlistwriter import JSONListWriter



fileName = 'plafondbleu_50k'
fileExt = '.txt'
outputJSONFileName = 'plafondbleu_50k_js'
jsFileExt = '.js'
listName = 'data'

pcr = PointCloudReader()
pointCloud = []
pcr.readPointCloudFile(fileName + fileExt, pointCloud)

pcw = JSONListWriter()
pcw.writePointCloudFile(outputJSONFileName + jsFileExt , pointCloud, listName)