import sys
import zmq


#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from weather server...")

#direct to server
socket.connect("tcp://localhost:5556")

#via proxy at port 8100
socket.connect("tcp://localhost:8100")

# Subscribe to zipcode, default is NYC, 10001
zip_filter = "10001"
socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)

# Process 5 updates
total_temp = 0
for update_nbr in range(5):
    string = socket.recv_string()
    zipcode, temperature, relhumidity = string.split()
    total_temp += int(temperature)

    print((f"Average temperature for zipcode " 
       f"'{zip_filter}' was {total_temp / (update_nbr+1)} F"))