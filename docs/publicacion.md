# Ver y publicar la web

## Vista local

Desde la raíz del repositorio:

```bash
python3 -m http.server 8000 --bind 127.0.0.1 --directory web
```

Abrir `http://127.0.0.1:8000` y detener con Ctrl+C. La web es HTML/CSS estático, sin compilación, JavaScript ni recursos externos. Los toolkits se ejecutan aparte, no desde el navegador. Publicar sólo `web/` evita servir scripts, documentación privada o metadatos de Git por accidente.

## GitHub Pages

El workflow [pages.yml](../.github/workflows/pages.yml) publica el contenido de `web/` cuando hay un push a `main`.

1. En el repositorio de GitHub, abrir **Settings → Pages**.
2. En **Build and deployment → Source**, seleccionar **GitHub Actions**.
3. Ejecutar **Actions → Publish portfolio → Run workflow** si el primer push ocurrió antes de activar Pages.
4. Esperar la ejecución exitosa y abrir la URL indicada por el despliegue.

La URL esperada es `https://gonza-or.github.io/portfolio/`; no debe darse por publicada hasta comprobar el despliegue. Las rutas de CSS e icono son relativas y funcionan bajo `/portfolio/`.

Si falla `configure-pages`, verificar que Pages esté habilitado y que el repositorio tenga acceso a esa función. No hacen falta secretos personalizados: el workflow usa el token temporal de GitHub con permisos de Pages.

Para hosting propio, ver [Apache](apache.md). No subir `.venv`, resultados locales ni credenciales.
