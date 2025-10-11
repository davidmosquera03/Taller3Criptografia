#!/bin/bash

echo "Reseteando entorno..."

# Eliminar sample_plain
rm -rf sample_plain
echo "✓ sample_plain eliminado"

# Eliminar contenido de sample_cipher
rm -rf sample_cipher/*
echo "✓ sample_cipher limpiado"

# Copiar archivos desde backup
cp backup/* sample_cipher/
echo "✓ Archivos restaurados desde backup"

echo "Reinicio completo. Listo para ejecutar de nuevo."