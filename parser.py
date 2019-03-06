from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    ident(transform)
    file = open(fname, "r").read().split("\n")
    for i in range(len(file)):
        if file[i] == "line":
            l = file[i + 1].split(" ")
            add_edge(points, int(l[0]),int(l[1]),int(l[2]),int(l[3]),int(l[4]),int(l[5]))
        if file[i] == "ident":
            ident(transform)
        if file[i] == "scale":
            l = file[i + 1].split(" ")
            matrix_mult(make_scale(int(l[0]), int(l[1]), int(l[2])), transform)
        if file[i] == "move":
            l = file[i + 1].split(" ")
            matrix_mult(make_translate(int(l[0]), int(l[1]), int(l[2])), transform)
        if file[i] == "rotate":
            l = file[i + 1].split(" ")
            if l[0] == "x":
                matrix_mult(make_rotX(l[1]), transform)
            if l[0] == "y":
                matrix_mult(make_rotY(l[1]), transform)
            if l[0] == "z":
                matrix_mult(make_rotZ(l[1]), transform)
        if file[i] == "apply":
            matrix_mult(transform, points)
        if file[i] == "display":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        if file[i] == "save":
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_extension(screen, file[i + 1])
    pass
