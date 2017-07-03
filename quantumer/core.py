import requests
import itchat
from quantumer.components import load_all


class Core:

    class Detector:

        def __init__(self):
            raise NotImplementedError()

    def register_trigger_function(self):
        raise NotImplementedError()

    def register_judge_function(self):
        raise NotImplementedError()

    def register_extract_function(self):
        raise NotImplementedError()

    def start(self):
        raise NotImplementedError()

load_all(Core)