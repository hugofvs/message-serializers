from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda: 0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)


import codecs
import json
from locust import HttpLocust, TaskSet, task
from message_formats.small_proto2_pb2 import User


fh = codecs.open('message_formats/small_message.json')
data = fh.read()


def prepare_data():
    data_dict = json.loads(data)
    user = User()
    user.username = data_dict['username']
    user.email = data_dict['email']
    user.age = data_dict['age']
    return user.SerializeToString()


data_cache = prepare_data()


class ProtoTask(TaskSet):
    @task
    def post(self):
        self.client.post("/test/protobuf/", data=data_cache)


class WebLocust(HttpLocust):
    task_set = ProtoTask
    stop_timeout = 1800  # 30 minutes
