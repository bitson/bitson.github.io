<!--
.. title: Debugueando react-native en Android
.. slug: debugueando-react-native-en-android
.. date: 2018-03-16 13:24:15 UTC-03:00
.. tags: react-native,android,javascript,react
.. author: D
.. category:
.. link:
.. description:
.. type: text
-->

En este post vamos a mostrar herramientas para debuguear la aplicacion que estemos desarrollando en react-native, igual que en mi post anterior voy a mostrar como hacerlo en linux.

## Requisitos

- Internet (claramente).
- Tener una aplicacion en react-native (de ser posible la del post anterior, paso el [link](http://blog.bitson.group/posts/empezando-con-android-y-react-native/)).
- Paciencia.

## Manos a la obra

Abrimos el Android Studio, vamos a `tools > AVD Manager` y corremos un emulador de Android.

Una vez que tengamos el emulador corriendo abrimos en una terminal el directorio donde tengamos nuestra app. En este caso seguimos usando la `rn-app` que hicimos el post anterior. Una vez en el directorio ejecutamos `npm run android`.

Una vez que la aplicacion se haya abierto en el emulador hacemos `ctrl + m` eso va a abrir una serie de opciones, ya iremos explicando una por una (aunque hayan opciones bastante obvias). Hacemos click en `Debug JS Remotely`.

Eso lo que va hacer es abrirnos una tab en chrome/firefox con una texto parecido a este:

```
React Native JS code runs as a web worker inside this tab.

Press Ctrl⇧J to open Developer Tools. Enable Pause On Caught Exceptions for a better debugging experience.

You may also install the standalone version of React Developer Tools to inspect the React component hierarchy, their props, and state.

Status: Debugger session #0 active.
```

Abrimos la consola del explorador con la tecla `F12` y vemos que dice

```
Running application "rnapp" with appParams: {"rootTag":11}. __DEV__ === true, development-level warning are ON, performance optimizations are OFF
```

Eso quiere decir que nuestro navegador ya esta "escuchando" a la aplicacion de react-native. Lo que podemos hacer para probarlo es ir al archivo `app.js` y dentro de la funcion `render()` hacer un simple `console.log('testing debug...');` eso se va a mostrar en la consola de su explorador.

Pero vamos un poco mas alla, creemos un boton y veamoslo funcionar un poco mas copado.

Vamos a poner un `Button` en nuestra app y ver por consola un mensaje que se escribe cuando hacemos click. En esta parte vamos a copiar y pegar el codigo, ya haremos un post explicando componentes y funciones.

```
import React from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';

export default class App extends React.Component {
    testDebug = () => {
        console.log('testing debug');
    }
  render() {
    return (
      <View style={styles.container}>
        <Text>Open up App.js to start working on your app!</Text>
        <Text>Changes you make will automatically reload.</Text>
        <Text>Shake your phone to open the developer menu.</Text>
            <Button
              onPress={this.testDebug}
              title="Press Me!"
              color="#841584"
              accessibilityLabel="Learn more about this purple button"
            />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
```

Simplemente lo que hace este mini codigo, es mostrar un mensaje en el press(click) del boton de nuestra app. Ahora cada vez que cliqueamos podemos ver por consola que se muestra un mensaje que dice `testing debug`.


## Otras herramientas

Contamos con una herramienta similar a la consola, pero que corre independientemente del navegador, [react-native-debugger](https://github.com/jhen0409/react-native-debugger).
Vamos a la parte de Installation al link que dice `releases`, y nos bajamos la version para linux.

Cerramos la tab donde estabamos debugueando anteriormente y volvemos a hacer `ctrl + M` para desactivar el `Debug JS Remotely`.
Vamos a la carpeta donde haya descargado, extraemos el zip y abrimos el archivo `React Native Debugger`. Vamos a ver que es similar al inspector de elementos de chrome. Repetimos los pasos pero con la aplicacion abierta y vemos que ahora el mensaje nos lo tira en la consola del `React Native Debugger`.
Lo que es interesante de esta aplicacion es que en el panel de abajo a la izquierda podemos ver el arbol del "DOM" (no es un DOM exactamente pero es simil) y podemos editar al vuelo las propiedades lo cual nos ahorra mucho tiempo de prueba y recarga.
Por ejemplo vayamos al `<Button>` dentro del explorador de elementos y cambiemos la propiedad `color` a `#333` veamos como el boton cambia de color, tambien podemos hacer "click" (press) y ver como nuestro mensaje sale por la consola.

Muy bien, ya tenemos la aplicacion instalada y las herramientas para debuguearla, FELICITACIONES!

<hr />

Gracias por leer, cualquier consulta la pueden dejar escrita en el blog y la contestamos.

Saludos,

D.
