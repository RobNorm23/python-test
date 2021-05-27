import logging
import os
from cli import ComposerCliFactory

logging.basicConfig(format='[%(levelname)s] %(filename)s/%(funcName)s - %(message)s',
                    level=logging.DEBUG)  # pragma: no cover


class ComposerClientType:  # pragma: no cover

    REAL = "real"

    MOCKED = "mocked"


class ComposerClientFactory:

    @staticmethod
    def create_real(composer_client_path, project_dir, new_report_dir):

        return ComposerClientInterface(

            ComposerClient(

                composer_client_path,

                project_dir,

                new_report_dir,

                ComposerClientType.REAL

            )

        )

    @staticmethod
    def create_mocked(project_dir, new_report_dir,):

        return ComposerClientInterface(

            ComposerClient(

                "",

                project_dir,

                new_report_dir,

                ComposerClientType.MOCKED

            )

        )


class ComposerClientInterface(object):  # pragma: no cover

    def __init__(self, composer_client):

        self.composer_client = composer_client

    def install(self):

        return self.composer_client.install()

    def uTest(self):

        return self.composer_client.uTest()

    def archive(self):

        return self.composer_client.archive()


class ComposerClient(object):

    def __init__(self, composer_client_path, project_dir, new_report_dir, client_type):

        self.project_dir = project_dir
        self.new_report_dir = new_report_dir

        if client_type == ComposerClientType.REAL:

            if not os.path.exists(project_dir):

                raise Exception("Json file " + project_dir + " does't exist.")

            self.composer_cli = ComposerCliFactory().create_real(composer_client_path)

        elif client_type == ComposerClientType.MOCKED:

            self.composer_cli = ComposerCliFactory().create_mocked()

    def install(self):

        ret = self.composer_cli.install(self.project_dir)
        if (ret == False):

            return False

        return self.composer_cli.uTest(self.project_dir, self.new_report_dir)

    def archive(self):

        return self.composer_cli.archive(self.project_dir)
