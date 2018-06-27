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
from protobuf_config.large_proto2_pb2 import People, User, Friend


fh = codecs.open('json_samples/large_message.json')
data = fh.read()


def prepare_data():
    data_dict = json.loads(data)
    people = People()
    for user_dict in data_dict['users']:

        user = User()
        user._id = user_dict['_id']
        user.isActive = user_dict['isActive']
        user.balance = user_dict['balance']
        user.picture = user_dict['picture']
        user.age = user_dict['age']
        user.firstName = user_dict['firstName']
        user.lastName = user_dict['lastName']
        user.email = user_dict['email']
        user.phone = user_dict['phone']
        user.address = user_dict['address']
        user.about = user_dict['about']
        user.registered = user_dict['registered']

        for tag in user_dict['tags']:
            user.tags.append(tag)

        for fr in user_dict['friends']:
            friend = Friend()
            friend._id = fr['_id']
            friend.firstName = fr['firstName']
            friend.lastName = fr['lastName']
            friend.last_login = fr['last_login']
            friend.last_message = fr['last_message']
            user.friends.extend([friend])

        people.users.extend(user)

    return people.SerializeToString()


data_cache = prepare_data()


class ProtoTask(TaskSet):
    @task
    def post(self):
        self.client.post("/test/base/", data=data_cache)


class WebLocust(HttpLocust):
    task_set = ProtoTask
    stop_timeout = 10*60  # 10 minutes
