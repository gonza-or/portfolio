# Portfolio técnico — Gonzalo Ortiz

Portfolio personal estático, compatible con GitHub Pages. Está construido únicamente con HTML y CSS, usando como base visual el tema [Minimal de orderedlist](https://github.com/orderedlist/minimal), sin frameworks ni dependencias externas.

## Ejecutar localmente

Desde la raíz del repositorio:

```bash
python3 -m http.server 8000
```

Abrir <http://localhost:8000> en el navegador.

## Modificar el contenido

- Editar `index.html` para cambiar textos, proyectos, formación y enlaces.
- Editar `stylesheets/styles.css` para ajustar colores, tipografía o distribución.
- Reemplazar los enlaces que contienen `REEMPLAZAR_` en la sección de contacto.
- `_config.yml` contiene la configuración mínima de GitHub Pages/Jekyll.

## Publicar con GitHub Pages

1. Subir los cambios a la rama `main`.
2. En GitHub, abrir **Settings → Pages**.
3. En **Build and deployment**, elegir **Deploy from a branch**.
4. Seleccionar `main` y la carpeta `/ (root)`, y guardar.

La dirección esperada es <https://gonza-or.github.io/portfolio/>.
