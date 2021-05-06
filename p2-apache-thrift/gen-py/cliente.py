from calculadora import Calculadora

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

#import numpy as np 

transport = TSocket.TSocket("localhost", 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Calculadora.Client(protocol)

transport.open()

print("Pedro Padilla Reyes\nCalculadora implementada con Python y Apache Thrift\n")
print("Suma y resta implementadas por el profesor")
print("Hacemos ping al server")
client.ping()

resultado = client.suma(1, 1)
print("1 + 1 = " + str(resultado))
resultado = client.resta(1, 1)
print("1 - 1 = " + str(resultado))
resultado = client.multiplicacion(2,2)
print("2 * 2 = " + str(resultado))
resultado = client.division(6,2)
print("6 / 2 = " + str(resultado))

print("\nVectores:")
lst1 = [1,2,3,4,5]
lst2 = [5,4,3,2,1]
resultado = client.suma_vectores(lst1, lst2)
print(lst1)
print( " + ")
print(lst2)
print( " = " + str(resultado))
print("\n")
resultado = client.resta_vectores(lst1, lst2)
print(lst1)
print( " - ")
print(lst2)
print( " = " + str(resultado))
print("\n")
resultado = client.multiplicacion_vectores(lst1,lst2)
print(lst1)
print( " * ")
print(lst2)
print( " = " + str(resultado))
print("\n")

print("Matrices:")
m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2= [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
resultado = client.multiplicacion_matrices(m1, m2)
for i in range(len(m1)):
    for j in range(len(m1[i])):
        print(m1[i][j], end=' ')
    print()
print(" * ")
for i in range(len(m2)):
    for j in range(len(m2[i])):
        print(m2[i][j], end=' ')
    print()
print( " = " + str(resultado))


transport.close()
