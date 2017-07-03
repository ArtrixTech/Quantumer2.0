from quantumer.core import Core
from quantumer.components import load_all

ins = Core()



# Register part
register_trigger_function = ins.register_trigger_function
register_extract_function = ins.register_extract_function
register_judge_function = ins.register_judge_function

# WeChat part
start = ins.start

