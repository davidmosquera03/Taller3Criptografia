import socket
import pickle
from rsa_crypto import RSA

rsa = RSA()
sk, pk = rsa.Grsa(2048, 65537)

# Conectar y enviar pk
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 65432))
sock.sendall(pickle.dumps(pk))

# Recibir c
c = pickle.loads(sock.recv(4096))
sock.close()

# Descifrar s
s = rsa.Irsa(sk, c)
#print(f"Secreto obtenido: {s}")
print(f"Secreto obtenido")


