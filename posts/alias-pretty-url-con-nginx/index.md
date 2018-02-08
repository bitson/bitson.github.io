<!--
.. title: Alias & Pretty URL con Nginx
.. slug: alias-pretty-url-con-nginx
.. date: 2018-02-07 22:24:22 UTC-03:00
.. tags: devops, nginx, alias, deploy
.. category: tutorial, nginx, devops
.. link: 
.. description: Una breve descripción de configuración de Nginx
.. type: text
.. author: lecovi
-->

En este artículo te voy a contar cómo hacer para publicar en un mismo servidor
diferentes carpetas con archivos estáticos de tu sitio.

# Primer deploy

Supongamos que tenemos un sitio estático, por ejemplo, el sitio institucional
de [bitson](https://bitson.group). Eso lo tenemos en un repo y es un conjunto
de archivos de texto (HTML, js, css y demás) que conforman el sitio.

> Se le dice **estático** no porque esté *"quieto"* sino porque sólo contiene
> archivos de texto y no necesita correr un *backend* para funcionar.

Supongamos que tenemos los archivos en https://github.com/bitson/sitio1.git
clonamos el repo en el server y tendremos una configuración del Nginx que será
algo similar a:

```bash
server {
    listen 80;
    listen [::]:80;
    server_name bitson.group www.bitson.group;
    return 301 https://$host/$request_uri;
}
server {
    listen 443 ssl;
    listen [::]:443 ssl;

    root /home/bitson/sitio1;

    server_name bitson.group www.bitson.group;

    location / {
        try_files $uri $uri/ =404;
    }

    ssl_certificate         /etc/letsencrypt/live/bitson.group/fullchain.pem;
    ssl_certificate_key     /etc/letsencrypt/live/bitson.group/privkey.pem;
}
```

Esta configuración hace que todas las peticiones que lleguen vía HTTP sean
redireccionadas al HTTPS y se sirvan del directorio `/home/bitson/sitio1` donde
tenemos clonado el repo.

> Para los certificados usamos Let's Encrypt y esa es la ruta usual en donde
> se guardan en un sistema Debian.

Además en esta configuración vemos una sentencia de `try_files` para la
locación de la raíz (`/`). Lo que nos quiere decir esto es que cuando alquien
haga una petición a, por ejemplo: `bitson.group/saraza` Nginx tiene que buscar
si existe el archivo `/home/bitson/sitio1/saraza` o si existe el directorio
`/home/bitson/sitio1/saraza/`. En caso de que no exista ninguno entonces el
Nginx responderá con un 404, el código de HTTP que corresponde a `Not Found`.

# Agregando el alias

Supongamos ahora que tenemos otro repositorio, por ejemplo,
https://github.com/bitson/presentaciones.git y queremos publicarlo en el mismo
servidor. Algo así como lo que podemos ver en
[bitson.group/slides](https://bitson.group/slides/).

Para no tener que publicarlo en otro server, podemos aprovechar un alias de
Nginx. Suponiendo que tenemos ese repositorio en el server en
`/home/bitson/presentaciones` tenemos que poner una configuración como:

```bash
server {
    listen 443 ssl;
    listen [::]:443 ssl;

    root /home/bitson/sitio1;

    server_name bitson.group www.bitson.group;

    location / {
        try_files $uri $uri/ =404;
    }

    location /slides {
        alias /home/bitson/presentaciones;
    }

    ssl_certificate         /etc/letsencrypt/live/bitson.group/fullchain.pem;
    ssl_certificate_key     /etc/letsencrypt/live/bitson.group/privkey.pem;
}
```

# Pretty URLs

Si queremos omitir tener que poner el `.html` en cada una de las URLs a las que
queremos acceder en nuestro sitio. Sólo tenemos que agregar una sentencia de
`try_files` en nuestra configuración. Por ejemlo:

```bash
    location /slides {
        alias /home/bitson/presentaciones;
        try_files $uri $uri.html =404;
    }
```

Así, si queremos entrar a `https://bitson.group/slides/presentacion1.html`
podremos hacerlo con sólo ir a `https://bitson.group/slides/presentacion1`

----

Espero que les haya gustado! Los leemos en los comentarios!
