# FRM_lab2
ROS y kobuki
# Guía 2a Introducción a ROS.
Daniel Felipe Cantor Santana, Andres Felipe Zuleta Romero, Thomas Hernandez Ochoa,
Edgar Giovanny Obregon Espitia.
## 1. Definición de ROS y sus principales ventajas.
ROS se conoce como Robot Operating System, este es un framework de código abierto el
cual le da la facilidad a los desarrolladores de crear aplicaciones y programas para robots
que resultan ser algo complejos utilizando bibliotecas y herramientas de software integradas
en el framework, este necesita montarse sobre otro sistema operativo, en este caso es
posible montar ROS Noetic en Ubuntu 20.04.
Sus principales ventajas son:

● Flexibilidad: ROS es modular y se puede utilizar para construir una amplia gama de
aplicaciones.

● Ecosistema Amplio: Ofrece un vasto ecosistema de herramientas y bibliotecas
para construir aplicaciones complejas rápidamente.

# 2. ¿Qué comandos se pueden usar con rosnode, rostopic, rosservice, rosmsg y
rospack?

A continuación se describe la función de cada uno de los comandos mencionados en el
enunciado para luego describir los comandos que se pueden utilizar en cada uno de ellos.

1. rosnode: Permite interactuar con nodos en el sistema de ROS.

● rosnode list: Muestra la lista de todos los nodos que se encuentran activos.

● rosnode info (nombre_del_nodo): Proporciona información detallada sobre un
nodo en específico.

2. rostopic: Facilita la comunicación entre nodos a través de tópicos de ROS.

● rostopic list: Enumera todos los tópicos posibles.

● rostopic info (nombre_del_topico): Muestra detalles sobre un topico en
especifico.

● rostopic echo (nombre_del_topico): Imprime los mensajes que fluyen a través
de un tópico.

3. rosservice: Permite llamar servicios proporcionados por nodos.
   
● rosservice list: Enumera todos los servicios disponibles.

● rosservice info (nombre_del_servicio): Muestra detalles sobre un servicio en
específico.

● rosservice cal (nombre_del_servicio)l: Llama a un servicio con unos
argumentos específicos.

4. rosmsg: Proporciona información sobre los tipos de mensajes definidos en ROS.
● rosmsg list: Lista todos los tipos de mensajes disponibles.

● rosmsg show (nombre_del_mensaje): Muestra la estructura de un mensaje
en específico.

5. rospack: Este comando gestiona los paquetes de ROS.
   
● rospack list: Enumera todos los paquetes instalados en ROS.

● rospack find (nombre_del_paquete): Este comando encuentra la ubicación de
un paquete en especifico.

## 3. Describa paso a paso que hacen los programas realizados en python, indique las
funciones de ROS empleadas.

Se utiliza el publicador de velocidad, hello ros y suscriptor de posición, además de ello para
la generación de la figura se emplea turtlesimservice, allí se importa la librería de ros para
que se pueda utilizar desde python, la cual se llama rospy, en caso de requerir enviar
mensajes se debe importar el tipo de mensaje que se va a utilizar, si nos vamos a suscribir
se usa el tipo string, en el caso de publicar se emplea el archivo de tipo twist.
En el programa subpose, se hace una suscripción para que llegue un mensaje de posición
donde se observarán valores en X y X y un ángulo el cual será correspondiente a la
orientación de la tortuga.
En el caso de publicar velocidad, el tipo de mensaje twist requiere la velocidad lineal
además de la velocidad angular.
En el caso de hello ros hay una función llamada login info, es una función encargada de
publicar en la consola, este es un primer acercamiento a ROS, el mismo ejemplo se lleva a
cabo generalmente en más lenguajes de programación, por ejemplo en python.
En el archivo de turtlesim service, se dan 5 puntos a la tortuga para que esta sea capaz de
dibujar el cuadrado, son 5 puntos ya que esta debe regresar a su punto de origen, para el
caso del triángulo en total se definen 4 puntos.
Para dibujar el cuadrado, se da un tiempo de recorrido a la tortuga, en el momento que
termina de moverse esta vuelva a spawnear pero con una dirección diferente para poder
continuar su movimiento y así realizar el dibujo del cuadrado.

## 4. Usando turtle_teleop_key y el programa de pose determine las dimensiones del
plano donde el turtle_sim puede moverse.
A continuación se presenta una imagen donde se corre el simulador turtlesim de ROS
además del nodo de la posición de la tortuga.
![image](https://github.com/Ggio0/FRM_lab2/assets/82681128/58f47622-9345-453c-97f7-f864849a9af3)

Luego, se presentan 4 imágenes donde la tortuga se encuentra en las 4 esquinas del plano
para poder determinar las dimensiones del mismo.

![image](https://github.com/Ggio0/FRM_lab2/assets/82681128/70b35183-785a-4e59-ba3b-c199c5b9812a)

![image](https://github.com/Ggio0/FRM_lab2/assets/82681128/caf46123-8792-47b4-a4a0-525093bf9069)

![image](https://github.com/Ggio0/FRM_lab2/assets/82681128/fab6df5b-f624-459c-afa2-82b1a9bddc14)

![image](https://github.com/Ggio0/FRM_lab2/assets/82681128/53fb6e30-d6bc-4ac1-bc91-59ae4343d901)

Con base en las imágenes presentadas anteriormente es posible concluir que el tamaño del
plano donde se mueve la tortuga es de 11.09 unidades X 11.09 unidades.
## 5. Describa cómo usar algún servicio en python, luego pruebe el código
proporcionado en la guía.
Los servicios de ROS permiten a los nodos realizar tareas específicas mediante otros
nodos. En el caso de python se emplean importando la carpeta “rospy”. Para ver su
funcionamiento debe verse su estructura general:
rospy.ServiceProxy(name, service_class, persistent=True)
Como se ve, debe añadirsele un nombre al servicio, agregarle una clase y si es persistente o no
(es decir si estará disponible continuamente o no). Empleando el servicio en el código del
cuadrado, se tiene lo siguiente:
rospy.wait_for_service('turtle1/teleport_absolute')
turtle1_teleport = rospy.ServiceProxy('turtle1/teleport_absolute',TeleportAbsolute)
Asumiendo que el nodo fue creado con anterioridad, se puede ver cómo se crea el servicio
“turtle1/teleort_absolute” de la clase tipo TeleportAbsolute, para así posicionar a la tortuga
en la posición que se requiere según los puntos dados en el bucle.

![image](https://github.com/Ggio0/FRM_lab2/assets/82681128/b41d2720-d279-4117-9751-b2209f9a0291)

Como puede verse en la figura anterior, se creó un archivo de código, se realizó un
catkin_make y el archivo se transformó a uno de tipo ejecutable (con el comando cdmod
+x), dando como resultado la figura esperada.
6. Inicie un nodo en turtlesim, usando el servicio spawn para aparecer otra tortuga y
realice un programa en python que haga que las tortugas dibujen un triángulo y un
cuadrado
Para el triángulo se tomó como referencia el archivo anterior, pero reduciendo su número de
puntos a 4, (nuevamente realizando la conversión para que el archivo fuera ejecutable).
Como se pedía, se realizó en simultáneo su compilación para ver a 2 tortugas, cada una
realizando una figura distinta, como puede verse en la figura:
![image](https://github.com/Ggio0/FRM_lab2/assets/82681128/a5e542f4-5fa2-4f6a-b752-0b81b19788cb)
