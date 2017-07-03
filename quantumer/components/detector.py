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
        self.__extract_function_args = False
        self.username = False
        self.__test_func = False
        self.__count = 1
        self.old = False

    def set_test_func(self, func):
        if isinstance(func, FunctionType):
            self.__test_func = func

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

    def set_args(self, args):
        if args:
            self.__extract_function_args = args
        else:
            raise ValueError

    def start_listening(self):
        assert self.__url
        assert self.__interval
        assert self.__extract_function
        assert self.__trigger_function
        assert self.__test_func
        thread = threading.Thread(target=self.loop_thread)
        thread.start()

    def stop_listening(self):
        self.stop = True

    def loop_thread(self):

        def update(init=False):

            content = requests.get(self.__url).text
            if init:
                # Execute the init check
                self.__extract_function_args["content"] = content
                assert isinstance(self.__extract_function, FunctionType)
                assert isinstance(self.__test_func, FunctionType)
                now = self.__extract_function(self.__extract_function_args)
                self.__test_func(self.username, "测试提取:" + now)
                print("Now the %s check." % str(self.__count + 1))
                self.__count += 1
                self.old = now
                print("Now result:%s" % now)
            else:
                # Execute the alternative check
                assert isinstance(self.__extract_function, FunctionType)
                assert isinstance(self.__trigger_function, FunctionType)
                now = self.__extract_function(self.__extract_function_args)
                if not now == self.old:
                    self.__trigger_function()
                self.old = now

        update(True)
        old_stamp = time.time()
        while True:
            if time.time() - old_stamp >= int(self.__interval):
                old_stamp = time.time()
                update()
            time.sleep(1)
            if self.stop:
                break
