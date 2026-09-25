# Validación

Las pruebas principales se hicieron en Linux con Python 3 y `psutil`.

- Monitor: consulta JSON y ruta inexistente.
- Red: DNS local, ping, TCP abierto y TCP cerrado.
- Seguridad: hash, cambio de archivo, contraseñas, logs y puertos locales.
- Bash: sintaxis, sistema, disco, memoria, procesos, red, ping y logs.
- Apache: configuración temporal, HTTP 200 y 404.
- Web: revisión en 1440, 768, 390 y 320 px.

Los repositorios separados conservan el código de cada herramienta. Repetir las pruebas desde cada repo si se modifica el script.

## Pendiente

No había Windows ni PowerShell en el entorno de trabajo. El toolkit de Windows debe probarse en una máquina Windows. Tampoco estaba instalado `traceroute`; el script informa ese caso.

No se probaron fallas físicas, memoria RAM, SMART de discos ni análisis de malware.
