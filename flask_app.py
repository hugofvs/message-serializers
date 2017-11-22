from flask import Flask, request
from message_formats.small_proto3_pb2 import User


app = Flask(__name__)


@app.route('/test/json/', methods=['POST'])
def test_json_view():
    username = request.get_json()['username']
    return username, 200


@app.route('/test/protobuf/', methods=['POST'])
def test_protobufs_view():
    u = User()
    u.ParseFromString(request.get_data().replace(b'\r\n', b'\n'))
    return u.username, 200
