import os
import unittest

from mock import patch

import AWeber


class AWeberTestCase(unittest.TestCase):
    def cleanUpTestDir(self):
        if os.path.exists('/data/archive/0/archiveData.gz'):
            os.remove('/data/archive/0/archiveData.gz')
        if os.path.exists('/data/archive/0'):
            os.removedirs('/data/archive/0')

    def setUp(self):
        self.app = AWeber.app.test_client()
        self.cleanUpTestDir()

    def tearDown(self):
        self.cleanUpTestDir()

    def test_home_get(self):
        rsp = self.app.get('/')
        assert 'USAGE: Issue a POST with JSON data to /{postID}/archive' in rsp.data

    def test_archive_get(self):
        rsp = self.app.get('/0/archive')
        assert 'GET not yet supported' in rsp.data

    def test_archive_post(self):
        rsp = self.app.post('0/archive', data = '{"data": "test"}')
        assert 'SUCCESS' in rsp.data
        self.assertTrue(os.path.exists('/data/archive/0/archiveData.gz'))

    def test_archive_post_fail(self):
        #archiveManager = ArchiveManager()
        #archiveManager.createDataFile = Mock(side_effect=IOError)
        with patch('archiveManager.ArchiveManager') as mock:
            instance = mock.return_value
            instance.createDataFile.return_value = IOError
            rsp = self.app.post('0/archive', data = '{"data": "test"}')
            assert 'Failed to archive data' in rsp.data
            self.assertFalse(os.path.exists('/data/archive/0/archiveData.gz'))

if __name__ == '__main__':
    unittest.main()
