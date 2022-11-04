class PostHook():
    
    log = __import__('logging')

    def __init__(self):
        self.REMOVE_PATHS = [
            '{% if cookiecutter.makefile != "Included" %} Makefile {% endif %}'
        ]
        self.init_logging()

    def remove_files(self)->None:
        import os
        for path in self.REMOVE_PATHS:
            path = path.strip()
            if path and os.path.exists(path):
                if os.path.isdir(path):
                    os.rmdir(path)
                    self.log.info("Deleting file: {}".format(path))
                else:
                    os.unlink(path)
                    self.log.info("Unlinking file: {}".format(path))
            else:
                self.log.error("File does not exist: {}".format(path))

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

if __name__ == "__main__":
    buff = PostHook()
    buff.remove_files()
