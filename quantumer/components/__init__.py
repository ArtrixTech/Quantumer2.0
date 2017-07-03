from quantumer.components.detector import load_detector
from quantumer.components.register import load_register
from quantumer.components.string_operating import load_string_operating
from quantumer.components.wechat_operating import load_wechat_operating


def load_all(core):
    load_register(core)
    load_detector(core)
    load_string_operating(core)
    load_wechat_operating(core)
