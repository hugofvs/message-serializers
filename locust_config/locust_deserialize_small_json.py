import codecs
from locust import HttpLocust, TaskSet, task


fh = codecs.open('message_formats/small_message.json')
data = fh.read()


def prepare_data():
    return data


data_cache = prepare_data()


class JsonTask(TaskSet):
    @task
    def post(self):
        self.client.post('/test/json/', json=data_cache)


class WebLocust(HttpLocust):
    task_set = JsonTask
    stop_timeout = 1800  # 30 minutes
