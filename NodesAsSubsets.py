import dia_pb2 as dia_proto
import numpy as np

def CorrelateNodesAsRigidSubsets(mesh : dia_proto.ProtoMesh, refI : np.ndarray, curI : np.ndarray):
    
    for e in mesh.elements:
        e.active = False; #Sets all elements inactivate

