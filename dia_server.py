import time
import zmq
import dia_msg_pb2 as dia_proto
import numpy as np
from matplotlib import pyplot as plt
import NodesAsSubsets

def get_refi(message: dia_proto.ProtoDIAStepStatus) -> np.ndarray:
    shape = (height, width) = (message.refI.height, message.refI.width)
    bytes_per_pixel = message.refI.format.bytes_per_pixel
    data = message.refI.data
    if height*width*bytes_per_pixel != len(data):
        raise ValueError("Image format does not match with number of bytes")
    format = message.refI.format.pixel_format
    if format == dia_proto.PIXEL_FORMAT_UINT8:
        return np.frombuffer(data, dtype=np.uint8).reshape(shape)
    if format == dia_proto.PIXEL_FORMAT_UINT16:
        return np.frombuffer(data, dtype=np.uint16).reshape(shape)
    if format == dia_proto.PIXEL_FORMAT_FLOAT32:
        return np.frombuffer(data, dtype=np.float32).reshape(shape)
    if format == dia_proto.PIXEL_FORMAT_FLOAT64:
        return np.frombuffer(data, dtype=np.float64).reshape(shape)    
    raise ValueError("Unknown pixel format in message!")

def get_curi(message: dia_proto.ProtoDIAStepStatus) -> np.ndarray:
    shape = (height, width) = (message.curI.height, message.curI.width)
    bytes_per_pixel = message.curI.format.bytes_per_pixel
    data = message.curI.data
    if height*width*bytes_per_pixel != len(data):
        raise ValueError("Image format does not match with number of bytes")
    format = message.curI.format.pixel_format
    if format == dia_proto.PIXEL_FORMAT_UINT8:
        return np.frombuffer(data, dtype=np.uint8).reshape(shape)
    if format == dia_proto.PIXEL_FORMAT_UINT16:
        return np.frombuffer(data, dtype=np.uint16).reshape(shape)
    if format == dia_proto.PIXEL_FORMAT_FLOAT32:
        return np.frombuffer(data, dtype=np.float32).reshape(shape)
    if format == dia_proto.PIXEL_FORMAT_FLOAT64:
        return np.frombuffer(data, dtype=np.float64).reshape(shape)    
    raise ValueError("Unknown pixel format in message!")
 

if __name__=="__main__":

    context = zmq.Context()                                 # https://zeromq.org/socket-api/
    socket = context.socket(zmq.REP)
    address = "tcp://*:5555"
    socket.bind(address)
    print("Socket.Bind() to: %s" % address);
    print("Waiting for requests...");

    while True:
        received = socket.recv()
        #print(f'Buffer length: %i' % len(received))
        t = time.time()
        msg = dia_proto.ProtoDIAStepStatus.FromString(received)
        refI = get_refi(msg)
        curI = get_refi(msg)
        #refI = np.nan_to_num(refI)
        #curI = np.nan_to_num(curI)
        mesh = msg.mesh

        #NodesAsSubsets.CorrelateNodesAsRigidSubsets(mesh, refI, curI)
        
        print("Frame Idx: %i" % msg.fidIdx)
        
        #elapsed = time.time() - t
        #print("Processed in: %f [sec]" % elapsed)

        #plt.imshow(curI, interpolation='nearest')
        #plt.show()
        #print("Received message with size: %i" % received.count())
        #length = len(received)
        #print(f'Length of this bytes object is {length}.')
        #refI = get_refi(msg)
        #refI = np.nan_to_num(refI)
        #time.sleep(1)

        #socket.send(msg.SerializeToString());
        socket.send(b"Continue")                            #Send 'Continue' if you dont want to upload data to DIACore
