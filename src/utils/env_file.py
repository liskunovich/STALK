class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Environment(metaclass=Singleton):
    env = None

    def __init__(self):
        import os
        from dotenv import load_dotenv

        load_dotenv()
        self.env = os.getenv
