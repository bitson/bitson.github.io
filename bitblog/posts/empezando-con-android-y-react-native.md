<!--
.. title: Empezando con Android y React-Native
.. slug: empezando-con-android-y-react-native
.. date: 2018-02-27 18:43:18 UTC-03:00
.. author: D
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


En este post vamos a configurar el ambiente en linux para empezar a programar aplicaciones
en react-native para android (iOS queda fuera por razones obvias :grimacing:)

## Requisitos:

- Internet (claramente).
- Conocimientos minimos sobre variables de entorno (como setearlas).
- Paciencia.

## 1: Instalar Java


- Abrimos la terminal e instalamos java (version 8).

```
sudo apt-get update
sudo apt-get install openjdk-8-jdk
```

Una vez finalizado de instalar ejecutamos

`java -version`

Para ver si instalo correctamente y deberiamos ver algo similar a esto

```
openjdk version "1.8.0_151"
OpenJDK Runtime Environment (build 1.8.0_151-8u151-b12-1~deb9u1-b12)
OpenJDK 64-Bit Server VM (build 25.151-b12, mixed mode)
```

## 2: Descargar e Instalar Android Studio


Paso simple vamos a este [link](https://developer.android.com/studio/index.html?hl=es-419) y descargamos
Android Studio (for linux).
Una vez que lo bajamos, extraemos la carpeta en `/opt/` y dentro de la carpeta `android-studio` ejecutamos el archivo `studio.sh`.

Seleccionar la opcion que queramos si queremos importar configuraciones de instalaciones previas de Android Studio o no, click en OK.

Aca es donde deciamos que habia que tener paciencia, el wizard de instalacion de Android Studio te va a guiar el resto del proceso, el cual incluye la descarga del SDK (Software Development Kit), componentes que son necesarios para el desarrollo de apps. Parece que se va a trabar pero simplemente hay que esperar a que baje todos los archivos, va a depender mucho de tu velocidad de internet.

## 2.1: Librerias para PCs de 64-bit


Si tenes una pc con un SO de 64-bits tenes que instalarte estas librerias para poder trabajar.

```
sudo apt-get install libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 libbz2-1.0:i386
```



## 3: Descarga version de SDK en AS


Abrimos el android studio, creamos un proyecto (esto es obligatorio, pero no le den demasiada importancia no vamos a usarlo). Dejamos trabajar al IDE y en la consola vemos que nos va a pedir de updatar `gradle`, hacemos click e instalamos. Una vez terminado de instalar, vamos a `Tools > Android > SDK Manager` ahi vamos a seleccionar la version de Android con la que queremos trabajar (yo elijo la version 6 uds pueden elegir la que quieran). Despues vamos a la tab `SDK Tools` y nos fijamos que esten chequeadas las opciones `Android SDK Tools` y `Android SDK Platform-Tools` de no estarlas las chequeamos, e instalamos ambas o la que falte.

## 4: Variables de entorno


Vamos a setear las variables de entorno para "decirle" al sistema donde ir a buscar las SDK-Tools.
Abrimos la terminal y escribimos:

```
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

Si queres que queden fijas en la terminal modifica tu archivo `~/.bashrc` agregando esas 3 lineas al final y reiniciando la consola.
Para testear si expusimos bien las variables en una terminal ejecutamos el comando

`adb --version`

El comando adb es una herramienta dentro de los SDK-Tools simplemente vamos a ver si encuentra ese archivo pidiendole la version, la salida deberia verse parecida a esta:

```
Android Debug Bridge version 1.0.39
Version 0.0.1-4500957
Installed as /home/{USER}/Android/Sdk/platform-tools/adb
```

## 5: Android Virtual Device Manager


El Android Studio cuenta con un emulador de android que podemos ejecutar en la PC, muy util para desarrollar y debuguear. Dentro del AS vamos a `Tools > Android > AVD Manager` y cliqueamos `Create Virtual Device` esto va a crear un nuevo emulador, seleccionan el tipo de dispositivo que quieren, la version de Android (instalada previamente en el paso 3). Una vez creada van a ver en la lista de dispositivos que se encuentra el suyo y a la derecha dentro de la columna `Actions` hay un boton de play que les permite ejecutarla.

## 5.1: Detalle sobre AVD


El emulador consume mucha RAM, lo cual va a ser que se realentice el proceso de buildear y de ejecutar la aplicacion, tambien presenta problemas en placas de video. Por ejemplo yo tengo una placa nVidia y para poder correr el AVD en mi maquina tuve que instalarme los drivers de linux de lo contrario el emulador abria y cerraba automaticamente. Les dejo el [link](https://wiki.debian.org/es/NvidiaGraphicsDrivers) para instalar los drivers de nVidia en debian, para los drivers de otras placas de video consulten con nuestro buen amigo google.

## 6: Node.js & npm


Ya tenemos instalado y corriendo nuestro emulador de android en nuestra pc ahora bien la pregunta del millon...Como arrancamos a programar?
Simple, tenemos que bajarnos (para variar) `nodejs` y `npm`, son programas que nos van a permitir compilar nuestro codigo en JS y ejecutarlo como si fuera nativo, manos a la obra!
Para node vamos a la terminal de linux y ejecutamos:

```
curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -
sudo apt-get install -y nodejs
```

Eso basta para tener `node` y `npm` (node package manager) instalados en tu PC, para comprobarlo hacemos
`node -v && npm -v`

La salida deberia ser similar a:
```
v6.13.0
3.10.10
```

## 7: create-react-native-app


Muy bien, continuando con nuestro brevisimo post, en la terminal hacemos un `sudo npm i -g create-react-native-app` lo cual va a instalar un paquete de node de forma global (por eso sudo y por eso -g), para facilitarnos la creacion desde 0 de un proyecto en react native, dejo el [link](https://github.com/react-community/create-react-native-app) para que puedan ver el readme e interiorizarse mas si quieren.

## 8: Ejecucion


Una vez instalado el paquete vamos al destino donde querramos instalar el proyecto y en una terminal hacemos `create-react-native-app rn-app` eso nos va a crear una app llamada rn-app (uds le pueden poner el nombre que quieran). Va a tardar un rato (otra vez), pero una vez que termine ya estamos listos para trabajar. Entramos a la carpeta `cd rn-app` y ejecutamos `npm start` en una consola y en otra `npm run android` si tenemos el emulador abierto la aplicacion se va a ejecutar en el mismo, sino va a fallar y salir.

## 8.1: Ejecucion en dispositivo


Para este paso vamos a necesitar un cable usb y un celular (con android obviamente).
Vamos a habilitar el debug con USB en el celular, para eso hay que tener las opciones de desarrollador activadas, eso lo hacemos yendo a `Configuracion > Acerca de` y cliqueamos el numero de build 7 veces, despues volvemos a configuracion y vamos a tener las `Opciones de Desarrollador`, entramos y habilitamos el "Debug por USB".

Enchufamos el celular a la computadora y seleccionamos la opcion de transferir fotos via PTP.

En la terminal ejecutamos `lsusb` y obtenemos algo similar a esto:
```
Bus 002 Device 007: ID 1004:631d LG Electronics, Inc. Optimus Android Phone (Camera/PTP Mode)
Bus 002 Device 003: ID 1a81:1006 Holtek Semiconductor, Inc.
Bus 002 Device 002: ID 8087:0020 Intel Corp. Integrated Rate Matching Hub
Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 003: ID 04f2:b1d6 Chicony Electronics Co., Ltd CNF9055 Toshiba Webcam
Bus 001 Device 002: ID 8087:0020 Intel Corp. Integrated Rate Matching Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

```

Esta claro que mi celular es:

`ID 1004:631d LG Electronics, Inc. Optimus Android Phone (Camera/PTP Mode)`

De la linea de arriba agarramos los primeros 4 digitos del dispositivo:

`1004:631d`

En este caso `1004` es el identificador para LG.

Ingresamos lo siguiente en la consola:
```
echo SUBSYSTEM=="usb", ATTR{idVendor}=="22b8", MODE="0666", GROUP="plugdev" | sudo tee /etc/udev/rules.d/51-android-usb.rules
```

Por ultimo hacemos un check para ver si el adb lo detecta en la consola:

`adb devices`

Y deberiamos ver algo similar (depende del dispositivo que tengan)

```
List of devices attached
LGD62093133844	device
```
Ahora puden hacer en la carpeta de su `rn-app` `npm run android` y la aplicacion se va a abrir en su celular. COPADO!

<hr />

Gracias por leer, cualquier consulta la pueden dejar escrita en el blog y la contestamos.

Saludos,

D.

<hr />
Fuentes y ayudas:

- [Establishing a build enviorment](https://source.android.com/setup/initializing)
- [Install android studio](https://developer.android.com/studio/install.html)
- [Este link de stackoferflow](https://stackoverflow.com/questions/26256279/how-to-set-android-home-path-in-ubuntu-please-provide-the-steps)
- [Instalar node](https://nodejs.org/es/download/package-manager/#distribuciones-de-linux-basadas-en-debian-y-ubuntu)
