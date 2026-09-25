# Publicar la web

## Probarla localmente

Desde la raíz:

```bash
python3 -m http.server 8000 --bind 127.0.0.1 --directory web
```

Abrir `http://127.0.0.1:8000` y detener con Ctrl+C.

## GitHub Pages

El repositorio se publica desde `main`, carpeta `/ (root)`. `index.html` redirige a `web/`.

La dirección es:

https://gonza-or.github.io/portfolio/web/

En GitHub: **Settings → Pages → Deploy from a branch → main → / (root)**.

## Apache

Para servirla con Apache, ver [apache.md](apache.md). No copiar `.git`, entornos virtuales ni credenciales al directorio público.
