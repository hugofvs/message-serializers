import codecs
from locust import HttpLocust, TaskSet, task


fh = codecs.open('message_formats/big_message.json')
data = fh.read()


def prepare_data():
    return data


class JsonTask(TaskSet):
    @task
    def post(self):
        self.client.post('/test/base/', json=prepare_data())


class WebLocust(HttpLocust):
    task_set = JsonTask
    stop_timeout = 1800  # 30 minutes
