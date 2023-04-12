import time
from machine import Pin,PWM

MIN_DUTY = 1000
MAX_DUTY = 9000

pwm = PWM(Pin(0,Pin.OUT))
pwm.freq(50)


# Function to set servo motor to 0 degrees
def set_servo_zero():
    pwm.duty_u16(2000)
    
# Function to set servo motor to 180 degrees
def set_servo_full():
    pwm.duty_u16(8300)
    
def set_servo_duty(n):
    pwm.duty_u16(n)
    
    
    



#     for _ in range(1024): #1024
#         duty += direction
#         
#         if duty > MAX_DUTY:
#             duty = MAX_DUTY
#             direction = -direction
#             time.sleep(1)
#         elif duty < MIN_DUTY:
#             duty = MIN_DUTY
#             direction = -direction
#             time.sleep(1)
#         pwm.duty_u16(duty)
        
        