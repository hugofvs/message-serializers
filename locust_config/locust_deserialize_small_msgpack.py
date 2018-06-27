import codecs
import json
from locust import HttpLocust, TaskSet, task
import msgpack


fh = codecs.open('json_samples/small_message.json')
data = fh.read()


def prepare_data():
    data_dict = json.loads(data)
    return msgpack.dumps(data_dict)


data_cache = prepare_data()


class ProtoTask(TaskSet):
    @task
    def post(self):
        self.client.post("/test/msgpack/", data=data_cache)


class WebLocust(HttpLocust):
    task_set = ProtoTask
    stop_timeout = 10*60  # 10 minutes
