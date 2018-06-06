<!--
.. title: Usando Python en funciones de Postgresql
.. slug: usando-python-en-funciones-de-postgresql
.. date: 2018-06-05 23:57:46 UTC-03:00
.. tags: postgresql python functions sql bitson
.. category: Database tricks
.. link: 
.. description: Usando Python dentro de Postgresql
.. type: text
-->


Usando Python en funciones de Postgresql

Además de ser súper robusto a muy bajo costo, Postgresql, posee una muy buena característica, que es poder generar distintos tipos de funciones haciendo uso del lenguaje procedural, en este caso vamos a hablar de PL/Python, el cual, como pueden deducir por el titulpo del post, nos permite escribir codigo python dentro de las funciones.

En el post de hoy nos vamos a concentrar en dejar la extensión disponible para una base de datos en particular y también haremos un pequeño ejemplo de uso para poder sacarnos las ganas.
<!-- TEASER_END -->

#_Algunas cuestiones que debemos tener en cuenta:_

Si queremos utilizar explícitamente Python 2.7 (No entiendo bien porque alguien lo haría, pero lo explico igual)  debemos llamar a la extensión ‘plpython2u’
De igual manera, si queremos usar Python 3, debemos llamar a la extensión ‘plpython3u’ 

Por una cuestión de calendario (ya estamos en el 2018) y de sentido común (python 2 debe morir) nos vamos a focalizar en Python 3.

# Instalando...

Como primer paso, deberemos instalar el PLPythonu para dejarlo disponible en nuestra base de datos.

Lo instalamos con apt-get y definimos que motor de postgresql tenemos instalado, en mi caso uso Postgresql 9.6 así que instalo de la siguiente manera:

```SHELL
sudo apt-get install postgresql-plpython3-9.6
```

Nota: para saber la version instalada e postgres, desde una consola hacemos: 
```SQL
SELECT version();
```
# Preparando el entorno

Una vez instalada la extensión la dejamos disponible para nuestra base de datos, para ello lo hacemos asi:
‘CREATE EXTENSION plpython3u’

con eso deberia ser suficiente para generar una funcion en la base de datos que en su interior tenga codigo python.

# 1,2,3... Probando

Como prueba podemos usar la siguiente funcion:

```SQL
CREATE FUNCTION pymax (a integer, b integer)
  RETURNS integer
AS $$
  if (a is None) or (b is None):
    return None
  if a > b:
    return a
  return b
$$ LANGUAGE plpythonu;

-- Llamo a la función:
SELECT pymax(2, 3);
-- devuelve 3

```

#Referencias y algunos ejemplos mas:
- [Documentacion Oficial](https://www.postgresql.org/docs/9.6/static/plpython-funcs.html)
- [Pagina de Python Argentina](http://www.python.org.ar/wiki/PlPython)

