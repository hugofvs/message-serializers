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

2. Activate virtualenv  
`workon message_serializers`

3. Install project requirements  
`pip install -r requirements.txt`

4. Run Flask server  
`sh run_server.sh`


#### Locust
1. Open a new terminal in the same project folder

2. Activate virtualenv  
`workon message_serializers`

3. Run Locust (use different configuration file depending on experiment)  
`locust -f locust_config/<LOCUST CONFIG>.py --host=<FLASK SERVER> --web-host=0.0.0.0`

4. Open Locust in browser  
`0.0.0.0:8089`


## VM Instances
To run the experiments under a controlled environment, we launched 2 instances in Google Cloud - g1-small (1 vCPU, 1.7 GB memory) - one for the Flask server and another just for Locust.


## Acknowledgments
A big thank you to [@marcelolebre](https://github.com/marcelolebre) (my master Yoda) who introduced me to this technologies and pushed me to publish the blogpost.
