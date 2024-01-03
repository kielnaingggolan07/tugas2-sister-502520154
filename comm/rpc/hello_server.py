import zerorpc

class HelloRPC(object):
    def hello(self, name):
        return "Hello, %s" % name
    @zerorpc.stream
    def get_stream(self):
        return range(0,1000)

    def bad(self):
        raise Exception('its bad')

s = zerorpc.Server(HelloRPC())
s.bind("tcp://*:9999")
s.run()