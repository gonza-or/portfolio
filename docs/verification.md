# Registro de validación

Validación realizada el 24 de septiembre de 2026 en Linux (Ubuntu), con Python 3 y psutil 7.1.0. Los resultados describen este entorno, no todas las combinaciones de hardware y sistema operativo.

## Pruebas ejecutadas

| Componente | Prueba | Resultado |
| --- | --- | --- |
| Python | `python3 -m unittest discover -s tests -v` | 13 pruebas correctas |
| Monitor | JSON real, rangos de métricas y ruta inexistente | Correcto; error controlado para ruta inexistente |
| Red | DNS localhost/IPv6, TCP con listener temporal y puerto sin listener | Correcto |
| Entradas | Puertos inválidos, intento de pasar opciones como host | Rechazados con salida 2 |
| Seguridad | Archivo mayor a 1 MiB, hash de referencia, modificación y hash inválido | Coincidencia y discrepancia detectadas |
| Contraseñas | Longitudes 12, 24, 128 y longitudes inválidas | Restricciones verificadas sin guardar contraseñas |
| Puertos locales | Listener temporal, rangos/host remoto y más de 20 entradas | Conexión local detectada; entradas no permitidas rechazadas |
| Logs | Archivo ficticio de cuatro líneas | Conteos esperados |
| Consultas locales | Conexiones y procesos del toolkit defensivo | Ejecutadas sin elevar privilegios |
| Bash | Sintaxis, sistema, disco, memoria, procesos, interfaces, ping IPv4/IPv6 | Correcto |
| systemd | Logs y consulta de un servicio inexistente | Lectura completada; código 4 para unidad inexistente |
| Apache 2.4 | Configuración temporal, HTTP en loopback | Sintaxis válida; página y CSS 200; ruta inexistente 404 |
| Web | Chromium a 1440, 768, 390 y 320 px | Cinco cards, enlaces internos válidos, sin desbordamiento de página |
| Accesibilidad | axe-core, reglas WCAG 2 A/AA y 2.1 AA | Sin infracciones automáticas en esos tamaños |
| Rutas | Destinos de GitHub en la web y enlaces relativos Markdown | Existen en el repositorio |
| Repositorio | Revisión de archivos versionados y patrones habituales de credenciales | Sin secretos detectados; sin entornos, dependencias ni informes locales versionados |

Las pruebas del navegador se ejecutaron con Playwright y axe-core instalados en una carpeta temporal fuera del repositorio. Se revisaron visualmente las [capturas de escritorio](../screenshots/web-1440.png) y [móvil](../screenshots/web-390.png). Un chequeo automático no sustituye la evaluación manual completa con lector de pantalla.

La instancia Apache de prueba usó un puerto alto local y archivos temporales, sin instalar ni modificar un servicio del sistema. No equivale a haber ejecutado todos los pasos administrativos de [apache.md](apache.md).

## Límites del entorno

- `traceroute` no estaba instalado. Se verificó el mensaje de herramienta ausente y salida 1; no se afirma haber probado una ruta real con esa utilidad. `tracert` requiere Windows.
- PowerShell y Windows no estaban disponibles. El script de Windows fue revisado, pero no se ejecutaron sus cmdlets ni un analizador PowerShell en este entorno.
- Las consultas de red se probaron en loopback. No se hicieron pruebas sobre equipos externos ni barridos de puertos.
- El monitor y los scripts Python se ejecutaron en Linux; su comportamiento en Windows debe verificarse allí.
- No se probaron memoria física, SMART de discos ni fallas reales de hardware.

## Comprobación pendiente en Windows

Abrir PowerShell en `projects/powershell-windows-toolkit` y ejecutar los ejemplos del README. Confirmar equipo, versión, CPU, RAM, discos, adaptadores/IP, procesos y servicios contra las herramientas del sistema. Para eventos, contrastar con el Visor de eventos; ausencia de coincidencias o falta de permisos puede generar un mensaje de consulta fallida.

Probar `Ping` con `127.0.0.1`. Para TCP, iniciar un servidor local de prueba en otra terminal (`py -m http.server 8000 --bind 127.0.0.1` desde `web/`), consultar `-Action TCP -TargetHost localhost -Port 8000` y detener el servidor. Repetir con el servidor detenido para observar `TcpTestSucceeded=False` y salida 1. Validar también `-TargetHost ::1` si IPv6 está habilitado.

Anotar versión de Windows/PowerShell, fecha y resultados antes de presentar esa ejecución como comprobada.
