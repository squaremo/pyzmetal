from zmq.core import context as zctx
from zmq.core.constants import *

ctx = zctx.Context.instance()
sock = ctx.socket(REQ)

sock.connect("tcp://127.0.0.1:5975")
sock.send("Connection.Open", flags = SNDMORE)
sock.send_json({'protocol': {'name': "MTL", 'version': 1},
                'virtual-host': 'test-env'})

print sock.recv()
print sock.recv_json()

sock.close()
ctx.term()
