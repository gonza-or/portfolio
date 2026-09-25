# Preparación para explicar el laboratorio

Leer y ejecutar cada proyecto antes de incluirlo en una entrevista. Presentarlo como práctica personal y explicar qué se verificó realmente; no afirmar dominio de una herramienta por tener un script.

| Proyecto | Pregunta para practicar | Punto que conviene entender |
| --- | --- | --- |
| Monitor | ¿Qué significa «Sin umbrales superados»? | Sólo CPU, RAM y disco bajo 90% en esa muestra; no garantiza salud del equipo. |
| Bash | ¿Por qué un servicio inactivo devuelve error? | El código de salida también comunica estado; no se reinicia el servicio. |
| PowerShell | ¿En qué se diferencia un pipeline de Bash? | Los cmdlets pasan objetos con propiedades; Bash normalmente pasa texto. |
| Redes | ¿Puede funcionar DNS y fallar TCP? | Sí: resolver un nombre no garantiza que el puerto acepte conexiones. |
| Seguridad | ¿Un hash coincidente prueba que un archivo es seguro? | Sólo prueba igualdad con la referencia; su procedencia importa. |
| Apache | ¿Qué hace DocumentRoot? | Define el directorio desde el que Apache sirve el sitio. |

Recorrido sugerido: mostrar un README, ejecutar una consulta, provocar un error controlado (ruta inexistente o puerto local sin servicio) y explicar el resultado. No mostrar salidas con datos privados ni contraseñas generadas.

Limitaciones que se pueden reconocer con claridad: no hay monitoreo histórico, reparación automática, análisis forense, pruebas de hardware ni detección de malware. Son herramientas pequeñas de observación y práctica.
