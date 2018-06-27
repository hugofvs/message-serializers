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
from protobuf_config.medium_proto2_pb2 import User, Friend


fh = codecs.open('json_samples/medium_message.json')
data = fh.read()


def prepare_data():
    data_dict = json.loads(data)
    user = User()
    user._id = data_dict['_id']
    user.isActive = data_dict['isActive']
    user.balance = data_dict['balance']
    user.picture = data_dict['picture']
    user.age = data_dict['age']
    user.firstName = data_dict['firstName']
    user.lastName = data_dict['lastName']
    user.email = data_dict['email']
    user.phone = data_dict['phone']
    user.address = data_dict['address']
    user.about = data_dict['about']
    user.registered = data_dict['registered']

    for tag in data_dict['tags']:
        user.tags.append(tag)

    for fr in data_dict['friends']:
        friend = Friend()
        friend._id = fr['_id']
        friend.firstName = fr['firstName']
        friend.lastName = fr['lastName']
        friend.last_login = fr['last_login']
        friend.last_message = fr['last_message']
        user.friends.extend([friend])

    return user.SerializeToString()


data_cache = prepare_data()


class ProtoTask(TaskSet):
    @task
    def post(self):
        self.client.post("/test/protobuf/", data=data_cache)


class WebLocust(HttpLocust):
    task_set = ProtoTask
    stop_timeout = 10*60  # 10 minutes
