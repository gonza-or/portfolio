# Ver y publicar la web

## Vista local

Desde la raíz del repositorio:

```bash
python3 -m http.server 8000 --bind 127.0.0.1 --directory web
```

Abrir `http://127.0.0.1:8000` y detener con Ctrl+C. La web es HTML/CSS estático, sin compilación, JavaScript ni recursos externos. Los toolkits se ejecutan aparte, no desde el navegador. Publicar sólo `web/` evita servir scripts, documentación privada o metadatos de Git por accidente.

## GitHub Pages

El sitio se publica directamente desde la rama `main`, sin un workflow propio. La entrada [index.html](../index.html) redirige a `web/`; `.nojekyll` indica que no se necesita procesar Jekyll.

1. En el repositorio de GitHub, abrir **Settings → Pages**.
2. En **Build and deployment → Source**, seleccionar **Deploy from a branch**.
3. Elegir la rama **main**, carpeta **/ (root)**, y guardar.
4. Esperar el despliegue automático de Pages y abrir la URL indicada. Cada push a `main` vuelve a publicar.

La URL de entrada es `https://gonza-or.github.io/portfolio/`, que lleva a `https://gonza-or.github.io/portfolio/web/`. Las rutas de CSS e icono son relativas y funcionan en ese subdirectorio. Comprobar el despliegue antes de compartir la URL.

No hacen falta secretos personalizados ni permisos para subir workflows. Si no publica, revisar Settings → Pages y la ejecución administrada por GitHub en Actions. La publicación desde la raíz hace públicos los archivos versionados del repositorio; mantener datos privados, entornos virtuales y resultados fuera de Git.

Para hosting propio, ver [Apache](apache.md). No subir `.venv`, resultados locales ni credenciales.
