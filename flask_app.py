import json
from flask import Flask, request
from protobuf_config.medium_proto2_pb2 import User
import msgpack


app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/', methods=['GET'])
def index():
    return 'Message Encryption Benchmark'


@app.route('/test/base/', methods=['POST'])
def test_base_view():
    return 'Ok', 200


@app.route('/test/json/', methods=['POST'])
def test_json_view():
    data = json.loads(request.get_json())
    email = data['email']
    return 'Ok', 200


@app.route('/test/protobuf/', methods=['POST'])
def test_protobufs_view():
    u = User()
    u.ParseFromString(request.get_data().replace(b'\r\n', b'\n'))
    email = u.email
    return 'Ok', 200


@app.route('/test/msgpack/', methods=['POST'])
def test_messagepack_view():
    data = msgpack.unpackb(request.get_data(), encoding='utf-8')
    email = data['email']
    return 'Ok', 200
