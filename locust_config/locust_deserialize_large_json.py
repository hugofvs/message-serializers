import codecs
from locust import HttpLocust, TaskSet, task


fh = codecs.open('json_samples/large_message.json')
data = fh.read()


def prepare_data():
    return data


data_cache = prepare_data()


class JsonTask(TaskSet):
    @task
    def post(self):
        self.client.post('/test/large_json/', json=data_cache)


class WebLocust(HttpLocust):
    task_set = JsonTask
    stop_timeout = 10*60  # 10 minutes
