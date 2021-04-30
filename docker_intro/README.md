# Docker - intro.

- Introducción a Docker
- Hands on  
  - 1. Descargar imagen y ejecutar contenedor con Jupyter notebook para DS 
  - 2. Ejecutar 2 contenedores que se comuniquen  
- Más comandos  
- Próximos pasos

## Qué es Docker

#### "_Build and Ship any Application Anywhere_"

[Docker](https://www.docker.com/) es un proyecto de código abierto el cual permite empaquetar una aplicación y sus dependencias en una unidad aislada, llamada _contenedor_, el cual se puede ejecutar en cualquier lugar, automatizando el despliegue de estas aplicaciones.  
Para esto, implementa una API de alto nivel para proporcionar contenedores livianos que ejecutan procesos de manera aislada.

Esto facilita la flexibilidad y portabilidad en donde la aplicación se puede ejecutar, ya sea en las instalaciones físicas, la nube pública, nube privada, etc.

+ Lanzamiento: marzo de 2013	
+ Programado en Go

Con los contenedores se evita el problema de: **"It works on my machine"**.

![It works on my machine](/images/it_works.png)


### Máquinas virtuales (VM)

Una máquina virtual (VM) es un sistema operativo completo funcionando de manera aislada sobre otro sistema operativo completo.

La tecnología de VMs permite compartir el hardware de modo que lo puedan utilizar varios sistemas operativos al mismo tiempo.

Para que las máquinas virtuales puedan ejecutarse es necesario instalar otro componente por encima del S.O.: **el hipervisor**   
Bajo éste esquema, un _hipervisor_ es un software especializado en exponer los recursos hardware que están debajo del sistema operativo, de modo que puedan ser utilizados por otros sistemas operativos. Esto incluye CPUs, memoria y espacio en disco, además del resto del hardware. De este modo se pueden crear máquinas virtuales a las que se expone parte del hardware subyacente.    
Los _hipervisores_ vienen con productos como Hyper-V, VirtualBox o VMWare, entre otros.

Con todo esto podemos tener diferentes sistemas operativos ejecutándose en paralelo sobre la misma máquina física, cada uno con su memoria y espacio en disco reservados (los "cores" se pueden compartir), y completamente aislados unos de otros. 


### Contenedores

Al igual que en las VM, los contenedores aislan las aplicaciones y generan un entorno replicable, pero se diferencian en que en lugar de albergar un sistema operativo completo lo que hacen es compartir los recursos del propio sistema operativo "host" sobre el que se ejecutan.

En éste en lugar del _hipervisor_ tenemos el _Docker Engine_ el cual se encarga gestionar los contenedores con nuestras aplicaciones, pero en lugar de exponer los diferentes recursos de hardware de la máquina para cada aplicación, lo que hace es compartirlos entre todos los contenedores optimizando su uso y eliminando la necesidad de tener sistemas operativos separados para conseguir el aislamiento.


### Contenedores vs VM

+ En primer lugar debemos tener en cuenta que, en el caso de los contenedores, el hecho de que no necesiten un sistema operativo completo sino que reutilicen el subyacente reduce mucho la carga que debe soportar la máquina física, el espacio de almacenamiento utilizado y el tiempo necesario para lanzar las aplicaciones.  
Por lo tanto los contenedores son mucho más ligeros que las máquinas virtuales.

+ Cuando definimos una máquina virtual debemos indicar de antemano cuántos recursos físicos les asignamos. Es decir, debemos indicar decir cuándos Cores, RAM y espacio en disco tendrá disponible cada VM, y aunque nuestra aplicación no haga uso de la totalida de los recursos estos no podrán ser utilizados por otras máquinas virtuales ni por nadie más.  
En el caso de los contenedores esto no es así. De hecho no indicamos qué recursos vamos a necesitar, sino que es Docker Engine, en función de las necesidades de cada momento, el encargado de asignar lo que sea necesario para que los contenedores funcionen adecuadamente.

+ El espacio ocupado en disco es muy inferior con Docker al no necesitar que instalemos el sistema operativo completo.

+ Los contenedores permiten desplegar aplicaciones más rápido, arrancarlas y pararlas más rápido y aprovechar mejor los recursos de hardware. Las máquinas virtuales nos permiten crear sistemas completos totalmente aislados, con mayor control sobre el entorno y mezclando sistemas operativos host y huésped.

![Contenedores vs VM](/images/Container_VM.png)


### Dockerfiles / Imágenes / Contenedores

Un **Dockerfile** es un archivo de texto que contiene los comandos necesarios para crear una imagen.

Una **imagen** se crea a partir de un archivo Dockerfile. Contienen la unión de sistemas de archivos apilados en capas, donde cada capa representa una modificación de la imagen y equivale a una instrucción en el archivo Dockerfile.

[Repositorio de imágenes](https://hub.docker.com/)

Un **contenedor** es una instancia en ejecución de una imagen.

![Dockerfiles / Imágenes / Contenedores](/images/images_containers.png)


### Ciclo de vida de un contenedor

![Cliclo de vida de un contenedor](/images/docker_likecycle.png)

Imagen de  [Nitin Agarwal](https://medium.com/@BeNitinAgarwal/lifecycle-of-docker-container-d2da9f85959)


### Comandos de Docker CLI

```
> docker --help

Usage:	docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default "/Users/avallarino/.docker")
  -c, --context string     Name of the context to use to connect to the daemon (overrides DOCKER_HOST env var and default context set with "docker context use")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level ("debug"|"info"|"warn"|"error"|"fatal") (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default "/Users/avallarino/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default "/Users/avallarino/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default "/Users/avallarino/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  builder     Manage builds
  checkpoint  Manage checkpoints
  config      Manage Docker configs
  container   Manage containers
  context     Manage contexts
  image       Manage images
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  secret      Manage Docker secrets
  service     Manage services
  stack       Manage Docker stacks
  swarm       Manage Swarm
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  build       Build an image from a Dockerfile
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  deploy      Deploy a new stack or update an existing stack
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes
```


## Hands on 1:

Descargaremos una imagen que permite ejecutar Jupyter notebooks  
Referencias:  
+ [imagen de Docker](https://hub.docker.com/r/jupyter/datascience-notebook)  
+ [Jupyter Docker Stacks](https://github.com/jupyter/docker-stacks)

1. Ejecutamos el siguiente comando para descargar la imagen:
``` 
docker pull jupyter/datascience-notebook
```

2. Ejecutamos el contenedor
``` 
docker run -p 8880:8888 -v /<path local>:/home/jovyan jupyter/datascience-notebook
```

+ `docker run`: ejecutar contenedor  
+ `-p 8880:8888`:  mapeo puerto del contenedor (8888) a puerto en host (8880). Podría omitirse este paso y acceder directo desde 8888
+ `-v /<path local>:/home/jovyan`: monta un volumen. Monta el directorio que se indice que **/<path local>** en el directorio del juputer notebook, con esto tendremos acceso a Notebooks y Datasets que tengamos en nuestro directorio y los cambios que hagamos en el código se mantendrán.
+ `jupyter/datascience-notebook`: imagen a partir de la cual ejecutaremos un contenedor

![Terminal](/images/jupyter01.png)

Una vez que el contenedor se está ejecutando, accedemos a **http://localhost:8880** y tendremos acceso a Jputer notebook corriendo en un contenedor: 

![Jupyter notebook](/images/jupyter02.png)


## Hands on 2:

![Diseño](/images/handson.png)

En éste ejemplo se ejecutarán 2 contenedores:
1. Base de datos MySQL
2. API Flask 

a partir de los cuales, a través de una API desarrolalda en Python + Flask permitirá consultar datos disponibles en otro contenedor con una BD MySQL.



### Contenedor con MySQL (sin persistencia de datos)

Ejecutaremos un contenedor desde la terminal utilizamos la imagen oficial [Docker MySQL](https://hub.docker.com/_/mysql) 

```
docker run -d --rm --name mysql_demo -e MYSQL_ROOT_PASSWORD=root -p 3336:3306 mysql:8.0.21
```

+ `docker run`: ejecutamos un contenedor. En caso de que no tengamos disponible la imágen, nos mostrará el mensaje "Unable to find image 'mysql:8.0.21' locally", la descargará y luego ejecutará el contenedor.
+ `-d`: el contenedor se ejecutará en fondo 
+ `--rm`: al detener el contenedor se elimina
+ `--name mysql_demo`: asignamos un nombre al contenedor
+ `-e MYSQL_ROOT_PASSWORD=root`: definimos la password del usuario **root** de MySQL
+ `-p 3336:3306`: mapeamos el puerto 3306 de MySQL en el contenedor con el puerto 3336 del host.
+ `mysql:8.0.21`: imagen a utilizar

> En éste caso no persistiremos los datos, por lo tanto lo que guardemos en la BD se eliminará al detener el contenedor.  
Para lograr peristencia se deben utilizar [volumenes](https://docs.docker.com/storage/volumes/)

Probar los siguientes comandos
- listar las images disponibles:
```
docker images
```
- listar los contenedores que se están ejecutando:   
En éste caso deberíamos tener uno con el el valor **mysql_demo** en la columna NAMES

```
docker ps
```


#### Ejecutando comandos en MySQL

Nos conectamos al contenedor a través de la terminal. Para esto ejecutamos la terminal del contenedor en modo interactivo:
```
docker exec -it mysql_demo /bin/bash
```

nos conenctamos a MySQL con el usuario **root**
```
mysql -u root -p
```
a continuación debemos ingresar la contraseña, la cual indicamos en _MYSQL_ROOT_PASSWORD_ (root) al momento de ejecutar el contenedor.  

El prompt nos debería mostrar `mysql>`

Una vez conectados a MySQL ejecutaremos algunos comandos desde la terminal.

1. Creamos la BD **agro_db** y la seleccionamos para trabajar:
```
CREATE DATABASE agro_db CHARSET utf8mb4;
USE agro_db;
```

2. Creamos tabla **products**:
```
CREATE TABLE products (
	id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	date DATE NOT NULL,
	commodity_name VARCHAR(100) NOT NULL,
	variety VARCHAR(100),
	low_price FLOAT,
	high_price FLOAT,
	mid_price FLOAT
);
```

3. Insertamos registros:
```
INSERT INTO products VALUES(1,  '2019-08-01', 'MANGOES', 'ATAULFO', 4.5, 5.12, 4.81);
INSERT INTO products VALUES(2,  '2019-08-01', 'MANGOES', 'KENT', 2.92, 3.83, 3.38);
INSERT INTO products VALUES(3,  '2019-08-01', 'MANGOES', 'TOMMY ATKINS', 2.92	3.92, 3.42);
INSERT INTO products VALUES(4,  '2019-08-02', 'MANGOES', 'ATAULFO', 4.5, 5.12, 4.81);
INSERT INTO products VALUES(5,  '2019-08-02', 'MANGOES', 'KENT', 2.92, 3.83, 3.38);
INSERT INTO products VALUES(6,  '2019-08-02', 'MANGOES', 'TOMMY ATKINS', 2.92, 3.92, 3.42);
INSERT INTO products VALUES(7,  '2019-08-05', 'MANGOES', 'ATAULFO', 4.5, 5.12, 4.81);
INSERT INTO products VALUES(8,  '2019-08-05', 'MANGOES', 'KENT', 2.92, 3.83, 3.38);
INSERT INTO products VALUES(9,  '2019-08-05', 'MANGOES', 'TOMMY ATKINS', 2.92, 3.92, 3.42);
INSERT INTO products VALUES(10, '2019-08-06', 'MANGOES', 'ATAULFO', 4.67, 5.5, 5.08);
```

4. Consultaremos los datos insertados
```
SELECT * FROM products;
```

5. Creamos el usuario **apiuser** y le asginamos permisos:   
(luego será utilizado para conectarnos desde la API)
```
CREATE USER 'apiuser'@'%' IDENTIFIED WITH mysql_native_password BY 'apiuser001';

GRANT ALL PRIVILEGES ON *.* TO 'apiuser'@'%';
```

> En este punto tenemos un contenedor en ejecución con MySQL como sistema de gestión de bases de datos relacional, en el cual creamos la base **agro_db**, agregamos la tabla **products** e insertamos algunos registros, los cuales se estan almacenando dentro del
sistema de archivos del contenedor, por lo tanto, si eliminamos el contenedor y lo volvemos a crear ejecutar habremos perdido esta información ya que **éste es un contenedorsin persistencia de datos**!


### Contenedor con API Flask

Para generar el contenedor con la aplicación lo haremos desde un **Dockerfile**.

1. Dockerfile:
```
FROM python:3.7.8-alpine3.12

WORKDIR /usr/src/apirest

COPY . /usr/src/apirest

RUN pip3 install --upgrade pip
RUN pip3 --no-cache-dir install -r requirements.txt

CMD  ["python3", "src/app_demo.py"]
```

+ `FROM`: el dockerfile inicia con el comando FROM en el cual se indica el SO o la imagen base a utilizar. En este caso, la images es **python:3.7.8-alpine3.12**. Luego, las demas instrucciones le dan forma a nuestra imagen.
+ `WORKDIR <path>`: directorio de trabajo dentro del contenedor **/usr/src/apirest**
+ `COPY`: Copiamos lo que tenemos en el directorio actual **.** al directorio de trabajo del contenedor **/usr/src/apirest**
+ `RUN`: ejecutamos comandos dentro del contenedor. Por ej. actualizamos `pip` y luego instalamos las librerias necesarias para la app, las cuales se indican en `requirements.txt`
+ `CMD` corremos la app.

2. Estando en el directorio que contiene la app y el _Dockerfile_ generamos la imagen:
```
docker build -t api_demo_dckr .
```

2. Ejecutamos el contenedor:
```
docker run -it --name api_demo --link mysql_demo -p 4004:4002 -d api_demo_dckr
```

+ `docker run`: ejecutamos el contenedor
+ `-it`: Se ejecutará en modo interactivo
+ `--name api_demo`: Nombre del contenedor
+ `--link mysql_demo`: vinculamos éste contenedor con el contenedor  **mysql_demo** que contiene la BD para poder conectarnos y realizar consultas.
+ `-p 4004:4002`: mapeamos el puerto 4002 de la app en el contenedor al puerto 4004 del hots.
+ `-d`: 
+ `api_demo_dckrp`: imagen a partir de la cual se ejecutará el contenedor.

Al finalizar la ejecución, si corremos el comando `docker ps` deberíamos ver los 2 contenedores.

### Ejecución de API

Desde el navegador podemos ir  **http://localhost:4004** para validar que la aplicación funcion, obtendremos el mensaje:

![Test API](/images/api_test01.png)

Y si consultamos **http://localhost:4004/products** la respuesta serán los datos que almacenamos en la base de datos del contenedor **mysql_demo**

![Test API - MySQL](/images/api_test02.png)

## Mas comandos
1. Detener todos los contenedores en ejecución:
```
docker stop $(docker ps -aq)
```

2. Eliminar contenedores:
```
docker rm $(docker ps -a -q)
```

3. Eliminar imagenes:
```
docker rmi <iamgen>
```


## Próximos pasos

+ [Volumes](https://docs.docker.com/storage/volumes/) para Persistencia de datos 
+ [Docker compose](https://docs.docker.com/compose/) para facilitar la definición y ejecución de varios contenedores.

