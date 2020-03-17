import time
import pygubu
import tk_tools
from tkinter import *
from pyfirmata import Arduino as arduino, util


builder = builder = pygubu.Builder()
builder.add_from_file('pygubu_arduino_03.ui')
window = builder.get_object('mainwindow')

frm_pin_mode = builder.get_object('frm_pin_mode')
lbl_analog_input = builder.get_object('lbl_analog_input')
lbl_digital_input = builder.get_object('lbl_digital_input')
lbl_digital_optput = builder.get_object('lbl_digital_optput')
lbl_digital_pwm = builder.get_object('lbl_digital_pwm')
spnbox_pin_number_1 = builder.get_object('spnbox_pin_number_1')
spnbox_pin_number_2 = builder.get_object('spnbox_pin_number_2')
spnbox_pin_number_3 = builder.get_object('spnbox_pin_number_3')
spnbox_pin_number_4 = builder.get_object('spnbox_pin_number_4')
btn_set_1 = builder.get_object('btn_set_1')
btn_set_2 = builder.get_object('btn_set_2')
btn_set_3 = builder.get_object('btn_set_3')
btn_set_4 = builder.get_object('btn_set_4')

frm_canvas = builder.get_object('frm_canvas')
frm_1 = builder.get_object('frm_1')
frm_2 = builder.get_object('frm_2')
frm_3 = builder.get_object('frm_3')
lbl_device_1 = builder.get_object('lbl_device_1')
lbl_device_2 = builder.get_object('lbl_device_2')
lbl_device_3 = builder.get_object('lbl_device_3')
lbl_device_4 = builder.get_object('lbl_device_4')
lbl_sldbar_4_value = builder.get_object('lbl_sldbar_4_value')
canvas_1 = builder.get_object('canvas_1')
canvas_2 = builder.get_object('canvas_2')
canvas_3 = builder.get_object('canvas_3')
pgsbar_1 = builder.get_object('pgsbar_1')
pgsbar_2 = builder.get_object('pgsbar_2')
pgsbar_3 = builder.get_object('pgsbar_3')
sldbar_4 = builder.get_object('sldbar_4')

r_sld_device1 = tk_tools.RotaryScale(canvas_1,max_value=255, size=99, img_data=tk_tools.images.rotary_gauge_bar)
led_device2 = tk_tools.Led(canvas_2, size=99)
led_device3 = tk_tools.Led(canvas_3, size=99)
r_sld_device1.pack()
led_device2.pack()
led_device3.pack()

frm_board_info = builder.get_object('frm_board_info')
lbl_board_info = builder.get_object('lbl_board_info')
txtbox_port = builder.get_object('txtbox_port')
btn_port_set = builder.get_object('btn_port_set')
frm_fasele = builder.get_object('frm_fasele')
lbl_connection = builder.get_object('lbl_connection')
lbl_connection_status = builder.get_object('lbl_connection_status')


def btn_port_set_click(event):
    def func_msgbox_destroy():
        msgbox.destroy()
    
    msgbox = Message(window, width=300)
    msgbox['text'] = 'Waitting ...'
    msgbox.grid(row=4, column=1)

    port = txtbox_port.get()
    try:
        global board
        board = arduino(port)
        iterator = util.Iterator(board)
        iterator.start()
        lbl_connection_status['text'] = 'Connected'
        frm_fasele['bg'] = 'blue'
        msgbox['text'] = 'Connected'
        msgbox.grid(row=4, column=1)
        msgbox.after(2500, func_msgbox_destroy)
    except:
        lbl_connection_status['text'] = 'DisConnected'
        frm_fasele['bg'] = 'red'
        msgbox['text'] = 'Can`t Connect. Port Name Can`t Find.'
        msgbox.grid(row=4, column=1)
        msgbox.after(5000, func_msgbox_destroy)

def btn_set_1_click(pin_num):
    global device1
    device1 = board.get_pin(f'a:{pin_num}:i')

def btn_set_2_click(pin_num):
    global device2
    device2 = board.get_pin(f'd:{pin_num}:i')

def btn_set_3_click(pin_num):
    global device3, led_device3_on
    device3 = board.get_pin(f'd:{pin_num}:o')
    led_device3_on = False

def btn_set_4_click(pin_num):
    global device4
    device4 = board.get_pin(f'd:{pin_num}:p')

def led_device3_clicked():
    if led_device3_on == False:
        device3.write(1)
        led_device3.to_green()
        led_device3_on = True
    elif led_device3_on == True:
        device3.write(0)
        led_device3.to_red()
        led_device3_on = False

def window_data_update():
    r_sld_device1.set_value(device1.read() * 255)
    if device2.read() == 0: led_device2.to_red()
    elif device2.read() == 1: led_device2.to_green()
    device4.write(sldbar_4.get() / 255)

    window.after(250, window_data_update)


btn_port_set.bind('<ButtonPress-1>', btn_port_set_click)
btn_set_1.bind('<ButtonPress-1>', btn_set_1_click(spnbox_pin_number_1.get()))
btn_set_2.bind('<ButtonPress-1>', btn_set_2_click(spnbox_pin_number_2.get()))
btn_set_3.bind('<ButtonPress-1>', btn_set_3_click(spnbox_pin_number_3.get()))
btn_set_4.bind('<ButtonPress-1>', btn_set_4_click(spnbox_pin_number_4.get()))
led_device3.bind('<ButtonPress-1>', led_device3_clicked)

window.after(1, window_data_update)
window.mainloop()
