# CLASE 01 MIÉRCOLES 14 DE AGOSTO DEL 2024 - Portafolio 1

**USO DE GITHUB Parte 1**

GitHub es una plataforma que nos permite guardar repositorios de Git que podemos usar como servidores remotos y ejecutar algunos comandos de forma visual e interactiva (sin necesidad de la consola de comandos).

Luego de crear nuestra cuenta, podemos crear o importar repositorios, crear organizaciones y proyectos de trabajo, descubrir repositorios de otras personas, contribuir a esos proyectos, dar estrellas y muchas otras cosas.

**COMANDOS**

```sh
Import repository, New repository, New organization: #significa que es como tu empresa, New project: significa es como un grupo de repositorios que puedes tener dentro de una empresa, New gist: es un pedasito de código que puedes compartir

New repository #Ponemos el nombre: class-git, descripción: Haremos un blog increible, hay muchas licencias para publicar el código: NO lo hacemos ahora.

Create repository #Lo ponemos en privado o en Publico.
```

El ***README.md*** es el archivo que veremos por defecto al entrar a un repositorio. *Es una muy buena práctica configurarlo para describir el proyecto, los requerimientos y las instrucciones que debemos seguir para contribuir correctamente.*

Para clonar un repositorio desde GitHub (o cualquier otro servidor remoto) debemos copiar la URL (por ahora, usando HTTPS) y ejecutar el comando git clone + la URL que acabamos de copiar. Esto descargará la versión de nuestro proyecto que se encuentra en GitHub.

>ATENCIÓN: ¿Por qué? Porque a través de https nos pedirá usuario(nombre perfil) y contraseña.
Sin embargo, esto solo funciona para las personas que quieren empezar a contribuir en el proyecto.

**Cómo conectar un repositorio de GitHub** a nuestro documento local Si queremos conectar el repositorio de GitHub con nuestro repositorio local, que creamos aconsejo que al trabajar desde GitHub no utilizemos localmente el comando git init, si debemos ejecutar las siguientes instrucciones:

```sh
## Guardar la URL del repositorio de GitHub con el nombre de origin

$ git remote add origin URL

## Verificar que la URL se haya guardado correctamente:

$ git remote

$ git remote -v

## Traer la versión del repositorio remoto y hacer merge para crear un commit con los archivos de ambas partes. 

#Podemos usar git fetch y git merge o solo git pull con el flag 

$ git pull --allow-unrelated-histories:

$ git pull origin master --allow-unrelated-histories

# Por último, ahora sí podemos hacer git push para guardar los cambios de nuestro repositorio local en GitHub:

$ git push origin master
```

**Cómo autenticarte en GitHub 2022**

Antes de empezar debemos renombrar la rama **‘máster’** a **‘main’**, este es el nuevo estándar en GitHub, para esto:

Primero nos posicionamos en la rama a la que queremos cambiarle el nombre.

Ejecutamos el siguiente comando: 

```sh
$ git branch -M main
```

**Pasos para crear un token de acceso personal.**

Inicia sesión en GitHub:

   >Ve a GitHub e inicia sesión con tu cuenta.
    Accede a la configuración de tu cuenta: Haz clic en tu avatar en la esquina superior derecha de la página y selecciona "Settings" (Configuración).

Ve a la sección de desarrolladores:

> En el menú de la izquierda, desplázate hacia abajo y selecciona "Developer settings" (Configuración de desarrollador).

Crea un nuevo token:

>En la sección de "Personal access tokens", selecciona "Tokens classic" y luego haz clic en "Generate new token" (Generar nuevo token).

Configura el token:

>Asigna un nombre descriptivo al token para recordar su propósito.
Selecciona la duración del token (por ejemplo, 30 días, 60 días, etc.) o déjalo sin fecha de expiración.
Selecciona los permisos necesarios para el token, dependiendo de lo que necesites hacer (repositorios, notificaciones, paquetes, etc.).

Genera y guarda el token:

>Haz clic en "Generate token" (Generar token).
**Importante**: Copia y guarda el token en un lugar seguro, ya que no podrás verlo nuevamente una vez que cierres esta ventana.

Usa el token:

>Puedes utilizar este token en lugar de tu contraseña al autenticarte en GitHub desde la línea de comandos o herramientas que requieran acceso a tu cuenta de GitHub.

*Desde el 2022 GitHub ya no deja hacer el push con la contraseña del propio GitHub, para esto tenemos que crear un token, y este token es la contraseña que vamos a colocar cuando nos pida clave.*

Descubre el uso de tags en Github

Ver los Tags en GitHub:

>1. Navega a tu repositorio en GitHub.
>2. Ve a la pestaña "Tags" en la sección de "Releases" para ver todos los tags.

Crear una release desde un Tag:

>1. En la pestaña "Releases", haz clic en "Draft a new release".
>2. Selecciona el tag que deseas asociar con la release.
>3. Llena los detalles como título, descripción y, si es necesario, adjunta binarios o archivos para la release.
>4. Haz clic en "Publish release" para crear una nueva release basada en el tag seleccionado.

## PORTAFOLIO

*Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Tutor:*

**Dante Nicolás Martinez**

<sub>Segundo Semestre Parte 1:</sub>

***Revisar y ejecutar cada comando, hacerlo como practica: NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.***

**Profesor Ariel Betancud**

# CLASE 02 MIÉRCOLES 21 DE AGOSTO DEL 2024 - Portafolio 2

**Vamos a cargar la llave SSH publica en GitHub**

Para copiar la llave publica debes ir al archivo ***.ssh*** y allí encontrarás el archivo ***.pub*** lo podes abrir con el *txt*, luego copiar el contenido que esta dentro.

    1- copiar la llave publica. Ir a GitHub, vamos a setting, vamos a SSH and GPG keys
    2- crear una nueva #New SSH key poner nombre y pegar la ssh publica, con esto esta listo.

<sub>Aconsejo que la ssh tenga el nombre del ordenador en el que estas trabajando. Esto se debe hacer con cada pc nueva o dispositivo nuevo que tengamos para acceder a nuestra cuenta de GitHub.</sub>

```sh
git branch #Vemos en que rama estamos

git checkout master #Ponernos en la rama master

git branch -M main #Cambiamos el nombre a la rama master

git remote add origin git@github.com:nombreUsuario/class-git.git #Agregamos el repositorio remoto, este es un ejemplo

git remote -v #Vemos si ya esta conectado

git merge segunda #Mergeamos lo que tenemos en la rama segunda en main

git commit -am "Uso de GitHub parte 20" #Hacemos el commit de hoy

git push origin main #Pasamos todo lo hecho a GitHub, revisar en el repositorio en GitHub.
```

***Frente al cambio de nombre de rama master a main, suele suceder que en el repo de GitHub se hayan creado dos ramas, la rama master y la rama main, se debe ir al repo, settings y ahí se puede cambiar la rama principal, en vez de que siga siendo master, que sea la rama main, luego de eso ya podemos borrar la rama master.***

### PORTAFOLIO

***Vamos a ver unos videos en el campus de como avanzar en lo que es un portafolio por el Tutor:***

**Dante Nicolás Martinez**

<sub>Segundo Semestre Parte 2:</sub>

> Revisar y ejecutar cada comando, hacerlo como practica: NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.

**Profesor Ariel Betancud**

# CLASE 03 MIÉRCOLES 28 DE AGOSTO DEL 2024 - Portafolio 3

## Cambios en GitHub: de master a main

> El escritor Argentino Julio Cortázar afirma que las palabras tienen color y peso. Por otro lado, los sinónimos existen por definición, pero no expresan lo mismo. Feo no es lo mismo que desagradable, ni aromático es lo mismo que oloroso.
> Por lo anterior, podemos afirmar que los sinónimos no expresan lo mismo, no tienen el mismo “color” ni el mismo “peso”.

**Sí, esta lectura es parte de la enseñanza profesional de Git & GitHub.**

**Desde el 1 de octubre de 2020 GitHub cambió el nombre de la rama principal: ya no es “master” -como aprenderás aquí- sino main.**

>Este derivado de una profunda reflexión ocasionada por el movimiento #BlackLivesMatter.

La industria de la tecnología lleva muchos años usando términos como **master, slave, blacklist o whitelist** y esperamos pronto puedan ir desapareciendo.

***Y sí, las palabras importan.***

*Por lo que de aquí en adelante cada vez que me escuches mencionar “master” debes saber que hago referencia a “main”.*

¿Cuando es que sigue siendo **"master"** y cuando sigue siendo **"main"**?

Cuando se crea un repositorio desde **git bash** en nuestro ordenador a través de **git init**, sigue siendo el estandar como master. ¿Qué hacer con esto? Debes cambiar el nombre de la rama master a main con el comando **"git branch -M main"**.
Ahora cuando creamos un repositorio desde la nube, osea desde GitHub, ya verás que la rama principal tiene por default el nombre de *"main"* y al clonar a nuestro ordenador seguira teniendo este nombre y no será necesario ningun cambio.

### PORTAFOLIO

***Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Tutor:***

**Dante Nicolás Martinez**

<sub>**Segundo Semestre Parte 3:**</sub>

# CLASE 04 MIÉRCOLES 4 DE SEPTIEMBRE DEL 2024 - Portafolio 4



1. Tu primer push
La creación de las SSH es necesario solo una vez por cada computadora. Aquí conocerás cómo conectar a GitHub usando SSH.


Luego de crear nuestras llaves SSH podemos entregarle la llave pública a GitHub para comunicarnos de forma segura y sin necesidad de escribir nuestro usuario y contraseña todo el tiempo.

Para esto debes entrar a la Configuración de Llaves SSH en GitHub, crear una nueva llave con el nombre que le quieras dar y el contenido de la llave pública de tu computadora.

Ahora podemos actualizar la URL que guardamos en nuestro repositorio remoto, solo que, en vez de guardar la URL con HTTPS, vamos a usar la URL con SSH:

ssh

<sub>git remote set-url origin url-ssh-del-repositorio-en-github</sub>

Comandos para copiar la llave SSH:

ESTAS SON LAS RUTAS DEL SSH PUBLICO
-Mac:
pbcopy < ~/.ssh/id_rsa.pub

Windows (Git Bash):

clip < ~/.ssh/id_rsa.pub

Linux (Ubuntu):

cat ~/.ssh/id_rsa.pub



Importante


Las buenas costumbres nos enseñan que antes de hacer un push, siempre debemos hacer un pull, un fetch, esto para que si alguien ya hizo algún cambio, no se genere un conflicto.

Invitar a un colaborador

Para invitar a un colaborador debemos ir a GitHub y seleccionar:
setting -> colaborators -> ingresar contraseña o un F2A de verificación y enviar la invitación escribiendo el nombre de usuario.


Del otro lado el usuario invitado solo debe aceptar y listo, ya puede participar del proyecto haciendo commit.

<hr>

# CLASE 05 MIÉRCOLES 11 DE SEPTIEMBRE DEL 2024 - Portafolio 5




Git tag y versiones en GitHub

En Git, las etiquetas o Git tags tienen un papel importante al asignar versiones a los commits más significativos de un proyecto. Aprender a utilizar el comando git tag, entender los diferentes tipos de etiquetas, cómo crearlas, eliminarlas y compartirlas, es esencial para un flujo de trabajo eficiente.


Creación de etiquetas en Git

```sh
git tag

```


Sustituye con un identificador semántico que refleje el estado del repositorio en el momento de la creación. Git admite etiquetas anotadas y ligeras.

Listado de etiquetas
Para obtener una lista de etiquetas en el repositorio, ejecuta el siguiente comando:

>$ git tag -a v1.0 -m "Product release"
  git tag -a ronburgundy -m "Brick killed a guy a trident."

  Para crear una etiqueta, ejecuta el siguiente comando:



Las etiquetas anotadas almacenan información adicional como la fecha, etiquetador y correo electrónico, y son ideales para publicaciones públicas. Las etiquetas ligeras son más simples y se emplean como “marcadores” de una confirmación específica.


git tag

Esto mostrará una lista de las etiquetas existentes, como:

v1.0

v1.1

v1.2

Para perfeccionar la lista, puedes utilizar opciones adicionales, como -l con una expresión comodín.


Uso compartido de etiquetas

Compartir etiquetas requiere un enfoque explícito al usar el comando git push. Por defecto, las etiquetas no se envían automáticamente. Para enviar etiquetas específicas, utiliza:

git push origin

Para enviar varias etiquetas a la vez, usa:

git push origin --tags


Eliminación de etiquetas
Para eliminar una etiqueta, usa el siguiente comando:

git tag -d

Esto eliminará la etiqueta identificada por en el repositorio local.

En resumen, las etiquetas en Git son esenciales para asignar versiones y capturar instantáneas importantes en el historial de un proyecto. Aprender a crear, listar, compartir y eliminar etiquetas mejorará tu flujo de trabajo con Git.

<hr>

# CLASE 06 MIÉRCOLES 18 DE SEPTIEMBRE DEL 2024 - Portafolio 6

>Error con los tags
Investigación: ¿Qué pasa si por error cargamos un tag dos veces?

¿Cómo solucionarías este problema o error?

La respuesta debe ser enviada antes de las 23 horas por cada grupo, deben enviar comandos y todo los pasos que harían frente a este conflicto.

Nosotros lo resolveremos aqui:


Para eliminar una etiqueta, usaremos el siguiente comando:

>git tag -d "Nombre de la etiqueta"

1. Primero lo que deberiamos hacer seria listar los tags para ver cual tenemos duplicado ejecutamos el siguiente comando:

>git tag

2. Eliminar el tag duplicado localmente
Supongamos que el tag duplicado se llama v1.0.0. Para eliminar el tag localmente, usaremos el siguiente comando:

>git tag -d v1.0.0.

Este comando solo elimina el tag en nuestro repositorio local.

3. Eliminar el tag duplicado en el repositorio remoto
Después de eliminar el tag localmente, también debemos eliminarlo del repositorio remoto. Para hacerlo, ejecutaremos:

En el git BASH ejecutaremos

>git push origin --delete v1.0.0

Este comando elimina el tag de nuestro repositorio en GitHub.

4. Verificación final
Para asegurarnos de que todo se ha resuelto correctamente, listaremos los tags en el repositorio remoto:

>git ls-remote --tags origin


<hr>

# CLASE 07 MIÉRCOLES 25 DE SEPTIEMBRE DEL 2024 - Portafolio 7

Error con los tags
Investigación: Si un tag es imposible generarlo dos veces ¿Cómo es que existe el error de dos tags con el mismo nombre?

¿Cómo se origina este problema o error?

El error de tener dos tags con el mismo nombre en Git generalmente ocurre debido a un malentendido o una operacion incorrecta en el repositorio remoto. Aqui hay algunas situaciones comunes que pueden causar este problema.

1. Fuerza de actualizacion de tags. Si alguien fuerza la actualizacion de un tag existente usando el comando git push --force, puede sobrescribir el tag en el repositorio remoto. Esto puede causar confusión si otros desarrolladores ya han referenciado el tag anterior.

2. Confusion entre tags y remotos: A veces, los desarrolladores pueden tener un tag local que no coincide con el tag remoto. Si intentan crear un tag con el mismo nombre sin sincronizar correctamente, pueden surgir conflictos.

3. Errores de sincronización: Si hay problemas de sincronizacion entre el repositorio local y remoto, como conflictos no resueltos o actualizaciones no aplicadas, puede parecer que hay dos tags con el mismo nombre.

Para solucionar estos problemas seguiremos estos pasos:

1. Eliminar el tag localmente:
git tag -d nombre_del_tag

2. Eliminar el tag del repositorio remoto:
git push origin --delete nombre_del_tag

3. Crear el nuevo tag  (si es necesario):
git tag nombre_del_tag

4. Enviar el nuevo tag al repositorio remoto:
git push origin nombre_del_tag

<p>Estos pasos aseguran que el tag sea único y esté correctamente sincronizado entre el repositorio local y el remoto.</p>