# Bash Linux Toolkit

Consultas breves para administrar y diagnosticar Linux sin cambiar configuraciones. Tecnología: Bash y herramientas habituales del sistema.

## Requisitos e instalación

Linux con Bash 4+, `coreutils`, `procps`, `iproute2` y `iputils-ping`. Las consultas de servicios y logs requieren systemd (`systemctl` / `journalctl`); en contenedores o distribuciones sin systemd pueden no funcionar. En Debian/Ubuntu esos paquetes se pueden instalar con el gestor de paquetes si faltan. No requiere bibliotecas ni ejecutar como root.

Descargar el repositorio y abrir esta carpeta. Se ejecuta con `bash`, sin instalación del script.

## Uso y ejemplos

```bash
bash toolkit.sh system
bash toolkit.sh disk
bash toolkit.sh memory
bash toolkit.sh processes
bash toolkit.sh network
bash toolkit.sh ping 127.0.0.1
bash toolkit.sh service apache2
bash toolkit.sh logs
bash toolkit.sh logs apache2
```

`processes` muestra los 15 procesos con más porcentaje de memoria; el porcentaje de CPU de `ps` es un promedio durante la vida del proceso. `logs` limita la salida a 30 entradas; sin unidad selecciona advertencias y errores. Algunos registros sólo serán visibles para usuarios autorizados. No cambia permisos ni eleva privilegios automáticamente.

Si un servicio está inactivo, `systemctl` devuelve un código distinto de cero: también es información de diagnóstico. Si falta un comando, el script lo identifica. Un ping fallido no prueba que un equipo esté apagado: ICMP puede estar filtrado.

## Qué demuestra

Lectura de recursos y procesos, interfaces y rutas, comprobación de conectividad, estado de servicios, journal de systemd, validación de parámetros y uso de pipes. No reinicia servicios, borra archivos ni modifica la red.
