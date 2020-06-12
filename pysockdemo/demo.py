import socketio
import time
import random

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.on('panda')
def on_message(data):
    print(data)

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://kstaging.tech:3000')

l = ["PY:laying", "PY:moving", "PY:standing"]

while True:
    mes = random.choice(l)
    sio.emit('panda',mes)
    print("emit:" + mes)
    time.sleep(3)