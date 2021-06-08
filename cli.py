import cmd
import subprocess
import logging

class ComposerCliFactory:

    @staticmethod
    def create_real(composer_client_path):

        return ComposerCliInterface(

            ComposerCli(

                composer_client_path,

                subprocess

            )

        )

    @staticmethod
    def create_mocked():

        return ComposerCliInterface(

            ComposerCli(

                "",

                SubProcessMocked()

            )

        )


class ProcessMocked(object):  # pragma: no cover

    def __init__(self, stdout, stderr):

        self.stdout = stdout

        self.stderr = stderr

        self.returncode = 0

    def communicate(self):

        return [self.stdout, self.stderr]



class SubProcessMocked(object):  # pragma: no cover

    def call(self, cli_command, shell):

        if "ERROR" in cli_command:

            return -1

        return 0

    def Popen(self, command, shell, stdout=None, stderr=None):

        _stdout = b"Process terminated correctly"

        _stderr = b""

        if "ERROR" in command:

            _stdout = b""

            _stderr = b"Error in command"

        return ProcessMocked(_stdout, _stderr)

    def check_output(self, cli_params):

        return b"test"
        
        

class ComposerCliInterface(object):  # pragma: no cover

    'Classe per la gestione di metodi Composer'

    def __init__(self, composer_cli):

        self.composer_cli = composer_cli

    def install(self, project_dir):

        return self.composer_cli.install(project_dir)

    def uTest(self, project_dir, new_report_dir):

        return self.composer_cli.uTest(project_dir, new_report_dir)
    
    def archive(self, project_dir):

        return self.composer_cli.archive(project_dir)



class ComposerCli(object):

    def __init__(self, composer_client_path, run_process_type):

        self.run_process = run_process_type

        self.command_array = [

            composer_client_path

        ]

        self.cli = " ".join(self.command_array)

    def p__output(self, array_command):

        check = True

        logging.debug("Composer Command executed: " + " ".join(array_command))

        process = self.run_process.Popen(" ".join(array_command), shell=True)

        process.communicate()

        if not process.returncode == 0:

            check = False

        output = ""

        logging.debug("Composer Process Check: " + str(check))

        return check, output

   
    def install(self, project_dir):
        
        cmd = [
            self.cli,
            "install",
            "--working-dir=\"" + project_dir + "\""
            
        ]
        return self.p__output(cmd)

    def uTest(self, project_dir, new_report_dir):
        
        cmd = [
            "\""+ project_dir + "/vendor/bin/phpunit"+"\"",
            "--coverage-clover",
            "\""+ project_dir + new_report_dir +"\""
            
        ]
        return self.p__output(cmd)

    def archive(self, project_dir):
        cmd = [
            self.cli,
            "archive",
            "--working-dir=\"" + project_dir + "\""
        ]

        return self.p__output(cmd)