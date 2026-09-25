# Guía breve de diagnóstico de PC

Guía de laboratorio y conversación técnica, no historial de reparaciones realizadas. El objetivo es reunir evidencia antes de cambiar componentes o configuración.

## 1. Delimitar el problema

Registrar el síntoma, cuándo empezó, qué estaba haciendo el usuario y si cambió algo recientemente. Identificar si ocurre siempre, sólo con una aplicación o sólo en una red. Evitar copiar datos personales al informe.

## 2. Comprobaciones físicas

Revisar alimentación, cables y periféricos externos. Ante olor a quemado, batería hinchada o ruido anormal, detener el uso y derivar la revisión. Antes de abrir un equipo: apagar, desconectar y seguir el procedimiento del fabricante y medidas antiestáticas. No abrir fuentes de alimentación.

## 3. Recursos y sistema

Ejecutar el monitor y anotar CPU, memoria, disco y uptime. Repetir durante el síntoma: un porcentaje aislado no identifica la causa. Usar el toolkit del sistema para consultar procesos y logs. Distinguir poco espacio libre de una falla física del disco: estas herramientas no leen SMART ni prueban la memoria RAM.

## 4. Red por etapas

1. Verificar que la interfaz esté activa y tenga IP.
2. Revisar ruta por defecto y conexión al gateway propio.
3. Comprobar resolución DNS del destino.
4. Probar el puerto TCP que usa el servicio.
5. Revisar traceroute si está disponible, sin interpretar un salto silencioso como falla definitiva.

Un ping exitoso no asegura que la aplicación funcione. DNS puede resolver correctamente aunque no haya un servicio escuchando.

## 5. Registrar y escalar

Anotar comandos, resultados relevantes y una hipótesis verificable. Antes de aplicar cambios, evaluar respaldo, permisos y cómo volver al estado anterior. Si el problema supera el alcance o afecta datos críticos, escalar con la evidencia obtenida.

### Ficha reutilizable

```text
Fecha / equipo (alias, sin datos privados):
Síntoma y pasos para reproducir:
Cambios recientes informados:
Comprobaciones realizadas:
Resultados:
Hipótesis y siguiente comprobación:
Acción autorizada / resultado / reversión:
```
