from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
def myap():
    glMatrixMode(GL_PROJECTION)
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
   #glOrtho(-10, 10, -10, 10, -10, 10)
    gluPerspective(60,1,.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)


def draw_1():




    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 0,1)
    glTranslate(-6,0,-2)
    glScale(2,2,.5)
    glutWireCube(3)
    glPopAttrib()
    glPopMatrix()






    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 0,1)
    glTranslate(-3,-1 , 2)
    glScale(2, .5, 2)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 0,1)
    glTranslate(-6, -5, 3)
    glScale(.5, -3, .5)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 0,1)
    glTranslate(-6, -5, 0)
    glScale(.5, -3, .5)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()


    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 0,1)
    glTranslate(-3, -6.5, 2)
    glScale(.5, -3, .5)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()


    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glColor(0, 0, 0,1)
    glTranslate(-4, -6.5, -2)
    glScale(-.5, -3, -.5)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()


def draw_2():


    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 0,1)
    glTranslate(3.5,0,-3)
    glScale(2,2,.5)
    glutWireCube(3)
    glPopAttrib()
    glPopMatrix()





    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 0,1)
    glTranslate(5,0 , 2)
    glScale(2, .5, 2)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 0,1)
    glTranslate(3, -4, 3)
    glScale(.5, -3, .5)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 0,1)
    glTranslate(6, -5, -1.5)
    glScale(.5, -3, .5)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()


    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 0,1)
    glTranslate(6, -6, 1.5)
    glScale(.5, -3, .5)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()


    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glColor(0, 0, 0,1)
    glTranslate(2, -5, -1.5)
    glScale(-.5, -3, -.5)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()
    draw_1()
    glFlush()













glutInit()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(400,400)
glutCreateWindow(b"table")
glutDisplayFunc(draw_2)
glutIdleFunc(draw_2)
myap()
glutMainLoop()