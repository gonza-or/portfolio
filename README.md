# Gonzalo Ortiz · Portfolio técnico

Laboratorio personal preparado para una postulación a **Auxiliar de Informática**. Reúne una web estática y cinco herramientas pequeñas de consulta y diagnóstico, con código explícito y documentación en español.

El contenido es práctica de laboratorio: no representa experiencia laboral, certificaciones ni dominio avanzado. Las terminales de la web son ejemplos ilustrativos identificados, no capturas reales de herramientas.

## Proyectos

| Proyecto | Alcance | Tecnologías |
| --- | --- | --- |
| [System Monitor](projects/system-monitor/README.md) | CPU, RAM, disco, uptime e interfaces | Python, psutil |
| [Linux Toolkit](projects/bash-linux-toolkit/README.md) | Recursos, procesos, red, servicios y logs | Bash, utilidades Linux |
| [Windows Toolkit](projects/powershell-windows-toolkit/README.md) | Equipo, Windows, eventos y conectividad | PowerShell, CIM |
| [Network Diagnostics](projects/network-toolkit/README.md) | DNS, ping, interfaces, TCP y traceroute | Python, socket, psutil |
| [Defensive Security](projects/cybersecurity-toolkit/README.md) | SHA-256, contraseñas, puertos locales y logs | Python, hashlib, secrets, psutil |

## Ver la web

```bash
git clone https://github.com/gonza-or/portfolio.git
cd portfolio
python3 -m http.server 8000 --bind 127.0.0.1 --directory web
```

Abrir `http://127.0.0.1:8000`. No requiere npm, compilación ni backend. Ver [publicación con GitHub Pages](docs/publicacion.md) o [laboratorio de Apache](docs/apache.md).

Vista previa: [escritorio](screenshots/web-1440.png) · [móvil](screenshots/web-390.png).

## Ejecutar las herramientas Python

Con Python 3.10+ desde la raíz:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r projects/system-monitor/requirements.txt
python projects/system-monitor/monitor.py
python projects/network-toolkit/network.py dns localhost
python projects/cybersecurity-toolkit/security.py logs projects/cybersecurity-toolkit/sample.txt
```

Los tres proyectos usan la misma dependencia `psutil>=7.0,<8.0`; cada carpeta también tiene su archivo de requisitos para ejecutarla de forma independiente. En Windows crear el entorno con `py -m venv .venv` y activarlo con `.venv\Scripts\Activate.ps1`. Bash requiere Linux; PowerShell requiere Windows. Consultar los README individuales antes de ejecutar.

## Estructura

```text
portfolio/
├── web/                         # Sitio estático HTML/CSS
├── projects/
│   ├── system-monitor/
│   ├── bash-linux-toolkit/
│   ├── powershell-windows-toolkit/
│   ├── network-toolkit/
│   └── cybersecurity-toolkit/
├── docs/                        # Guías, pruebas y publicación
├── screenshots/                 # Capturas de la web, si están disponibles
├── tests/                       # Pruebas locales reproducibles
└── .github/workflows/pages.yml  # Publicación de web/ en Pages
```

## Validación y límites

El [registro de validación](docs/verification.md) indica las pruebas realizadas y qué queda por verificar en Windows. Para repetir las pruebas Python:

```bash
python -m unittest discover -s tests -v
bash -n projects/bash-linux-toolkit/toolkit.sh
```

Estas herramientas observan el estado del sistema: no reparan hardware, no reemplazan un antivirus ni constituyen una auditoría completa. Las consultas de red se usan sobre equipos propios o autorizados. Los informes pueden contener información privada y no se guardan automáticamente.

## Cuaderno técnico

- [Diagnóstico de PC](docs/diagnostico-pc.md): ordenar comprobaciones y registrar evidencia.
- [Apache](docs/apache.md): servir una web estática y revisar HTTP y logs.
- [Preparación para entrevista](docs/entrevista.md): conceptos y límites para explicar el código.

Contacto y otros repositorios: [github.com/gonza-or](https://github.com/gonza-or). La web usa este perfil como canal público de contacto; no incluye formularios que envíen o almacenen datos.
