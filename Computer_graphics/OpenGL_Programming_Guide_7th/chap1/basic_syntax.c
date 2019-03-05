/**
INIT Operation:

glutInit(); 
glutInitDisplayMode(); //RGBA; single buffer or dual buffer;...
glutInitWindowPosition(); //window position (away from upper left corner of your screen!);
glutInitWindowSize();
glOrtho(); //Specify coordinate system


RENDER Operation:

glClearColor(); //Determine window color
glClear(); //render window.

DRAWING Operation:

glColor3f(); //Color for drawing objects.
glBegin(); //Code for defining drawing objects should be put between glBegin() and glEnd();
    glVertex3f();
    glVertex3fv();
glEnd();
glFlush(); //make sure Instructions' execution.

------------------------------------------------
glColor3f(1.0, 0.0, 0.0);
    is equivalent to:
GLfloat color_array[] = {1.0, 0.0, 0.0};
glColor3fv(color_array);

------------------------------------------------

MAIN FUNCTION:
glutDisplayFunc(); //redraw;
glutMainLoop(); //Start program.

* #TODO: will add more contents later.
*/


