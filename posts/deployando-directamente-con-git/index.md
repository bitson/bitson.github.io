<!--
.. title: Deployando directamente con git
.. slug: deployando-directamente-con-git
.. date: 2018-02-07 22:52:17 UTC-03:00
.. tags: deploy, devops, git
.. category: devops, git
.. link: 
.. description: Tutorial sobre como deployar directamente con git
.. type: text
.. author: lecovi
-->

Hoy les quiero contar cómo se puede configurar `git` para que deployemos
directamente con un `push` en nuestro server.

# Entorno

Vamos a suponer que ya tenés tu sitio en un repositorio y que lo que estás
haciendo ahora en tu ciclo de *deploy* es algo similar a esto:

1. Hacés tus cambios en tu repo y commiteás a **master**.
2. Te conectás por `ssh` a tu server y te parás en el directorio donde tenés tu
   sitio
3. Hacés un `git pull` para descargar tu nuevo sitio.

Si bien no es algo complejo, puede llegar a ser medio tedioso. Y qué mejor si
se puede hacer un deploy simplemente haciendo `git push`, no? xD.

# Configuración

## Server

Vamos a suponer que estás sirviendo tus archivos con un Apache o un Nginx en el
directorio `/home/bitson/mi_sitio/`. 
Para poder llevar adelante esta configuración, vamos a separar por un lado los
archivos del sitio y por el otro los archivos del control de versiones.
Necesitamos tener un nuevo repo en `/home/bitson/mi_sitio.git`. Para eso nos
conectamos al server por ssh como siempre y ejecutamos:

```bash
mkdir -p /home/bitson/mi_sitio.git
cd /home/bitson/mi_sitio.git
git init --bare
```

> Con el parámetro `--bare` le decimos que no vamos a tener los archivos con
> código fuente, sólo los archivos *internos* de `git`.

### Hooks

Ahora que tenemos el repositorio creado, tenemos que tener un directorio
`hooks`. Ahí dentro vamos a crear un archivo que se llame `post-receive` con el
con permisos de ejecución siguiente contenido:

```bash
#!/bin/sh
git --work-tree=/home/bitson/mi_sitio --git-dir=/home/bitson/mi_sitio.git checkout -f 
```

> Para darle permisos de ejecución, corré el comando: `chmod a+x post-receive`

Ahora cuando hagamos un `push` a este repositorio en `mi_sitio.git` se va a
ejecutar el `hook` que acabamos de crear en `post-receive`.

## Máquina local

Ahora lo que tenés que hacer es agregar un repositorio remoto a tu repositorio
local: 

```bash
git remote add deploy ssh://usuario@tu_dominio.com/home/bitson/mi_sitio.git
```

Ahora trabajamos localmente y cuando queremos deployar lo que vamos a hacer es:

```bash
git push deploy master
```

Y *voilà!* Asunto resuelto.

# Limpieza

Si tu entorno era similar a lo que describimos al principio del artículo, si te
conectás al server, te parás en `/home/bitson/mi_sitio` y tirás un `git status`
te va a decir que hubo cambios. Porque claramente ese repositorio no sabe que
se actualizó... De hecho ya no necesitás tener ese repositorio porque los
archivos de `git` los tenés en `/home/bitson/mi_sitio.git`. 

Así que lo que podés hacer para evitar confusiones es borrar el `.git` que
tenés en `/home/bitson/mi_sitio`.

```bash
rm -rf /home/bitson/mi_sitio/.git
```

----

Fácil? Dejanos tu comentario
