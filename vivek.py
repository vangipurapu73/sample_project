from machine import Pin, Timer

led = Pin(25, Pin.OUT)
tim = Timer()

def tick(timer):
    global led
    led.toggle()
    print('Toggle LED')

tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)