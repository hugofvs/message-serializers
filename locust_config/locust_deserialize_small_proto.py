import codecs
import json
from locust import HttpLocust, TaskSet, task
from message_formats.small_proto2_pb2 import User


fh = codecs.open('message_formats/small_message.json')


def prepare_data():
    data_dict = json.loads(fh.read())
    user = User()
    user.username = data_dict['username']
    user.email = data_dict['email']
    user.age = data_dict['age']
    return user.SerializeToString()


class ProtoTask(TaskSet):
    @task
    def post(self):
        self.client.post("/test/protobuf/", data=prepare_data())


class WebLocust(HttpLocust):
    task_set = ProtoTask
    stop_timeout = 1800  # 30 minutes
