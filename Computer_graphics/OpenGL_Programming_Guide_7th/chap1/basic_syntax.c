/**
glutInit(); 
glutInitDisplayMode(); //RGBA; single buffer or dual buffer;...
glutInitWindowPosition(); //window position (away from upper left corner of your screen!);
glutInitWindowSize();
glClearColor(); //Determine window color
glClear(); //Do clear operation.
glColor3f(); //Color for drawing objects.
glOrtho(); //Specify coordinate system
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
glutDisplayFunc(); //redraw;
glutMainLoop(); //Start program.

* #TODO: will add more contents later
*/


