import requests
import time
import threading
from types import FunctionType


def load_detector(core):
    core.Detector = Detector


class Detector:

    def __init__(self):
        self.__url = False
        self.__interval = False
        self.stop = False
        self.__judge_function = False
        self.__extract_function = False
        self.__trigger_function = False

    def set_url(self, url_in):
        self.__url = url_in

    def set_interval(self, interval_in):
        self.__interval = interval_in

    def set_functions(self, trigger, extract, judge=False):
        if judge:
            if all([isinstance(trigger, FunctionType), isinstance(
                    extract, FunctionType), isinstance(judge, FunctionType)]):
                self.__extract_function = extract
                self.__trigger_function = trigger
                self.__judge_function = judge
            else:
                raise TypeError
        else:
            if all([isinstance(trigger, FunctionType),
                    isinstance(extract, FunctionType)]):
                self.__extract_function = extract
                self.__trigger_function = trigger
            else:
                raise TypeError

    def start_listening(self):
        assert self.__url
        assert self.__interval
        thread = threading.Thread(target=self.loop_thread)
        thread.start()

    def loop_thread(self):

        def update():
            pass

        old_stamp = time.time()
        while True:
            if time.time() - old_stamp >= int(self.__interval):
                old_stamp = time.time()
            time.sleep(1)
            if self.stop:
                break
