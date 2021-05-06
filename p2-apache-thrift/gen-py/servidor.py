import glob
import sys

from calculadora import Calculadora

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import logging

logging.basicConfig(level=logging.DEBUG)


class CalculadoraHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print("me han hecho ping()")

    def suma(self, n1, n2):
        print("sumando " + str(n1) + " con " + str(n2))
        return n1 + n2

    def resta(self, n1, n2):
        print("restando " + str(n1) + " con " + str(n2))
        return n1 - n2

    def multiplicacion(self, n1, n2):
        print("multiplicando " + str(n1) + " con " + str(n2))
        return n1 * n2

    def division(self, n1, n2):
        print("dividiendo " + str(n1) + " con " + str(n2))
        return int(n1 / n2)

    def suma_vectores(self, v1, v2):
        print("sumando " + str(v1) + " con " + str(v2))
        v3 = []
        for i, w in enumerate(v1):
            v3.append(v1[i] + v2[i])
        return v3

    def resta_vectores(self, v1, v2):
        print("restando " + str(v1) + " con " + str(v2))
        v3 = []
        for i, w in enumerate(v1):
            v3.append(v1[i] - v2[i])
        return v3
    
    def multiplicacion_vectores(self, v1, v2):
        print("multiplicando " + str(v1) + " con " + str(v2))
        v3 = []
        for i, w in enumerate(v1):
            v3.append(v1[i] * v2[i])
        return v3

    def multiplicacion_matrices(self, m1, m2):
        #version modificada de la que aparece en https://es.stackoverflow.com/questions/216439/multiplicar-matrices-python
        # iterate through rows of m1
        result = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]
        for i in range(len(m1)):
            # iterate through columns of m2
            for j in range(len(m2[0])):
                # iterate through rows of m2
                for k in range(len(m2)):
                    result[i][j] += m1[i][k] * m2[k][j]
        return result


  


if __name__ == "__main__":
    handler = CalculadoraHandler()
    processor = Calculadora.Processor(handler)
    transport = TSocket.TServerSocket(host="127.0.0.1", port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print("Iniciando servidor...")
    server.serve()
    print("fin")
