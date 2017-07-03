from quantumer.components import load_all


class Core:

    # Detector
    class Detector:

        def __init__(self):
            raise NotImplementedError()

    # String operations
    @staticmethod
    def cut_string(input_str, head, tail):
        raise NotImplementedError()

    # Register
    def register_trigger_function(self):
        raise NotImplementedError()

    def register_judge_function(self):
        raise NotImplementedError()

    def register_extract_function(self):
        raise NotImplementedError()

    # WeChat operations
    def start(self):
        raise NotImplementedError()


load_all(Core)
