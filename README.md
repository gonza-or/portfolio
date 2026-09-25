# Portfolio técnico

Portfolio de Gonzalo Ortiz para una postulación a Auxiliar de Informática.

Web: https://gonza-or.github.io/portfolio/web/

## Repositorios

- [Python System Monitor](https://github.com/gonza-or/python-system-monitor)
- [Bash Linux Toolkit](https://github.com/gonza-or/bash-linux-toolkit)
- [PowerShell Windows Toolkit](https://github.com/gonza-or/powershell-windows-toolkit)
- [Network Diagnostic Toolkit](https://github.com/gonza-or/network-diagnostic-toolkit)
- [Cybersecurity Toolkit](https://github.com/gonza-or/cybersecurity-toolkit)

Cada repositorio tiene su código y su README.

## Ver la web

```bash
git clone https://github.com/gonza-or/portfolio.git
cd portfolio
python3 -m http.server 8000 --bind 127.0.0.1 --directory web
```

Abrir `http://127.0.0.1:8000`.

La web es HTML y CSS. No usa npm ni backend.

## Estructura

```text
web/          sitio
docs/         guías
screenshots/  capturas
index.html    entrada de GitHub Pages
```

Los proyectos se mantienen en los repositorios separados. El contenido es práctica personal y no representa experiencia laboral ni certificaciones.

## Documentación

- [Diagnóstico de PC](docs/diagnostico-pc.md)
- [Apache](docs/apache.md)
- [Publicación](docs/publicacion.md)
- [Validación](docs/verification.md)
- [Entrevista](docs/entrevista.md)
