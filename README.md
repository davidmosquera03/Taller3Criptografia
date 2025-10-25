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

    Como atacante puedo aprovechar distintas vulnerabilidades que dan puerta abierta para acceder a los dispositivos de las víctimas.

    Phishing: El más común, usando ingeniería social se aprovecha del “error humano” para abusar de la víctima y así cumplir el objetivo de acceder a los datos sensibles de esta. Se puede encontrar de distintas modalidades, como en correos electrónicos maliciosos, paginas fraudulentas, encuestas falsas, etc. La opción más común es el correo, puesto que usa la excusa de enviar un archivo adjunto infectado con el RansomWare, engañando a la víctima con la excusa de consultar información relevante, haciendo que baje el archivo, lo extraiga y ejecute.

2.  ¿Qué otros canales podría usarse en el paso 2 (intercambio de claves) para evitar
    sospechas? Ejemplo: un canal encubierto en tráfico ICMP. Describa el concepto, no
    su implementación.

    Existen otras alternativas que podrían usarse para el intercambio de claves:

    Tráfico ICMP encubierto
    Concepto: usar mensajes ICMP (por ejemplo, echo request/reply) para transportar pequeños fragmentos de datos dentro de los campos útiles del paquete. 
    
    ICMP suele considerarse diagnóstico, por eso a veces pasa por alto.
    Túneles DNS (ej.: consultas/resp. y registros TXT)
    Concepto: codificar información dentro de consultas 
    
    DNS o dentro de registros (como registros TXT) para que la clave viaje como parte de nombres de dominio o de respuestas DNS.
    Encabezados y metadatos de protocolos (HTTP headers, DHCP options, etc.)
    Concepto: aprovechar campos poco usados o extensibles de protocolos estándar para llevar datos encubiertos.


3.  Como defensor: ¿qué políticas y prácticas de seguridad (copias de seguridad, seg
    mentación, monitoreo, hardening, concientización) mitigarían la ocurrencia de este
    tipo de ataques?

    Como defensor lo más importante es concientizar a los usuarios sobre el internet y lo vulnerable que pueden llegar a estar en línea. Siempre se debe mantener el servicio de corta fuego activado y sobre todo debe estar siempre actualizado para gozar con lo último en seguridad que ofrece Microsoft, Apple o la empresa proveedora de S.O que use.
    
    Por parte del propio usuario; realizar copias de seguridad y realizar restauraciones del sistema cada cierto tiempo, asegurarse de la veracidad de los correos electrónicos, sobre todo si se es un trabajador de una empresa y el equipo tiene información sensible sobre esta. No estar conectados a redes publicas que expongan a atacantes si no se tiene contratado un servicio de VPN que te brinde seguridad.    

