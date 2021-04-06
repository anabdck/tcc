$ cd ../
$ git clone https://github.com/anabdck/pcb-defect-detection-api.git
$ cd pcb-defect-detection-api
$ pip3 install virtualenv
$ python3 -m venv flask_venv
$ source flask_venv/bin/activate
$ pip3 install -r requirements.txt
$ cp ../Darknet/libdarknet.so libdarknet.so
$ python run.py runserver --host 0.0.0.0
