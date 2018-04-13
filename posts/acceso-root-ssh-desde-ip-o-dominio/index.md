<!--
.. title: Acceso root SSH desde IP o dominio
.. slug: acceso-root-ssh-desde-ip-o-dominio
.. date: 2018-04-13 10:15:07 UTC-03:00
.. tags: devops ssh root
.. category: tutorial ssh
.. link:
.. description: accediendo por SSH como root desde una IP o dominio.
.. type: text
.. author: lecovi
-->

Hace poco con la coope nos mudamos y tuvimos que cambiar el ISP (*Internet
Service Provider*) y eso motivó a que tuviéramos que hacer algunos cambios, en
muchos aspectos pero no viene al caso, puntualmente en el server que tenemos
dentro de la ofi.
Tuve que desempastarme un poco y volver a leer el manual de **ssh** para
recordar algunas cuestiones que les comparto a continuación.

# Archivo de configuración

El *daemon* de SSH lee el archivo de configuración que está en
`/etc/ssh/sshd_config`. Este archivo tiene muchíiiiiiiisimas opciones de
configuración.

## Match

Lo interesante de este archivo de configuración es que acepta configuraciones
condicionales. Es decir, si se cumple una condición específica, se modifican
las opciones de configuración en cuestión.

Por ejemplo, es normal no permitir el acceso SSH como root desde cualquier
lado. En Debian, cuando instalás el servidor SSH es una opción por defecto.
Sólo podés acceder por SSH a la máquina con un usuario sin privilegios.

Pero podrías querer entrar por ejemplo desde una máquina local. Para eso usamos
las opciones de configuración condicionales.

```
Match Address 192.168.1.50
    PermitRootLogin yes
```

En este caso, lo que estamos indicando es que si el acceso SSH proviene desde
la IP 192.168.1.50 dejamos que se acceda como el usuario root. Esto es muy
útil para cuando queremos configurar acceso rápido desde máquinas "confiables".
Es decir, terminales que nosotros solemos utilizar, son de nuestra propiedad o
resultan conocidas.

También existe la posibilidad de asignarlo a través de un dominio. En cuyo caso
la opción de configuración será:

```
Match Host foo.bitson.group
    PermitRootLogin yes
```

Sólo nos resta reiniciar el servicio de SSH para que el *daemon* tome los
cambios.

```
systemctl restart ssh
```

Espero que les haya sido útil. Nos vemos en la próxima!

### Enlaces de interés

- [Manual Config SSH](https://linux.die.net/man/5/sshd_config)
- [How to allow root login from one IP address with ssh public keys only](https://www.cyberciti.biz/faq/match-address-sshd_config-allow-root-loginfrom-one_ip_address-on-linux-unix/)
- [Allow SSH Root Login From Specific IP](https://stackpointer.io/unix/linux-allow-ssh-root-login-specific-ip/618/)
