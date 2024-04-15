import math
import rospy
from geometry_msgs.msg import Twist
#from keyControl import getkey, pubVel
from turtlesim.srv import TeleportAbsolute, TeleportRelative
from numpy import pi

'''
 Esta función publica comandos de velocidad para controlar el movimiento de la tortuga.
 Recibe los siguientes argumentos: 
 vel_x: Velocidad lineal en la dirección x.
 vel_y: Velocidad lineal en la dirección y.
 ang_z: Velocidad angular alrededor del eje z.
 t:  Duración durante la cual se deben aplicar los comandos de velocidad en segundos.
 nt: Duración durante la cual se deben aplicar los comandos de velocidad en nanosegundos.
'''
def pubVel(vel_x, vel_y, ang_z, t, nt):
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('velPub', anonymous=False)
    vel = Twist()
    vel.linear.x = vel_x
    vel.linear.y = vel_y
    vel.angular.z = ang_z
    #rospy.loginfo(vel)
    endTime = rospy.Time.now() + rospy.Duration(t,nt)
    while rospy.Time.now() < endTime:
        pub.publish(vel)



def draw_square(side_length):

    for _ in range(4):
        pubVel(side_length, 0, 0, side_length, 0)
        pubVel(0, 0, math.pi / 2, 1, 0)

def draw_triangle(side_length):

    for _ in range(3):
        pubVel(side_length, 0, 0, side_length, 0)
        pubVel(0, 0, 2 * math.pi / 3, 1, 0)

def run():
    draw_square(2)  # Lado del cuadrado de longitud 2
    rospy.loginfo("Square drawn!")
    rospy.sleep(1)  # Espera un segundo antes de dibujar el siguiente
    rospy.loginfo("Drawing triangle...")
    draw_triangle(2)  # Lado del triángulo de longitud 2
  
    pubVel(0,0,1,math.pi/2,0)

if __name__ == '__main__':
    try:
        run()
    except rospy.ROSInterruptException:
        pass