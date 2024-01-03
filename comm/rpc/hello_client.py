import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:9999")
print(c.hello("RPC"))

for i in c.get_stream():
    print(i)

try:
    c.bad()
except Exception as e:
    print(str(e))