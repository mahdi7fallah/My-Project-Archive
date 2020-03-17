import tkinter as tk

w = tk.Tk()

canvas1 = tk.Canvas(w, width=300, height=300)
canvas1.pack()
btn1 = tk.Button(w, text='clear')
btn1.pack()

def create_circle(canvas_name, x, y, r):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = x + r

    return canvas_name.create_oval(x0, y0, x1, y1)




def press_click(event):
    global x0, y0
    x0 = event.x
    y0 = event.y

def release_click(event):
    x1 = event.x
    y1 = event.y
    canvas1.create_line(x0, y0, x1, y1)

def clear_canvas1(event):
    canvas1.delete('all')

canvas1.bind('<Button-1>', press_click)
canvas1.bind('<ButtonRelease-1>', release_click)
btn1.bind('<Button-1>', clear_canvas1)



w.mainloop()
