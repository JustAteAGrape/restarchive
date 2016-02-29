import unittest
import os
from archiveManager import ArchiveManager


class ArchiveManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.testDir = '/pyTest/testDir'
        self.testDirMissing = '/pyTest/testDirMissing'
        self.testDataFile = '/testData.txt'
        self.testExistingFile = '/test.txt'
        self.testCompressedFile = '/compressed.gz'
        self.archiveManager = ArchiveManager()
        if not os.path.exists(self.testDir):
            os.makedirs(self.testDir)
        dataFile = open(self.testDir + self.testExistingFile, 'w+b')
        dataFile.write('test data')
        dataFile.close()


    def tearDown(self):
        if os.path.exists(self.testDir + self.testDataFile):
            os.remove(self.testDir + self.testDataFile)
        if os.path.exists(self.testDir + self.testExistingFile):
            os.remove(self.testDir + self.testExistingFile)
        if os.path.exists(self.testDir + self.testCompressedFile):
            os.remove(self.testDir + self.testCompressedFile)
        if os.path.exists(self.testDir):
            os.removedirs(self.testDir)
        if os.path.exists(self.testDirMissing):
            os.removedirs(self.testDirMissing)

    def test_createPathIfNotExist_pathExists(self):
        self.archiveManager.createPathIfNotExist(self.testDir)
        self.assertTrue(os.path.exists(self.testDir), 'Test Directory Not Found')

    def test_createPathIfNotExist_pathNotExist(self):
        self.archiveManager.createPathIfNotExist(self.testDirMissing)
        self.assertTrue(os.path.exists(self.testDirMissing), 'Test Directory Not Found')

    def test_createDataFile_pathExists(self):
        self.archiveManager.createDataFile(self.testDir, self.testDataFile, 'test')
        self.assertTrue(os.path.isfile(self.testDir + self.testDataFile), 'File Not Found')

    def test_createDataFile_pathNotExists(self):
        with self.assertRaises(IOError):
            self.archiveManager.createDataFile(self.testDirMissing, self.testDataFile, 'test')

    def test_compressDataFile_pathExists(self):
        self.archiveManager.compressDataFile(self.testDir, self.testExistingFile, self.testCompressedFile)
        self.assertTrue(os.path.isfile(self.testDir + self.testCompressedFile), 'Compressed File Not Found')

    def test_compressDataFile_pathNotExists(self):
        with self.assertRaises(IOError):
            self.archiveManager.compressDataFile(self.testDirMissing, self.testExistingFile, self.testCompressedFile)


if __name__ == '__main__':
    unittest.main()
