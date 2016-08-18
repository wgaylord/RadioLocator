import livejson

data = None

def openData(file):
    global data
    data = livejson.ListFile(file)

def writeSignalData(location,powerLevel,freq):
    data.append([freq,powerLevel,location])

