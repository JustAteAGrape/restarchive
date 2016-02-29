import os
import gzip
import shutil

class ArchiveManager():
    archiveRoot = '/data/archive/'

    def __init__(self):
        #TODO: load archive root from configuration source such as file, registry or environment variable
        pass

    def createPathIfNotExist(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def createDataFile(self, dataPath, fileName, data):
        try:
            dataFile = open(dataPath + fileName, 'w+b')
            dataFile.write(data)
            dataFile.close()
        except:
            print 'Failed to create data file for archive'
            raise

    def compressDataFile(self, dataPath, rawFileName, outputFileName):
        try:
            rawFile = open(dataPath + rawFileName, 'r+b')
            gzipFile = gzip.open(dataPath + outputFileName, 'w+b')
            shutil.copyfileobj(rawFile, gzipFile)
        except:
            print 'Failed to compress data file'
            raise
        rawFile.close()
        gzipFile.close()
        os.remove(dataPath + rawFileName)

    def archiveData(self, archiveId, data):
        dataPath= self.archiveRoot + archiveId
        self.createPathIfNotExist(dataPath)
        try:
            self.createDataFile(dataPath, '/archiveData.json', data)
            self.compressDataFile(dataPath, '/archiveData.json', '/archiveData.gz')
        except:
            return False
        return True


