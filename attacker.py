import socket
import pickle
import random

HOST = '127.0.0.1'
PORT = 65432

# ATACANTE escucha
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
print("⏳ Atacante esperando conexión...")

conn, addr = sock.accept()
print(f"✓ Víctima conectada desde {addr}")

# Recibir pk
pk_bytes = conn.recv(4096)
pk = pickle.loads(pk_bytes)
print(f"✓ Clave pública recibida: {pk}")

# Generar secreto 's' y cifrarlo
(n, e) = pk
s = random.randint(1, n-1)
c = pow(s, e, n)  # c = s^e mod n
#print(f"✓ Secreto 's' generado: {s}")
print(f"✓ Secreto 's' generado")
print(f"✓ Guardando 's' para rescate...")

# Enviar 'c' a la víctima
c_bytes = pickle.dumps(c)
conn.sendall(c_bytes)

conn.close()
sock.close()