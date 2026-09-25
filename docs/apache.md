# Servir la web con Apache

Ejemplo para Debian o Ubuntu.

```bash
sudo apt install apache2
sudo install -d -m 755 /var/www/portfolio
sudo cp web/index.html web/styles.css web/favicon.svg /var/www/portfolio/
```

Crear `/etc/apache2/sites-available/portfolio.conf`:

```apache
<VirtualHost *:80>
    ServerName portfolio.local
    DocumentRoot /var/www/portfolio

    <Directory /var/www/portfolio>
        Options -Indexes
        AllowOverride None
        Require all granted
    </Directory>
</VirtualHost>
```

Activar y revisar:

```bash
sudo a2ensite portfolio.conf
sudo apache2ctl configtest
sudo systemctl reload apache2
curl -I -H 'Host: portfolio.local' http://127.0.0.1/
```

Si devuelve `Syntax OK` y HTTP 200, Apache está sirviendo la página. Los logs suelen estar en `/var/log/apache2/`.

Para usar el nombre local, agregar `127.0.0.1 portfolio.local` a `/etc/hosts`. No borrar otros sitios ni usar `chmod 777`.
