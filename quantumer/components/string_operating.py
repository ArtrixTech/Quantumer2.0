def load_string_operating(core):
    core.cut_string = cut_string


@staticmethod
def cut_string(input_str, head, tail):
    if isinstance(
        head,
        str) and isinstance(
            tail,
            str) and isinstance(
            input_str,
            str):
        start = input_str.find(head) + len(head)
        end = input_str.find(tail, start)

        rt_str = ""
        for index in range(start, end):
            rt_str += input_str[index]
        return rt_str
    else:
        raise TypeError("Inputs are not string!")

@staticmethod
def one(kw):

    ret_str = cut_string(
        kw["content"], kw["head"], kw["tail"])

    return ret_str

@staticmethod
def two(kw):

    ret_str = cut_string(
        kw["content"], kw["head"], kw["tail"])
    ret_str = cut_string(ret_str, kw["head2"], kw["tail2"])

    return ret_str