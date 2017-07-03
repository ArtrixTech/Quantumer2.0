import quantumer
from quantumer.components.string_operating import cut_string


@quantumer.register_extract_function()
def one(kw):

    ret_str = cut_string(
        kw["content"], kw["head"], kw["tail"])

    return ret_str


@quantumer.register_trigger_function()
def show():
    print("OK!")

quantumer.start()