# Message Serializers
This project was built to benchmark various serializers used in context of HTTP requests. We compare JSON vs. Protobufs vs. MessagePack running on a Flask service.

## Getting Started

#### Requirements
- pip
- virtualenv & virtualenvwrapper
- python 2.7.10

#### Flask Service
1. Create virtual environment  
`mkvirtualenv message_serializers`

2. Install project requirements  
`pip install -r requirements.txt`

3. Run Flask server
`sh run_server.sh`


#### Locust


## VM Instances

## Built With

## Authors

Compile Protobuf to python
protoc --python_out=message_formats/ message_formats/giant_proto2.proto
