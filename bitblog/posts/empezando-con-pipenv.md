<!--
.. title: Empezando con Pipenv
.. slug: empezando-con-pipenv
.. date: 2018-01-31 12:26:18 UTC-03:00
.. tags: python pipenv virtualenv
.. category: dev python
.. link: 
.. description: Introducción a Pipenv
.. type: text
.. author: lecovi 
-->

En este brevísimo artículo te explicamos cómo empezar a usar `pipenv`.

# Instalado Pipenv

`pipenv` es una herramienta para manejar paquetes y entornos virtuales de
manera sencilla en tu entorno de desarrollo. Te recomiendo que le eches un ojo
a la [Documentacion Oficila](http://pipenv.readthedocs.io/en/latest/).
Ahora te voy a mostrar cómo instalar `pipenv` y cómo usarlo en tus proyectos.

<!-- TEASER_END -->

## Instalar Pipenv

La forma más fácil de instalar `pipenv` es a través de `pipsi`. Si no tenés
`pipsi` instalado, lo podés instalar con:

```bash
$ curl https://raw.githubusercontent.com/mitsuhiko/pipsi/master/get-pipsi.py | python3
```
Para poder ejecutar desde la línea de comandos tenés que agregar a tu variable
de entorno `PATH` la ruta donde está el ejecutable de `pipsi`.

Con `bash`:
```bash
export PATH=$PATH:~/.local/bin/pipsi
```
Con `fish`:
```fish
set PATH $PATH ~/.local/bin/pipsi
```

Y después tenés que instalar `pew` y `pipenv`:

```bash
$ pipsi install pew
$ pipsi install pipenv
```

### Comandos útiles

- `pipenv --three install <paquete>`: instala <paquete> en el virtualenv.
- `pipenv --three install -r <archivo_de_requerimientos>`: instala los requerimientos en el virtualenv.
- `pipenv shell`: activa el virtualenv en la shell.
- `pipenv run <archivo>`: ejecuta <archivo> desde el virtualenv.
- `pipenv --rm`: borra el virtualenv.
- `pipenv --update`: actualiza `pip` & `pipenv`.
- `pipenv --venv`: muestra el PATH del virtualenv.
