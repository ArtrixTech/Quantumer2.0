from quantumer.components import load_all


class Core:

    judge_function = False
    extract_function = False
    trigger_function = False
    function_inited=False
    detector_pool = dict()

    # Detector----------------------------------
    class Detector:

        def __init__(self):
            raise NotImplementedError()

    # String operations-------------------------
    @staticmethod
    def cut_string(input_str, head, tail):
        raise NotImplementedError()

    # Register----------------------------------
    def register_trigger_function(self):
        raise NotImplementedError()

    def register_judge_function(self):
        raise NotImplementedError()

    def register_extract_function(self):
        raise NotImplementedError()

    # WeChat operations-------------------------
    def start(self):
        raise NotImplementedError()

    def new_detector(self, username):
        raise NotImplementedError()

    def is_in_detector_pool(self, username):
        raise NotImplementedError()


load_all(Core)
