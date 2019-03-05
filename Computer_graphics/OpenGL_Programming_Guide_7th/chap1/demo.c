// Make sure import GLUT.framework and OpenGL.framework in project environment.

#include <GLUT/GLUT.h>

void display(void) {
    //render window color.
    glClear(GL_COLOR_BUFFER_BIT);
    
    //define object color
    glColor3f(1.0, 1.0, 1.0);
    
    glBegin(GL_POLYGON); {
        glVertex3f(0.25, 0.25, 0);
        glVertex3f(0.75, 0.25, 0);
        glVertex3f(0.75, 0.75, 0);
        glVertex3f(0.25, 0.75, 0);
    }
    glEnd();
    
    glFlush();
}

void init(void) {
    //define window color
    glClearColor(0.0, 0.0, 0.0, 1.0);
    
    //init view values
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0);
}

int main(int argc, const char *argv[]) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_RGB| GLUT_SINGLE);
    glutInitWindowSize(250, 250);
    glutInitWindowPosition(0, 0);
    glutCreateWindow("Hello world");
    init();
    
    glutDisplayFunc(display);
    glutMainLoop();
    
    return 0;
}
