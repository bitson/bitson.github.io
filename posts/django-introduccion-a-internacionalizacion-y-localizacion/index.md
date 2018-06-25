<!--
.. title: Django: Introducción a internacionalización y localización
.. slug: django-introduccion-a-internacionalizacion-y-localizacion
.. date: 2018-06-18 22:02:41 UTC-03:00
.. tags: django, internationalization, localization, internacionalización, localización
.. category: django
.. link: 
.. description: Introducción a internacionalización y localización en Django
.. type: text
.. author: marcosdmyr
-->

# Django: Introducción a internacionalización y localización

Cuando escribimos código, solemos hacerlo por defecto en inglés, ya que es el lenguaje predominante. Sin embargo, sucede que en algunos casos los usuarios de nuestro desarrollo necesitan ver la aplicación en su lenguaje local y este no es el inglés. Este artículo no es más que una breve guía o bitácora de las acciones a seguir para conseguir aprovechar las capacidades de traducción de Django.

Particularmente los ejemplos serán en función de Django 2, y la documentación se encuentra disponible en el [sitio oficial](https://docs.djangoproject.com/en/2.0/topics/i18n/)

<!-- TEASER_END -->

Los pasos para conseguir traducir una aplicación web escrita en Django son los siguientes:

- [Configurar el sitio](#configuracion-del-sitio)
- [Marcar las cadenas de caracteres](#marcar-las-cadenas) (*Strings*) que deseamos que sean traducibles
- [Crear los archivos de traducción](#crear-archivos-de-traduccion) (*Archivos con extensión po*)
- [Compilar los mensajes](#compilar-los-mensajes) o cadenas de caracteres para que la aplicación pueda mostrarlos


Ahora, si te interesa abordar los fundamentos, de qué tratan estos dos conceptos comunes a casi cualquier framework moderno?

El objetivo de la internacionalización y localización es que una aplicación web disponga de contenido en lenguajes y formatos relacionados con sus usuarios.

En principio Django hace dos cosas:

- Permite a los desarrolladores *marcar* qué partes de la aplicación deberían ser traducibles o formateadas en lenguajes locales (**internacionalización**)
- Usa estas marcas para localizar la aplicación web en correspondencia con el usuario (**localización**)

*(Sólo a modo de aclaración, ya que evaluamos que los usuarios disponen de los navegadores de mayor uso. La intención de traducir a un lenguajes depende en última instancia de que el navegador acepte el header **Accpet-Language**)*


## Configuración del sitio {#configuracion-del-sitio}

Antes de empezar a traducir el sitio, debemos indicarle a Django qué lenguajes están disponibles, y cómo encontrar las traducciones. Estas dos cosas se hacen en el archivo de configuración **settings.py**.

Veamos como ejemplo, un sitio que queremos traducir al español.

```python
# The LocaleMiddleware check's the incoming request for the 
# user's preferred language settings. Add the LocaleMiddleware
# after SessionMiddleware and CacheMiddleware, and before the 
# CommonMiddleware.
MIDDLEWARE_CLASSES = (
   'django.contrib.sessions.middleware.SessionMiddleware',
   'django.middleware.locale.LocaleMiddleware',
   'django.middleware.common.CommonMiddleware',
)
# Provide a lists of languages which your site supports.
LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
)
# Set the default language for your site.
LANGUAGE_CODE = 'en'
# Tell Django where the project's translation files should be.
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
```

Si bien las instrucciones están documentadas a través de los comentarios, veamos los detalles:

- **LocalMiddleware** debe estar después de **SessionMiddleware** y antes de **SessionMiddleware**
- **LANGUAGES** es una tupla de tuplas, donde cada una indica el código del lenguaje y un nombre detallado
- **LANGUAGE_CODE** es el lenguaje por defecto en el sitio
- **LOCALE_PATH** es la ruta donde se encuentran los archivos de traducción


## Marcar las cadenas de caracteres {#marcar-las-cadenas}

En este punto, Django es capaz de determinar el lenguaje del usuario y ubicar los archivos de traducción. Para simplificar, siguiendo con el ejemplo de un sitio que queremos que esté disponible en español, veamos cómo marcar una cadena como traducible en un template.


```html
{% load i18n %}

<h1>{% trans 'Title' %}</h1>
```

En esta instancia estamos haciendo dos cosas:

- Indicamos que vamos a realizar trauducciones al incluir el tag *{% load i18n %}*. Esto se debe hacer al principio del arhivo, inclusive si el template extendie a otro que ya lo tiene.
- Además, marcamos la cadena **Title** como traducible


## Crear los archivos de traducción {#crear-archivos-de-traduccion}

En este paso, una vez que marcamos los textos a traducir, creamos los archivos de traducción desde la línea de comando de la siguiente manera:

```
> python manage.py makemessages -l 'es'
```

Esto sencillamente crea un archivo **.po** dentro de **locale**.

```
locale/
    es/
        LOCALE_MESSAGES/
            django.po
```


```
#: your-template-or-py-file:the-line-number
msgid "Title"
msgstr ""
```

Y después de actualizar el archivo .po:

```
#: your-template-or-py-file:the-line-number
msgid "Title"
msgstr "Título"
```


## Compilar las traducciones {#compilar-los-mensajes}

Como último paso, es necesario entender que Django buscará las traducciones en un archivo compilado con extensión **.mo**. Este archivo nuevamente lo generamos desde la línea de comando:

```
> python manage.py compilemessages
```

Podemos ver el nuevo archivo generado en la misma ruta que el correspondiente **.po**.

```
locale/
    es/
        LOCALE_MESSAGES/
            django.po
            django.mo
```

Una vez completado el primer paso, durante el proceso de traducción estaremos ciclando sobre el resto, es decir, marcando textos como traducibles, actualizando el **.po** y compilando las traducciones.

Finalmente, cualquier texto generado en Django tiene que ser traducible, por lo que sólo hace falta algo de paciencia para ver cuál es el lugar adecuado. Esta reseña tomó como ejemplo, una cadena en un template, pero también es posible traducir cualquier sección del administrador de Django.
