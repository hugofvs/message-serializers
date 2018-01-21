import codecs
import json
from locust import HttpLocust, TaskSet, task
import msgpack


fh = codecs.open('message_formats/big_message.json')
data = fh.read()


def prepare_data():
    data_dict = json.loads(data)
    return msgpack.dumps(data_dict)


class ProtoTask(TaskSet):
    @task
    def post(self):
        self.client.post("/test/base/", data=prepare_data())


class WebLocust(HttpLocust):
    task_set = ProtoTask
    stop_timeout = 1800  # 30 minutes
