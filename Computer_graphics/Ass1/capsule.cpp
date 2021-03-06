#include <math.h>
#include <GLUT/GLUT.h>

void display();
void specialKeys();
void capsule();
void semi_sphere_up();
void semi_sphere_down();

double rotate_y = 0;
double rotate_x = 0;
#define M_PI 3.14159265357

GLfloat vertices[][3] = { { -0.5, -0.5, -0.5 }, { 0.5, -0.5, -0.5 },
    { 0.5, 0.5, -0.5 }, { -0.5, 0.5, -0.5 }, { -0.5, -0.5, 0.5 },
    { 0.5, -0.5, 0.5 }, { 0.5, 0.5, 0.5 }, { -0.5, 0.5, 0.5 } };

GLfloat colors[][3] = { { 0.0, 0.0, 0.0 }, { 1.0, 0.0, 0.0 },
    { 1.0, 1.0, 0.0 }, { 0.0, 1.0, 0.0 }, { 0.0, 0.0, 1.0 },
    { 1.0, 0.0, 1.0 }, { 1.0, 1.0, 1.0 }, { 0.0, 1.0, 1.0 } };

GLubyte cubeIndices[24] = { 0, 3, 2, 1, 2, 3, 7, 6,
    0, 4, 7, 3, 1, 2, 6, 5, 4, 5, 6, 7, 0, 1, 5, 4 };



// draw capsule
void capsule() {
    float v[121][3];

    float Radius = 0.5;
    int sectors = 10;
    int rings = 10;

    float x, y, z;

    for (int i = 0; i < rings + 1; i++)
    {
        for (int j = 0; j < sectors + 1; j++)
        {
            y = Radius * 0.1 * (i); //z
            x = Radius * cos(2*j*M_PI / sectors); //x
            z = Radius * sin(2*j*M_PI / sectors); //y
            
            v[i*(sectors + 1) + j][0] = x;
            v[i*(sectors + 1) + j][1] = y;
            v[i*(sectors + 1) + j][2] = z;
        }
    }
    
    
    int np = 0;
    int index[484];
    for (int i = 0; i < rings; i++) { // r: index for ring
        for (int j = 0; j < sectors; j++) { // s: index for sector
            index[4 * np + 0] = i * (sectors + 1) + j;
            index[4 * np + 1] = i * (sectors + 1) + (j + 1);
            index[4 * np + 2] = (i + 1) * (sectors + 1) + (j + 1);
            index[4 * np + 3] = (i + 1) * (sectors + 1) + j;
            np++;
        }
    }
    
    // serface
    for (int i = 0; i < np; i++) { // i: index for polygon
        glBegin(GL_LINE_LOOP);
        glColor3f(1.0, 0.0, 0.0);
        glVertex3fv(v[index[4 * i + 0]]);
        glVertex3fv(v[index[4 * i + 1]]);
        glVertex3fv(v[index[4 * i + 2]]);
        glVertex3fv(v[index[4 * i + 3]]);
        glEnd();
    }
    
    semi_sphere_up();
    semi_sphere_down();
}

/* Draw upper semi_sphere */
void semi_sphere_up()
{
    float v[121][3];//points, sector+1
    float Radius = 0.5;
    int sectors = 10;
    int rings = 10;
    float x, y, z;

    //Points value
    for (int i = 0; i < rings+1; i++)
    {
        for (int j = 0; j < sectors+1; j++)
        {
            //float const z = cos(2 * M_PI * r * R);
            //float const x = sin(2 * M_PI * r * R) * cos(2 * M_PI * s * S);
            //float const y = sin(2 * M_PI * r * R) * sin(2 * M_PI * s * S);
            if (2 * i < rings) {
                y = Radius * cos(i*M_PI/ rings) + (Radius * 0.1 * rings);
            } else {
                y = (Radius * 0.1 * rings);
            }
            x = Radius * sin(i*M_PI / rings)*cos(2*j*M_PI / sectors);
            z = Radius * sin(i*M_PI / rings)*sin(2*j*M_PI / sectors);
            v[i*(sectors + 1) + j][0] = x;
            v[i*(sectors + 1) + j][1] = y;
            v[i*(sectors + 1) + j][2] = z;
        }
    }
    int np = 0;
    int index[484];
    for (int i = 0; i < rings; i++) { // r: index for ring
        for (int j = 0; j < sectors; j++) { // s: index for sector
            index[4 * np + 0] = i * (sectors + 1) + j;
            index[4 * np + 1] = i * (sectors + 1) + (j + 1);
            index[4 * np + 2] = (i + 1) * (sectors + 1) + (j + 1);
            index[4 * np + 3] = (i + 1) * (sectors + 1) + j;
            np++;
        }
    }
    
    for (int i = 0; i < np; i++) { // i: index for polygon
        glBegin(GL_LINE_LOOP);
        glColor3f(1.0, 0.0, 0.0);
        glVertex3fv(v[index[4 * i + 0]]);
        glVertex3fv(v[index[4 * i + 1]]);
        glVertex3fv(v[index[4 * i + 2]]);
        glVertex3fv(v[index[4 * i + 3]]);
        glEnd();
        
    }
}

/* Draw lower semi_sphere */
void semi_sphere_down()
{
    float v[121][3];//
    float Radius = 0.5;
    int sectors = 10;
    int rings = 10;
    float x, y, z;
    //angle = 36, curve = PI / 5;
    //Points value
    for (int i = 0; i < rings+1; i++)
    {
        for (int j = 0; j < sectors+1; j++)
        {
            //float const z = cos(2 * M_PI * r * R);
            //float const x = sin(2 * M_PI * r * R) * cos(2 * M_PI * s * S);
            //float const y = sin(2 * M_PI * r * R) * sin(2 * M_PI * s * S);
            if (2 * i < rings) {
                y = -1 * (Radius * cos(i*M_PI/ rings)) ;
            } else {
                y = 0;
            }
            x = Radius * sin(i*M_PI / rings)*cos(2*j*M_PI / sectors);
            z = Radius * sin(i*M_PI / rings)*sin(2*j*M_PI / sectors);
            v[i*(sectors + 1) + j][0] = x;
            v[i*(sectors + 1) + j][1] = y;
            v[i*(sectors + 1) + j][2] = z;
        }
    }
    
    int np = 0;
    int index[484];
    for (int i = 0; i < rings; i++) { // r: index for ring
        for (int j = 0; j < sectors; j++) { // s: index for sector
            index[4 * np + 0] = i * (sectors + 1) + j;
            index[4 * np + 1] = i * (sectors + 1) + (j + 1);
            index[4 * np + 2] = (i + 1) * (sectors + 1) + (j + 1);
            index[4 * np + 3] = (i + 1) * (sectors + 1) + j;
            np++;
        }
    }
    
    for (int i = 0; i < np; i++) { // i: index for polygon
        glBegin(GL_LINE_LOOP);
        glColor3f(1.0, 0.0, 0.0);
        glVertex3fv(v[index[4 * i + 0]]);
        glVertex3fv(v[index[4 * i + 1]]);
        glVertex3fv(v[index[4 * i + 2]]);
        glVertex3fv(v[index[4 * i + 3]]);
        glEnd();
        
    }
}

void display(){
    
    //  Clear screen and Z-buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    
    // Reset transformations
    glLoadIdentity();
    
    // Other Transformations
    // glTranslatef( 0.1, 0.0, 0.0 );      // Not included
    // glRotatef( 180, 0.0, 1.0, 0.0 );    // Not included
    
    // Rotate when user changes rotate_x and rotate_y
    glRotatef(rotate_x, 1.0, 0.0, 0.0);
    glRotatef(rotate_y, 0.0, 1.0, 0.0);
    
    // Other Transformations
    // glScalef( 2.0, 2.0, 0.0 );          // Not included
    
    //colorcube3();
    //sphere();
    capsule();
    glFlush();
    glutSwapBuffers();
    
}
// ----------------------------------------------------------
// specialKeys() Callback Function
// ----------------------------------------------------------
void specialKeys(int key, int x, int y) {
    
    //  Right arrow - increase rotation by 5 degree
    if (key == GLUT_KEY_RIGHT)
        rotate_y += 5;
    
    //  Left arrow - decrease rotation by 5 degree
    else if (key == GLUT_KEY_LEFT)
        rotate_y -= 5;
    
    else if (key == GLUT_KEY_UP)
        rotate_x += 5;
    
    else if (key == GLUT_KEY_DOWN)
        rotate_x -= 5;
    
    //  Request display update
    glutPostRedisplay();
    
}

// ----------------------------------------------------------
// main() function
// ----------------------------------------------------------
int main(int argc, char* argv[]){
    
    //  Initialize GLUT and process user parameters
    glutInit(&argc, argv);
    
    //  Request double buffered true color window with Z-buffer
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    
    // Create window
    glutCreateWindow("Color Cube");
    
    //  Enable Z-buffer depth test
    glEnable(GL_DEPTH_TEST);
    
    // Callback functions
    glutDisplayFunc(display);
    glutSpecialFunc(specialKeys);
    
    //  Pass control to GLUT for events
    glutMainLoop();
    
    //  Return to OS
    return 0;
    
}
