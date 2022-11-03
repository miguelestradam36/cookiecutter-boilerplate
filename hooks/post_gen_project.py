class PostHook():
    def __init__(self):
        self.REMOVE_PATHS = [
            '{% if cookiecutter.packaging != "pip" %} requirements.txt {% endif %}',
            '{% if cookiecutter.packaging != "poetry" %} poetry.lock {% endif %}',
        ]
    def remove_files(self)->None:
        import os
        for path in self.REMOVE_PATHS:
            path = path.strip()
            if path and os.path.exists(path):
                if os.path.isdir(path):
                    os.rmdir(path)
                else:
                    os.unlink(path)

if __name__ == "__main__":
    buff = PostHook()
    buff.remove_files()
