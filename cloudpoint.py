class CloudPoint:
    def __init__(self, x, y, z, R, G, B):
        self.x = x
        self.y = y
        self.z = z
        self.R = R
        self.G = G
        self.B = B

    def getInFileFormat(self):
        return (str(self.x) + ' ' + str(self.y) + ' ' +
                str(self.z) + ' ' + str(self.R) + ' ' +
                str(self.G) + ' ' + str(self.B) + '\n')

    def getLowResInFileFormat(self, lowres_x, lowres_y):
        return (str(lowres_x) + ' ' + str(lowres_y) + ' ' +
                str(self.z) + ' ' + str(self.R) + ' ' +
                str(self.G) + ' ' + str(self.B) + '\n')

    def getInJSONFormat(self):
        return ('{' + '"x":' + str(self.x) + ', "y":' +
        str(self.y) + ', "z":' + str(self.z) + ', "r":' +
        str(self.R) + ', "g":' + str(self.G) + ', "b":' + 
        str(self.B) + '}')