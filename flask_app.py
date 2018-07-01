import json
from flask import Flask, request
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
    data = request.get_json()
    email = data['email']
    return 'Ok', 200


@app.route('/test/protobuf/', methods=['POST'])
def test_protobufs_view():
    from protobuf_config.medium_proto2_pb2 import User
    u = User()
    u.ParseFromString(request.get_data().replace(b'\r\n', b'\n'))
    email = u.email
    return 'Ok', 200


@app.route('/test/msgpack/', methods=['POST'])
def test_messagepack_view():
    data = msgpack.unpackb(request.get_data(), encoding='utf-8')
    email = data['email']
    return 'Ok', 200


@app.route('/test/large_json/', methods=['POST'])
def test_json_view():
    data = request.get_json()
    email = data['users'][0]['email']
    return 'Ok', 200


@app.route('/test/large_protobuf/', methods=['POST'])
def test_protobufs_view():
    from protobuf_config.large_proto2_pb2 import People
    p = People()
    p.ParseFromString(request.get_data().replace(b'\r\n', b'\n'))
    email = p.users[0].email
    return 'Ok', 200


@app.route('/test/large_msgpack/', methods=['POST'])
def test_messagepack_view():
    data = msgpack.unpackb(request.get_data(), encoding='utf-8')
    email = data['users'][0]['email']
    return 'Ok', 200
