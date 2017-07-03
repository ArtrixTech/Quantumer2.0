import itchat
import requests
import threading
from itchat.content import *
from quantumer.components.detector import Detector
from quantumer.components.string_operating import cut_string

core=False

def set_core(core2):
    core=core2

def load_wechat_operating(core):
    #itchat.out_core = core
    core.new_detector = new_detector
    core.start = start
    core.is_in_detector_pool=is_in_detector_pool


def new_detector(self, username):
    det = Detector()
    self.detector_pool[username] = det

    return det


def is_in_detector_pool(self, username):
    try:
        assert isinstance(self.detector_pool[username], Detector)
        return True
    except:
        pass
    return False


def start(self):
    itchat.auto_login(hotReload=True, enableCmdQR=1)
    thread = threading.Thread(
        target=itchat.run,
        name="thread1", )
    thread.start()


class Generator:

    step = 0
    url = ""
    interval = ""
    content = ""
    head = ""
    tail = ""
    is_guide = False

    def generate(self):
        html = requests.get(self.url).text

        is_finished = False
        char = 50
        while not is_finished:
            start_place = html.find(self.content) - char
            self.head = html[start_place:start_place + char]

            start_place = html.find(self.content) + len(self.content)
            self.tail = html[start_place:start_place + 1]

            command = "开始监听 url=%s,head1=%s,tail1=%s,interval=%s," % (
                self.url, self.head, self.tail, self.interval)
            if "\n" in command:
                if not char == 0:
                    char -= 1
                else:
                    print("Generate Failed!")
            else:
                is_finished = True
        return "开始监听 url=%s,head1=%s,tail1=%s,interval=%s," % (
            self.url, self.head, self.tail, self.interval)

g = Generator()


def first_result_show(username, content):
    itchat.send(content, username)


@itchat.msg_register(TEXT)
def simple_reply(msg):

    core = itchat.out_core
    user_name = msg['FromUserName']
    if g.is_guide:
        if g.step == 0:
            g.url = str(msg['Text'])
            g.step = 1
            return "输入每次刷新时间(秒)，建议20秒:"
        if g.step == 1:
            g.interval = str(msg['Text'])
            g.step = 2
            return "输入要抓取的内容:"
        if g.step == 2:
            g.content = str(msg['Text'])
            g.step = 3
            itchat.send("请输入“开始”以开始监听，或者复制以下内容，发送至本账号来开始监听。", user_name)
            return g.generate()
        if g.step == 3:
            g.step = 0
            g.is_guide = False
            if "开始" in str(msg['Text']):
                m = msg
                m['Text'] = g.generate()
                simple_reply(m)
                return ""
            else:
                return "取消自动开始"

    if msg['Type'] == 'Text':
        text = str(msg['Text'])
        if "开始监听" in text:

            command = text.replace("开始监听,", "")
            print("User:" + user_name + "开始新任务")
            exist = core.is_in_detector_pool(core, user_name)

            if exist:
                itchat.send("开始新任务！旧任务已停止", user_name)
                old_det = core.detector_pool[user_name]
                assert isinstance(old_det, Detector)
                old_det.stop_listening()
            else:
                itchat.send("开始新任务", user_name)
            det = core.new_detector(core,user_name)

            # Get arguments from the WeChat commands.
            url = cut_string(command, "url=", ",")
            head = cut_string(command, "head1=", ",")
            tail = cut_string(command, "tail1=", ",")
            interval = cut_string(command, "interval=", ",")

            # assert core.function_inited
            det.set_url(url)
            det.set_interval(interval)
            det.set_test_func(first_result_show)
            print(core)
            det.set_functions(trigger=core.trigger_function, extract=core.extract_function)
            det.set_args({"head": head, "tail": tail})

            def send_task_message():
                itchat.send("任务信息：", user_name)
                itchat.send("url：" + url, user_name)
                itchat.send("间隔Interval：" + interval, user_name)

            send_task_message()
            det.username = user_name
            det.start_listening()

            return

        elif "停止监听" in text:

            user_name = msg['FromUserName']
            exist = core.is_in_detector_pool(core, user_name)

            if exist:
                old_det = core.detector_pool[user_name]
                assert isinstance(old_det, Detector)
                old_det.stop_listening()
                core.detector_pool[user_name] = False
            return "任务停止"

        elif "生成命令" in text:
            g.is_guide = True
            return "输入url"
        else:
            return "命令有误，请重新输入"


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text'])  # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg(
        '你好！请输入“生成命令”来开始一个新的任务。Hello!Please enter "生成命令" to start a new task!',
        msg['RecommendInfo']['UserName'])
