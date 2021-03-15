import tkinter

canvas = tkinter.Canvas(height = 1000, width = 1000)
canvas.pack()

maxx = int(canvas["width"])
maxy = int(canvas["height"])

for i in range(0, maxx, 10):
    canvas.create_line(i, 0, i, maxy, fill = 'gray')

for i in range(0, maxy, 10):
    canvas.create_line(0, i, maxx, i, fill = 'gray')

def napis(suradnice):
    x = suradnice.x
    y = suradnice.y
    info = '[' + str(x) + ', ' + str(y) + ']'
    infox = x + 80

    if maxx - infox < 80:
        infox = x - 80

    canvas.delete('napis')
    canvas.create_text(infox, y, text = info, fill = 'red', font = 'Arial 20', tags = 'napis')

canvas.bind('<Motion>', napis)
