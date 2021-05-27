from client import ComposerClientFactory
class main():

    def main():     
        composer_client = ComposerClientFactory.create_real("C:/ProgramData/ComposerSetup/bin/composer", "C:/Users/rcastruc/OneDrive - Capgemini/Desktop/php-test", "coverage/report.xml")
        check, message = composer_client.install()
        print(check, message)
        if(check == True):
            archive = composer_client.archive()
            print(archive)

    if __name__ == "__main__":
        main()