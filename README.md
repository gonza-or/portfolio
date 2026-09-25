# Gonzalo Ortiz · Portfolio técnico

Laboratorio personal preparado para una postulación a **Auxiliar de Informática**. Reúne una web estática y cinco herramientas pequeñas de consulta y diagnóstico, con código explícito y documentación en español.

[Ver portfolio en GitHub Pages](https://gonza-or.github.io/portfolio/web/) · [Perfil de GitHub](https://github.com/gonza-or)

El contenido es práctica de laboratorio: no representa experiencia laboral, certificaciones ni dominio avanzado. Las terminales de la web son ejemplos ilustrativos identificados, no capturas reales de herramientas.

## Proyectos

| Proyecto | Alcance | Tecnologías |
| --- | --- | --- |
| [System Monitor](https://github.com/gonza-or/python-system-monitor) | CPU, RAM, disco, uptime e interfaces | Python, psutil |
| [Linux Toolkit](https://github.com/gonza-or/bash-linux-toolkit) | Recursos, procesos, red, servicios y logs | Bash, utilidades Linux |
| [Windows Toolkit](https://github.com/gonza-or/powershell-windows-toolkit) | Equipo, Windows, eventos y conectividad | PowerShell, CIM |
| [Network Diagnostics](https://github.com/gonza-or/network-diagnostic-toolkit) | DNS, ping, interfaces, TCP y traceroute | Python, socket, psutil |
| [Defensive Security](https://github.com/gonza-or/cybersecurity-toolkit) | SHA-256, contraseñas, puertos locales y logs | Python, hashlib, secrets, psutil |

## Ver la web

```bash
git clone https://github.com/gonza-or/portfolio.git
cd portfolio
python3 -m http.server 8000 --bind 127.0.0.1 --directory web
```

Abrir `http://127.0.0.1:8000`. No requiere npm, compilación ni backend. Ver [publicación con GitHub Pages](docs/publicacion.md) o [laboratorio de Apache](docs/apache.md).

Vista previa: [escritorio](screenshots/web-1440.png) · [móvil](screenshots/web-390.png).

## Clonar y ejecutar una herramienta

Con Python 3.10+ desde la raíz:

Cada proyecto independiente contiene su propio README y requisitos. Por ejemplo:

```bash
git clone https://github.com/gonza-or/python-system-monitor.git
cd python-system-monitor
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python monitor.py
```

Los proyectos Python usan `psutil>=7.0,<8.0`. En Windows crear el entorno con `py -m venv .venv` y activarlo con `.venv\Scripts\Activate.ps1`. Bash requiere Linux; PowerShell requiere Windows. Consultar el README de cada repositorio antes de ejecutar.

## Estructura

```text
portfolio/
├── web/                         # Sitio estático HTML/CSS
├── docs/                        # Guías, pruebas y publicación
├── screenshots/                 # Capturas de la web, si están disponibles
├── index.html                   # Entrada de Pages: redirige a web/
└── .nojekyll                    # Publicación estática sin Jekyll
```

## Validación y límites

El [registro de validación](docs/verification.md) indica las pruebas realizadas y qué queda por verificar en Windows. Para repetir las pruebas Python:

Cada repositorio independiente conserva su código y README. Las pruebas históricas del conjunto se ejecutaron antes de la separación; las validaciones específicas se deben repetir desde el repositorio de cada herramienta.

Estas herramientas observan el estado del sistema: no reparan hardware, no reemplazan un antivirus ni constituyen una auditoría completa. Las consultas de red se usan sobre equipos propios o autorizados. Los informes pueden contener información privada y no se guardan automáticamente.

## Cuaderno técnico

- [Diagnóstico de PC](docs/diagnostico-pc.md): ordenar comprobaciones y registrar evidencia.
- [Apache](docs/apache.md): servir una web estática y revisar HTTP y logs.
- [Preparación para entrevista](docs/entrevista.md): conceptos y límites para explicar el código.

La carpeta `portfolio` funciona como índice y web publicada; el código ejecutable vive en los cinco repositorios enlazados arriba.

Contacto y otros repositorios: [github.com/gonza-or](https://github.com/gonza-or). La web usa este perfil como canal público de contacto; no incluye formularios que envíen o almacenen datos.
