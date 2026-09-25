# Cybersecurity Toolkit

Utilidades de seguridad defensiva: SHA-256, comparación de integridad, contraseñas con `secrets`, comprobación de puertos locales explícitos y lectura de procesos, conexiones y logs. Python 3.10+, biblioteca estándar y `psutil`; Linux y Windows.

## Instalación

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

En Windows: `py -m venv .venv` y `.venv\Scripts\Activate.ps1`.

## Uso y ejemplos

```bash
python security.py hash sample.txt
python security.py password --length 24
python security.py ports 80 443
python security.py connections
python security.py processes
python security.py system
python security.py logs sample.txt
```

`sample.txt` contiene registros ficticios. El análisis cuenta líneas que contienen las palabras completas `error`, `warning`, `failed` o `denied`, sin distinguir mayúsculas. Una misma línea puede coincidir con varias categorías. No detecta incidentes ni reemplaza una revisión del contexto; lee archivos de texto, no archivos binarios EVTX.

Para comprobar integridad, copiar un SHA-256 de una fuente confiable y pasarlo como segundo argumento de `verify`:

```bash
python security.py verify sample.txt HASH_ESPERADO_DE_64_CARACTERES
```

Ese último argumento es un marcador, debe reemplazarse. Una coincidencia indica igualdad con el hash esperado; no prueba que el archivo sea seguro ni auténtico si la referencia no es confiable. Los archivos se leen en bloques de 1 MiB.

Las contraseñas tienen entre 12 y 128 caracteres e incluyen minúsculas, mayúsculas, dígitos y símbolos. Se imprimen en la terminal, no se guardan: evitar grabar o compartir esa salida. `secrets` usa la fuente aleatoria criptográfica del sistema.

`ports` comprueba únicamente `127.0.0.1` y `::1`, hasta 20 puertos indicados explícitamente, con un segundo de espera por conexión. Un resultado negativo puede deberse a rechazo, timeout o IPv6 no disponible. No comprueba exposición desde otras redes ni servicios enlazados sólo a otra interfaz. No acepta hosts remotos, rangos ni autodetección. Su salida 0 significa que terminó la revisión, aunque haya puertos sin conexión.

Las listas de procesos y conexiones pueden ser parciales por permisos; no se elevan privilegios. No se muestran argumentos de procesos para reducir la exposición accidental de datos. Antes de compartir salidas, quitar nombres de equipos, IP y datos privados.

## Qué demuestra

Integridad, hashes, aleatoriedad segura, sockets locales, permisos de lectura, inventario de procesos y análisis simple de texto. No contiene explotación, persistencia, evasión ni cambios en el sistema. Salida 1 indica error o hash distinto; 2 indica argumentos inválidos.
