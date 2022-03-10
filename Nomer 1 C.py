# Nama  : Galih Pratama
# Nim   : 20051397083
# Kelas : Manajemen Informatika 2020 A

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-6, 6, -6, 6, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glColor3f(1, 1, 1)
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.00)
    glVertex2f(2, 3)
    glVertex2f(0, 0)
    glVertex2f(5, 3)
    glEnd()

    glutSwapBuffers()


glutInit(sys.argv)
glutInitWindowSize(500, 500)
glutCreateWindow("No. 1 C")
glutDisplayFunc(draw)
glutMainLoop()
