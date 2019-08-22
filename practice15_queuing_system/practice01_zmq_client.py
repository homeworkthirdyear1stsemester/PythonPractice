import zmq

context = zmq.Context()
sock = context.socket(zmq.PULL)  # queue 에 존재 하지 않으므로 오류가 나지 않는다
sock.connect("tcp://127.0.0.1:5690")

while True:
    message = sock.recv()
    print("Received: {}".format(message.decode()))
