from pyfirmata import Arduino as arduino, util
from tkinter import *
import pygubu


builder = builder = pygubu.Builder()
builder.add_from_file('pygubu_arduino_02.ui')
window = builder.get_object('mainwindow')

lbl1 = builder.get_object('lbl1')
lbl_poten1_value = builder.get_object('lbl_poten1_value')
btn_on_off = builder.get_object('btn_on_off')
lbl_on_off = builder.get_object('lbl_on_off')
sld_motor1 = builder.get_object('sld_motor1')


port = '/dev/ttyACM0'
board = arduino(port)
iterator = util.Iterator(board)
iterator.start()

poten1 = board.get_pin('a:0:i')
motor1 = board.get_pin('d:6:p')
motor2 = board.get_pin('d:5:p')

motor1_status = False


def btn_on_off_click(event):
    if not motor1_status:
        motor1.write(1)
        lbl_on_off['text'] = 'ON'
        sld_motor1.set(10)
        motor1_status = True
    else:
        motor1.write(0)
        lbl_on_off['text'] = 'OFF'
        sld_motor1.set(0)
        motor1_status = False

def sld_motor1_change(event):
    motor1.write(sld_motor1.get() / 10)
    if sld_motor1.get() > 0: lbl_on_off['text'] = 'ON'
    else: lbl_on_off['text'] = 'OFF'

def poten1_value_change():
    motor2.write(poten1.read())
    lbl_poten1_value['text'] = str(poten1.read())
    lbl_poten1_value.after(250, poten1_value_change)


btn_on_off.bind('<ButtonPress-1>', btn_on_off_click)
sld_motor1.bind('<B1-Motion>', sld_motor1_change)
sld_motor1.bind('<ButtonRelease-1>', sld_motor1_change)
lbl_poten1_value.after(1, poten1_value_change)


window.mainloop()
