<!--
.. title: Evitando las malas prácticas en Python
.. slug: evitando-las-malas-practicas
.. date: 2018-02-21 22:57:25 UTC-03:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Abrunacci
-->

Cuando uno empieza a programar en Python suele suceder que incurrimos en errores que son considerados 
"leves" a nivel programación pero que a la hora de inspeccionar nuestro código y ver si cumple con las 
[reglas PEP8](https://www.fing.edu.uy/inco/cursos/fpr/wiki/index.php/Python_PEP8) nos encontramos con 
la sorpresa de que dudosamente una parte del código escrito logra aprobar el "examen".

A continuación un breve listado de cosas que podés estar haciendo mal sin saber.   

<div class="img-with-text" style="text-align:justify; width: 720px;">
    <img src="https://static.simpsonswiki.com/images/4/46/KnifeSafetyBook.png" alt="10 'SI' y 500 'NO' de la seguridad con las navajas" style="margin:0; display:block;"/>
    <p><code>No niego ni confirmo haber escrito este post solo para utlizar esta imágen.</code></p>
</div>



* ##*Real programmers don't use TABs*

   >O sí, pero decídanse por uno y sigan siempre con ese. 4 espacios o TABs, pero si vamos variando las indentaciones 
   de nuestros módulos con unos y otros, no estaríamos cumpliendo con las primeras dos reglas de PEP8
  
* ##*Respete los espacios*

   > Evite dejar espacios en blanco en las siguientes situaciones:	
      
      - Dentro de paréntesis curvos, llaves, o paréntesis rectos
      - Antes de una coma o punto y coma
      - Antes del paréntesis que abre la lista de argumentos en el llamado a una función
      - Más de un espacio alrededor de una asignación del operador para alinearlo con otro

   
* ##*79 Máxima*

   A la hora de codear en Python debemos tener en cuenta el largo de las líneas ya que, como bien lo dice [el zen de python](http://www.python.org.ar/wiki/PythonZen "El Zen de Python"),
   la legibilidad cuenta.
   
   Y para que podamos tener código mas legible, PEP8 recomienda que el máximo de caracteres por linea sean 79.
   
* ##*KISS*

   Keep it simple, ~~stupid~~ Sir.  
   
   > Las sentencias compuestas (varias instrucciones en la misma línea) son generalmente tomadas como malas prácticas de programación.

   Aunque a veces está bien poner if/for/while con una pequeña instrucción en la misma línea, no hacer esto para las declaraciones con múltiples instrucciones
   
* ##*Usted tiene 1934 actualizaciones pendientes...*

   El código debería estar comentado y que esos comentarios no contradigan lo que la función esta haciendo. 
   El código mal comentado es peor que el que no lo está. Procuren mantener actualizados los comentarios para que cualquiera
   que lo lea lo pueda interpretar correctamente y no tenga que adivinar qué es lo que hace cada función.
   
   

Eso es todo por ahora, más adelante subiré otros consejos sobre Python.

Saludos!
