from cli import ComposerCliFactory
from client import ComposerClientFactory
import unittest


class TestComposerClient(unittest.TestCase):

    def test_composer_client_install_ok(self):
        composer_client = ComposerClientFactory.create_mocked("","")
        ret = composer_client.install()

        self.assertTrue(ret, "dovrebbe esser true")        

    def test_composer_client_archive_ok(self):
        composer_client = ComposerClientFactory.create_mocked("","")
        ret = composer_client.archive()

        self.assertTrue(ret, "dovrebbe esser true")

    def test_composer_client_install_error(self):
        composer_client = ComposerClientFactory.create_mocked("ERROR","")
        ret = composer_client.install()

        self.assertTrue(ret, "dovrebbe esser true")
# ----------------------------------

    def test_composer_cli_install_ok(self):
        composer_cli = ComposerCliFactory.create_mocked()
        ret = composer_cli.install("")

        self.assertTrue(ret, "dovrebbe esser true") 

    def test_composer_cli_archive_ok(self):
        composer_cli = ComposerCliFactory.create_mocked()
        ret = composer_cli.archive("")

        self.assertTrue(ret, "dovrebbe esser true") 

class TestComposerCli(unittest.TestCase):
    def test_composer_cli_install_ok(self):
        composer_cli = ComposerCliFactory.create_mocked()
        ret = composer_cli.install()

        self.assertTrue(ret, "dovrebbe esser true") 

    if __name__ == '__main__':
        unittest.main()
