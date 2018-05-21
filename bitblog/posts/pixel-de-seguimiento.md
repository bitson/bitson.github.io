<!--
.. title: Pixel de seguimiento
.. slug: pixel-de-seguimiento
.. date: 2018-05-21 15:34:00 UTC-03:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: @maleCuervo
-->

En este post vamos a mostrar como agregar un pixel de facebook y google analitycs a nuestro sitio web

¿que son y para que sirven los pixel de seguimiento?

Los pixel de seguimiento son una herramienta de analisis con la que podemos medir la eficacia de nuestras publicacones y entender las acciones que las personas realizan en nuestro sitio web.

...


#AGREGANDO PIXEL DE FACEBOOK

Agregar el pixel de facebook a nuestra web es relativamente sencillo, basta con seguir los pasos que estan en la propia documentación de facebook. Aqui les mostraremos ese paso a paso.

![imagen](/img/intro-pixel.png)

1 - vamos a la pestaña pixeles del administrador de anuncios, hacemos click en crear pixel e inmediatamente nos pide asiganrle un nombre identficador, en este caso nuestro pixel se llama bitson.

![imagen](/img/confi-pixel.png)

2 - Acontinuación ingresamos a las configraciones del pixel y hacemos click en "instala el código manualmente"

![imagen](/img/instalacion-manual.png)

3 - en este momento nos muestra la pantalla con los pasos para terminar la configración.
Seleccionamos el código que nos brinda la configuración y la pegamos en el encabezado de nuestras páginas a las que le haremos seguimiento.

![imagen](/img/script-facebook.png)





















#AGREGANDO PIXEL DE GOOGLE ANALYTICS

Para agregar el pixel de google analytics a nuestra web debemos acceder a google analytics https://developers.google.com/analytics/?hl=es-419 e ingresar en Configurar Google Analytics.

![imagen](/img/google-analytics.png)	

Cuando accedemos con esta opción, acontinuación nos muestra que configuración esta disponible para ser usada, en nuestro caso vamos a usar la opción gtag.js.

![imagen](/img/gtag.png)

Luego de esto, vamos a copiar y a pegar el siguiente código, despues de la etiqueta head en todas las paginas de tu sitio web.

![imagen](/img/script-google.png)




Esto es todo lo que necesitamos para realizar el seguimiento en nuestros sitios, controlando publicaciones e interacciones de nuestros visitantes, solo necesitamos hacer uso del código que nos brinda facebook y google analytics.
