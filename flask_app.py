from flask import Flask


app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/', methods=['GET'])
def index():
    return 'Hello, World!'


@app.route('/test/json/', methods=['POST'])
def test_json_view():
    # username = request.get_json()['username']
    return 'Ok', 200


@app.route('/test/protobuf/', methods=['POST'])
def test_protobufs_view():
    # u = User()
    # u.ParseFromString(request.get_data().replace(b'\r\n', b'\n'))
    return 'Ok', 200


@app.route('/test/messagepack/', methods=['POST'])
def test_messagepack_view():
    # user_dict = msgpack.unpackb(request.get_data(), encoding='utf-8')
    return 'Ok', 200
