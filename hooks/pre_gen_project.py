class PreHook():

    defaults = r'\config\defaults.yaml'
    installments = '{{ cookiecutter.installs }}'
    log = __import__('logging')
    prefix = r'python'

    def __init__(self):
        import os
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.installments = self.installments.strip()
        #Init logging
        self.init_logging()
        self.log.info("Started pre-hook class object")

    def read_defaults(self)->None:
        try:
            if self.installments == "Automatic":
                import yaml
                filepath = self.dir_path + self.defaults
                self.log.info('Reading YAML Config file')
                with open(filepath, 'r') as file:
                    self.data = yaml.load(file)
                    self.flag = True
        except ImportError as importerror:
            self.log.error("IMPORT ERROR: {}".format(importerror))
        except Exception as error:
            self.log.error("GENERAL ERROR: {}".format(error))

    def install_modules(self)->None:
        if self.flag:
            self.log.info("Checking in to installations...")
            if self.installments == "Automatic":
                for module in self.data["defaults"]["installs"]:
                    try:
                        self.log.info("Checking {} module into venv".format(module))
                        assert __import__(module)
                    except ImportError as error:
                        self.log.info("Installing {} module into venv".format(module))
                        self.os.system("{} pip install {}".format(self.prefix, module))
                    except Exception as error:
                        self.log.error("ERROR: {}".format(error))
            else:
                self.log.error("Install modules through the requirements.txt file")
                print("Read logs...\nInstall modules through the requirements.txt file")
        else:
            self.log.error("YAML file has not been readed")
            print("Read logs...\nYAML file has not been readed")

    def init_logging(self)->None:
        import logging
        logFileFormatter = logging.Formatter(
            fmt=f"%(levelname)s %(asctime)s (%(relativeCreated)d) \t %(pathname)s F%(funcName)s L%(lineno)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        fileHandler = logging.FileHandler(filename='pre-hook.log')
        fileHandler.setFormatter(logFileFormatter)
        fileHandler.setLevel(level=logging.INFO)
        logging.basicConfig(level=logging.INFO)
        self.log = logging.getLogger(__name__) #<<<<<<<<<<<<<<<<<<<<
        self.log.addHandler(fileHandler)

    def deprecation_warning(self)->None:
        statement = """
                =============================================================================
                *** DEPRECATION WARNING ***

                Cookiecutter data science is moving to v2 soon, which will entail using
                the command `ccds ...` rather than `cookiecutter ...`. The cookiecutter command
                will continue to work, and this version of the template will still be available.
                To use the legacy template, you will need to explicitly use `-c v1` to select it.

                Please update any scripts/automation you have to append the `-c v1` option,
                which is available now.

                For example:
                    cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science
                =============================================================================
        """
        print(statement)
        self.log.error(statement)
    
    def __del__(self):
        self.log.info("---Pre Hook Finished---")

if __name__ == "__main__":
    buff = PreHook()
    buff.deprecation_warning()
    buff.read_defaults()
    buff.install_modules()
