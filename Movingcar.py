from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
def myap():
    glMatrixMode(GL_PROJECTION)
    glClearColor(0,1,0,0)
    glClear(GL_COLOR_BUFFER_BIT)
   #glOrtho(-10, 10, -10, 10, -10, 10)
    gluPerspective(60,1,.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)
x=0
angle=0
deltax= .001
deltaangle=.3




def draw():
    global x
    global angle
    global deltax
    global deltaangle
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)




    glLoadIdentity()
    glColor(0, 0, 0, 1)
    glTranslate(1, 0, -1)
    glScale(100, 0, 3)
    glutSolidCube(3)

    glLoadIdentity()
    glColor(1, 1, 1)
    glTranslate(2, 0, -1)
    glScale(100, 0, .5)
    glutSolidCube(3)


    glLoadIdentity()
    glColor(1, 1, 1)
    glTranslate(2, 0, 1.5)
    glScale(100, 0, .5)
    glutSolidCube(3)

    glLoadIdentity()
    glColor(1.0,1.0,0.0)
    glTranslate(-2,4,-8)
    glutSolidCube(3)


    glLoadIdentity()
    glColor(1.0, 1.0, 0.0)
    glTranslate(-20, 4, -8)
    glutSolidCube(3)


    glLoadIdentity()
    glColor(1.0, 1.0, 0.0)
    glTranslate(4, 4, -8)
    glutSolidCube(3)




    glLoadIdentity()
    glColor(1.0, 1.0, 0.0)
    glTranslate(-10, 4, -8)
    glutSolidCube(3)













    glLoadIdentity()
    glColor3f (1,0,0)
    glScale(1,0.25,0.5)
    glTranslate(x,0,0)
    glutWireCube(5)



    glLoadIdentity()
    glColor3f(1, 0, 0)
    glTranslate(x,.25*5,0)
    glScale(0.5, 0.25, 0.5)

    glutSolidCube(5)

    glColor(0,0,0,1)
    glLoadIdentity()
    glTranslate(x+2.5, -2*0.25,2.5* .5)
   # glRotate(angle,0,0,1)

    glutWireTorus(0.125, 0.5, 12, 8)

    glColor(0,0,0,1 )
    glLoadIdentity()
    glTranslate(x+2.5, -2*0.25, -2.5*.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 8)

    glColor(0, 0,0,1)
    glLoadIdentity()
    glTranslate(x-2.5, -2.5*0.25,-2.5* .5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 8)







    glColor(0,0,0,1)
    glLoadIdentity()
    glTranslate(x-2.5,-2.5*0.25,2.5*.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125,0.5,12,8)





    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(-29, 0, -1 * 6)
    glScale(0.2, 10, -0.5)
    glutSolidCube(4.5)
    glColor3f(0, 0, 0)
    glLoadIdentity()
    glTranslate(0, 0, -1 * 6)
    glScale(0.2, 10, -0.5)
    glutSolidCube(4.5)
    if x>10:

        deltax = -.001
        deltaangle=- .1




    elif x<-10:

        deltax=.001
        deltaangle=.1

    x+=deltax
    angle-=deltaangle
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(400,400)
glutCreateWindow(b"animation")
glutDisplayFunc(draw)
glutIdleFunc(draw)
myap()
glutMainLoop()