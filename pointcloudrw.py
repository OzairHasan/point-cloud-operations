from cloudpoint import CloudPoint

class PointCloudReader:
    def __init__(self):
        pass

    def readPointCloudFile(self, fileName, outputPointCloud):
        file = open(fileName, 'r')

        # discard opening 2 lines of pointcloud file
        file.readline()
        numPoints = int(file.readline())

        # read points into output list
        for i in range(numPoints):
            [x, y, z, R, G, B] = file.readline().split(' ')[:6]
            point = CloudPoint(float(x), float(y),
                                float(z), int(R),
                                int(G), int(B))
            outputPointCloud.append(point)
        file.close()

        
class PointCloudWriter:
    def __init__(self):
        pass

    def writePointCloudFileFromDict(self, fileName, outputPointCloudDict):
        file = open(fileName, 'w')

        # write opening 2 lines
        file.write("//X Y Z R G B\n")
        file.write(str(len(outputPointCloudDict)) + '\n')

        # write points
        for key in outputPointCloudDict.keys():
            file.write(outputPointCloudDict[key].getLowResInFileFormat(key[0], key[1]))
        file.close()

    def writePointCloudFile(self, fileName, outputPointCloud):
        file = open(fileName, 'w')

        # write opening 2 lines
        file.write("//X Y Z R G B\n")
        file.write(str(len(outputPointCloud)) + '\n')

        # write points
        for point in outputPointCloud:
            file.write(point.getInFileFormat())
        file.close()