class JSONListWriter:
    def __init__(self):
        pass

    def writePointCloudFile(self, fileName, outputPointCloud, listName):
        file = open(fileName, 'w')

        # write opening 2 lines
        file.write("let " + listName + " = [")

        # write points
        for idx, point in enumerate(outputPointCloud):
            file.write(point.getInJSONFormat())
            
            if idx == len(outputPointCloud):
                file.write('];')
            else:
                file.write(',\n')
        file.close()  