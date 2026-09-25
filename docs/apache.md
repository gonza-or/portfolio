# Servir el portfolio con Apache

Práctica para Debian/Ubuntu. Objetivo: relacionar un directorio de archivos estáticos con un VirtualHost y comprobar HTTP y logs. No requiere PHP, base de datos ni Node.js. La instalación y activación son pasos manuales para una máquina de laboratorio; no se ejecutan desde los toolkits.

## Preparar los archivos

Desde la raíz del repositorio, en una máquina donde tengas autorización para administrar Apache:

```bash
sudo apt install apache2
sudo install -d -m 755 /var/www/portfolio
sudo cp web/index.html web/styles.css web/favicon.svg /var/www/portfolio/
sudo chmod 644 /var/www/portfolio/index.html /var/www/portfolio/styles.css /var/www/portfolio/favicon.svg
```

Revisar primero que `/var/www/portfolio` no contenga otra web: la copia reemplaza esos tres archivos si existen. El servidor sólo necesita leerlos; no se usa `chmod 777` ni se copia el repositorio entero al directorio público.

## Configuración

Crear `/etc/apache2/sites-available/portfolio.conf` con:

```apache
<VirtualHost *:80>
    ServerName portfolio.local
    DocumentRoot /var/www/portfolio

    <Directory /var/www/portfolio>
        Options -Indexes
        AllowOverride None
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/portfolio-error.log
    CustomLog ${APACHE_LOG_DIR}/portfolio-access.log combined
</VirtualHost>
```

Validar y activar:

```bash
sudo a2ensite portfolio.conf
sudo apache2ctl configtest
```

Sólo si devuelve `Syntax OK`:

```bash
sudo systemctl reload apache2
curl -I -H 'Host: portfolio.local' http://127.0.0.1/
systemctl status apache2 --no-pager
```

Para navegar con ese nombre local, agregar manualmente `127.0.0.1 portfolio.local` a `/etc/hosts`, conservando las entradas existentes. No deshabilitar otros sitios para esta práctica. HTTP local no proporciona cifrado; una publicación pública debe usar HTTPS, por ejemplo mediante GitHub Pages.

## Comprobaciones

- HTTP 200 en `/`, `/styles.css` y `/favicon.svg`.
- Un recurso inexistente responde 404.
- Revisar `/var/log/apache2/portfolio-access.log` y `portfolio-error.log` con los permisos correspondientes.
- Si no conecta, revisar servicio, puerto de escucha y dirección; si responde otro sitio, comprobar `ServerName` y la cabecera Host.

Para desactivar sólo esta práctica: `sudo a2dissite portfolio.conf`, validar con `sudo apache2ctl configtest` y, si es correcto, recargar Apache. No borrar los archivos de otros sitios.

La [validación del repositorio](verification.md) distingue la prueba HTTP local realizada de la instalación manual con systemd descrita aquí.
