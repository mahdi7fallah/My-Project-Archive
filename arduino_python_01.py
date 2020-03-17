import time
try:
    from pyfirmata import Arduino as arduino, util
except:
    import pip
    pip.main(['install', 'pyfirmata'])


port = '/dev/ttyACM0'
board = arduino(port)
                                                    
iterator = util.Iterator(board)
iterator.start()

motor = board.get_pin('d:6:p')
poten = board.get_pin('a:0:i')

for i in range(500):
    motor.write(poten.read())
    time.sleep(0.01)
    print(i + 1, poten.read())
