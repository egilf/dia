from doctest import ELLIPSIS_MARKER
import numpy as np
import dia_pb2 as dia_proto

class Mesh:
    def __init__(self, msg: dia_proto.ProtoDIAStepStatus):
        self.numNodes = msg.mesh.numNodes
        self.numElms = msg.mesh.numElements
        self.elm = np.zeros(self.numElms, 4)
        self.actElms = np.zeros(self.numElms, 1)
        self.elmType = np.zeros(self.numElms, 1)
        self.nloc = np.zeros(self.numNodes, 2)
        self.ndef = np.zeros(self.numNodes, 2)
        self.ndefref = np.zeros(self.numNodes, 2)

        c = 0;
        for n in msg.mesh.nodes:
            self.nloc[c,0] = n.nloc.x
            self.nloc[c,1] = n.nloc.y
            self.ndef[c,0] = n.ndef.dx
            self.ndef[c,1] = n.ndef.dy
            self.ndefref[c,0] = n.ndefRef.dx
            self.ndefref[c,1] = n.ndefRef.dy
            c = c+1

        c = 0
        for e in msg.mesh.elements:
            self.elm[c, 0] = e.nodes[0]
            self.elm[c, 1] = e.nodes[1]
            self.elm[c, 2] = e.nodes[2]
            self.elm[c, 3] = e.nodes[3]
            self.actElms[c] = 



