
# Window size (in pixels)
WIDTH = 900
HEIGHT = 600

BALL_SIZE = 20
BAT_THICKNESS = 10
BAT_LENGTH = 100
SPEED = 200  # pixels per second
BAT_SPEED = SPEED * 1.5  # also pixels per second

NET_LENGTH = 20
FONT_SIZE = 42
TEXT_ALIGN = 30


bat_coordinates = [HEIGHT // 2, HEIGHT // 2]  # vertical position of two bats
ball_coordinates = [0, 0]  # x, y ball coordinates -- set in reset()
ball_speed = [0, 0]  # x, y components of ball speed -- set in reset()
keys_pressed = set()  # set of pressed keys
score = [0, 0]  # score for 2 players


import pyglet

window = pyglet.window.Window(width=WIDTH, height=HEIGHT)

from pyglet import gl
...
def draw_rectangle(x1, y1, x2, y2):
    """Draw the rectangle to the given coordinates

    How it should look like::

         y2 - +-----+
              |/////|
         y1 - +-----+
              :     :
             x1    x2
    """
    # I am calling OpenGL here which is the easiest to use for us at the moment
    gl.glBegin(gl.GL_TRIANGLE_FAN)   # draw connected triangles
    gl.glVertex2f(int(x1), int(y1))  # coordinate A
    gl.glVertex2f(int(x1), int(y2))  # coordinate B
    gl.glVertex2f(int(x2), int(y2))  # coordinate C, draw triangle ABC
    gl.glVertex2f(int(x2), int(y1))  # coordinate D, draw triangle BCD
    # another coordinate E would draw triangle CDE and so on
    gl.glEnd()  # stop drawing the triangles

def render():
    """Render(draw) state of the game"""
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)  # clear the window (paint the window black)
    gl.glColor3f(1, 1, 1)  # set the paint to white

window = pyglet.window.Window(width=WIDTH, height=HEIGHT)
window.push_handlers(
    on_draw=render,  # for drawing into the window use function `render`
)


pyglet.app.run()  # everything is set, let the game begin