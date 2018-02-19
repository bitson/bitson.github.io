<!--
.. title: Creando artículos en Nikola
.. slug: creando-articulos-en-nikola
.. date: 2018-02-16 16:10:50 UTC-03:00
.. tags: nikola, blog
.. category: 
.. link: 
.. description: Cómo crear un artículo para el blog de bitson con Nikola
.. type: text
.. author: @nespino
-->

Hoy les presentamos nuestro primer post recursivo. 

## Cómo crear un artículo para el blog de bitson



[logo-nikola]: https://getnikola.com/assets/img/logo.png "Logo de Nikola"

En esta oportunidad, vamos a hacerlo usando:

* [pipenv](https://github.com/pypa/pipenv "Repositorio de pipenv") (Para más información ver la guía [Empezando con pipenv](http://blog.bitson.group/posts/empezando-con-pipenv/ "Empezando con pipenv")
* [GitHub Pages](https://pages.github.com/ "Páginas de GitHub")
* [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet "Guía rápida de Markdown") como lenguaje de marcado 
* [![nikola logo][logo-nikola]](https://getnikola.com/ "Sitio oficial de Nikola")

Sin más preámbulo, dejo la receta a continuación... 


# Configurando el entorno pipenv

Primero, nos aseguramos de tener [pipenv instalado](https://bryson3gps.wordpress.com/2017/11/08/stop-everything-start-using-pipenv/ "Cómo instalar pipenv"). Resulta práctico disponer del comando pipenv desde cualquier ruta, por lo que sugerimos agregar la ubicación de la misma a la variable de entorno PATH en el archivo .bashrc (.zshrc, o el que corresponda al shell que usen). Para saber dónde está ubicado pipenv podemos ejecutar el siguiente comando desde la consola:

__which pipenv__

> /home/nespino/.local/bin/pipenv

Por lo que la línea de código para agregar pipenv al PATH sería: 

__export PATH=$PATH:~/.local/bin__ 


# Clonando nuestro repositorio de GitHub Pages

Una vez configurado el entorno pipenv, procedemos a clonar el [repositorio](https://github.com/bitson/bitson.github.io.git "Repositorio del blog de bitson") donde se alojan todas las entradas de nuestro blog.

__git clone https://github.com/bitson/bitson.github.io.git__

No necesitamos permisos especiales para clonarlo, pero no podremos subir el nuevo contenido del blog sin estar debidamente autorizado.

## IMPORTANTE

Debemos usar la rama __src__, en donde tenemos disponible los archivos necesarios para instalar Nikola y todas los artículos del blog.

__git checkout src__

# Instalando Nikola

Dentro del mismo, en la carpeta __bitblog__ se encuentra el archivo __Pipfile__, que es el que nos permitirá instalar [__Nikola__](https://getnikola.com/ "Sitio oficial de Nikola") a través del siguiente comando en consola:

__pipenv --three install__

El parámetro __--three__ indica que vamos a usar la versión 3 de Python. En caso de omitirlo, usaremos la versión que esté configurado por defecto en nuestro sistema. 

---
__Nota:__ Es posible las dependencias que tengamos en el sistema choquen con las que están declaradas en el archivo Pipfile.lock. En ese caso, podemos ignorar este archivo durante la instalación usando el comando:

__pipenv --three install --skip-lock__

---

__Otra nota:__

Es posible que el instalador de pipenv nos devuelva la siguiente advertencia:

> Warning: Your Pipfile requires python_version 3.6, but you are using 3.5.2 (/home/n/./b/bin/python).

>  $ pipenv check will surely fail.

No es algo de qué preocuparse.

---

### Instalación en curso...

>Virtualenv location: /home/nespino/.virtualenvs/bitblog-Dccxvb6W

>Installing dependencies from Pipfile...

> 🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 1/1 — 00:01:23

>To activate this project's virtualenv, run the following:

> $ pipenv shell

¡Éxito! Sólo nos falta verificar que Nikola esté funcionando correctamente. 

__pipenv run nikola auto__

En mi caso, al ejecutar ese comando recibo un Traceback que termina en

> OSError: [Errno 98] La dirección ya se está usando

Lo que significa que el puerto usado por defecto (8000) está ocupado. Para especificar el puerto a usar basta con agregar __-p <puerto>__ al final del comando. En el ejemplo, usaremos el puerto 8010.

> ➜  bitblog git:(src) ✗ pipenv run nikola auto -p 8010

> Scanning posts........done!

> [2018-02-16T20:03:24Z] INFO: auto: Watching files for changes...

> [2018-02-16T20:03:24Z] INFO: ws4py: Using epoll

> [2018-02-16T20:03:24Z] INFO: auto: Serving HTTP on 127.0.0.1 port 8010...

> [2018-02-16T20:03:24Z] INFO: ws4py: Managing websocket [Local => 127.0.0.1:8010 | Remote => 127.0.0.1:56708]

> [2018-02-16T20:03:24Z] INFO: auto: <--- {'command': 'hello', 'protocols': ['http://livereload.com/protocols/official-6', 'http://livereload.com/protocols/official-7'], 'snipver': 1, 'ver': '2.2.1'}

> [2018-02-16T20:03:24Z] INFO: auto: ---> {"command": "hello", "protocols": ["http://livereload.com/protocols/official-7"], "serverName": "nikola-livereload"}

> [2018-02-16T20:03:24Z] INFO: auto: <--- {'command': 'info', 'plugins': {'less': {'version': '1.0', 'disable': False}}, 'url': 'http://localhost:8010/'}

> [2018-02-16T20:03:24Z] INFO: auto: ****** Browser connected: http://localhost:8010/

> [2018-02-16T20:03:24Z] INFO: auto: ****** sending 0 pending messages


# Voilá!

Nikola está listo para ser usado. Para ver el estado actual del blog, ingresar a [http://localhost:8010/](http://localhost:8010/ "8010 o el puerto en el que esté corriendo Nikola") y buscar esta misma [entrada](http://blog.bitson.group/posts/creando-articulos-en-nikola/ "Haga clic aquí para sentir el efecto recursivo en tu propias venas"). Todo este procedimiento para llegar al tan deseado momento...

# Creando artículos en Nikola

Para crear una nueva entrada en el blog, nos posicionamos en el directorio __bitblog__ y ejecutamos:

__pipenv run nikola new_post -f markdown__

Sin desperdiciar un segundo, Nikola nos pedirá un título para el artículo...

>Creating New Post

>-----------------

>

>Title: Creando artículos en Nikola

>Scanning posts........done!

>[2018-02-16T19:10:50Z] INFO: new_post: Your post's text is at: posts/creando-articulos-en-nikola.md

>➜  bitblog git:(src) ✗ ls

---

Con el parámetro __-f markdown__ estamos especificando que el formato de marcado será [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet "Guía rápida de Markdown"). Si no lo especificamos, Nikola usará por defecto [reStructuredText](https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst "Guía rápida de reStructuredText). Al día de la fecha, [Nikola soporta](https://getnikola.com/handbook.html#id17 "Lista de lenguajes soportados por Nikola") reStructuredText, Markdown, Jupyter (IPython) Notebooks y HTML, entre otras. 

__Nota:__ El mismo [blog de Nikola creado con Nikola](https://getnikola.com/blog/ "Blog de Nikola") tiene una [nota](https://getnikola.com/blog/markdown-can-affect-performance.html "Nota sobre el rendimiento de Markdown") sobre el rendimiento del Markdown con respecto a otros lenguajes de formateo.

---

Estamos listos para redactar la publicación...
> __Your post's text is at: posts/creando-articulos-en-nikola.md__ 

 Abrimos el archivo que Nikola nos generó automáticamente y podemos ver que incluye un encabezado donde principalmente podemos:

* Cambiarle fecha y título a la entrada
* Agregarle tags separados por coma y definirle categorías
* Agregar una descripción
* Declarar quién es el autor

Para esto último, alcanza con agregar la línea __.. author: @nespino__ al final del encabezado. Lo que debería quedar algo similar a:

> <!--

> .. title: Creando artículos en Nikola

> .. slug: creando-articulos-en-nikola

> .. date: 2018-02-16 16:10:50 UTC-03:00

> .. tags: nikola, blog

> .. category: 

> .. link: 

> .. description: Cómo crear un artículo para el blog de bitson con Nikola

> .. type: text

> .. author: @nespino

> -->

> Escribe tu publicación aquí.


De acá en adelante es fácil. Escribimos la entrada y guardamos el archivo. 

__ INFO: auto: Watching files for changes...__

Nikola nos informa que cada vez que el contenido se modifique, el servidor local intentará reiniciar, reflejando los cambios en el navegador.

# Aplicando los cambios

Una vez que hayamos terminado de redactar la nota y verifiquemos que se vea correctamente, sólo debemos ejecutar el comando:

# pipenv run nikola github_deploy

lo que subirá los cambios al repositorio en la rama __src__ y GitHub Pages se encargará de mostrarlo en la dirección que tengamos configurada.



---

* PD: [guthub.com](http://guthub.com "GitHub mal escrito") redirecciona a [github.com](http://github.com "GitHub bien escrito") 

* PD2: pipenv --jumbotron 















 
