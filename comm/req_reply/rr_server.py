import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:6001")

while True:
    message = socket.recv()
    print(f"Received request: {message}")
    socket.send(b"World")