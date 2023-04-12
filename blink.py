import machine
import utime

led_pin = machine.Pin('LED',machine.Pin.OUT)
led_pin.low()
def n_blink(n):
    for i in range(n):
        led_pin.high()
        utime.sleep(0.5)
        led_pin.low()
        utime.sleep(0.5)