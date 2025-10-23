# Taller3Criptografia

El Taller tiene como propósito analizar y simular el funcionamiento de un ransomware básico como caso de estudio en criptografía aplicada, implementando únicamente una prueba de concepto segura y controlada.

## Ejecución

1. Usar un Venv o instalar en python los paquetes de requirements.txt

```
pip install -r requirements.txt
```

2. Abrir 2 terminales

3. Ejecutar en la primera terminal

```
python attacker.py
```

y en la otra

```
python victim.py
```

4. Reiniciar entorno
   Para poder correr varias veces, se tiene la carpeta backup, donde se ubican archivos a encriptar.
   De esta forma se puede tranquilamente probar el codigo varias veces sin tener que volver a manualmente ubicar los archivos en su lugar y borrar las encriptaciones.

ejecutar reset.sh

```
./reset.sh
```

## Diagrama de Flujo

![diagrama](/img/Modelo%20A.png)

## Capturas

### Pre-Ataque

Aquí se pueden ver los archivos cruciales para la victima, especialmente el primero.
![Pre-Ataque](/img/preAtaque.png)

### Ataque

Tras la encripción se pierde acceso a los archivos y se tiene una nota pidiendo un pago
![Ataque](/img/Ataque.png)

### Recuperación

Tras el 'pago', los archivos están disponibles de nuevo
![Recuperacion](/img/postPago.png)

## Reflexion

Preguntas de reflexión. Además de la simulación, respondan en un documento:

1.  Como atacante: ¿qué estrategias usaría para lograr que la víctima instale el ransom
    ware (paso 1)? Discútalo en términos teóricos (phishing, ingeniería social, etc.), sin
    implementar nada.

2.  ¿Qué otros canales podría usarse en el paso 2 (intercambio de claves) para evitar
    sospechas? Ejemplo: un canal encubierto en tráfico ICMP. Describa el concepto, no
    su implementación.

3.  Como defensor: ¿qué políticas y prácticas de seguridad (copias de seguridad, seg
    mentación, monitoreo, hardening, concientización) mitigarían la ocurrencia de este
    tipo de ataques?
