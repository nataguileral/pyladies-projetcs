import math

import pyglet

window = pyglet.window.Window()

def tick(t):
    snake.x = snake.x + t * 20

pyglet.clock.schedule_interval(tick, 1/30)

def process_text(text):
    snake.x = 150
    snake.rotation = snake.rotation + 10

image = pyglet.image.load("snake.png")
snake = pyglet.sprite.Sprite(image, x=10, y=10)

def draw():
    window.clear()
    snake.draw()

def click(x, y, button, mode):
    print(button, mode)
    snake.x = x
    snake.y = y

window.push_handlers(
    on_text=process_text,
    on_draw=draw,
    on_mouse_press=click,
)

image2 = pyglet.image.load('snake2.png')

def change(t):
    snake.image = image2
    pyglet.clock.schedule_once(change_back, 0.2)

def change_back(t):
    snake.image = image
    pyglet.clock.schedule_once(change, 0.2)

pyglet.clock.schedule_once(change, 0.2)

pyglet.app.run()