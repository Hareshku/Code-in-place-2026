from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20

def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, "aqua")
    for i in range(N_CIRCLES):
        draw_random_circle(canvas)

def draw_random_circle(canvas):
    x = random.randint(0, CANVAS_WIDTH)
    y = random.randint(0, CANVAS_HEIGHT)
    color = random_color()
    canvas.create_oval(x, y, x+CIRCLE_SIZE, y+CIRCLE_SIZE, color)

    
def random_color():
    colors = ['aqua','blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

 


if __name__ == '__main__':
    main()