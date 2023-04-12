import network
from machine import Pin
from time import sleep
import urequests
import usocket as socket
import time
import blink
import servo


username = "wifi_username"
password = "wifi_password"

led_pin = Pin("LED",Pin.OUT)
led_pin.low()


HTML = """<!DOCTYPE html>
<html>
<head><title>Control Page</title></head>
<body>
<h1>Control Page</h1>
<p>Click the buttons below to control the device:</p>
<button onclick="on()">On</button>
<button onclick="off()">Off</button>
<script>
function on() {
  fetch('/on');
}
function off() {
  fetch('/off');
}
</script>
</body>
</html>
"""

def on():
    servo.set_servo_duty(3500)
def off():
    servo.set_servo_duty(6500)


# Set up WiFi connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(username, password)

#wlan.ifconfig(('192.168.1.155', '255.255.255.0', '192.168.1.1', '8.8.8.8'))

while not wlan.isconnected():
    print('Connecting to WiFi...')
    sleep(1)
print('Connected to WiFi')
print('IP address:', wlan.ifconfig()[0])


# Set up button and LED
button = Pin(14, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)

# Set up web server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
print('Web server started')
blink.n_blink(3)

# Define request handler function
def handle_request(conn):
    request = conn.recv(1024)
    request = str(request)
    method = request.split(' ')[0]
    try:
        url = request.split(' ')[1]
    except:pass
    
    if url == '/':
        
        conn.sendall(HTML)
        
    if "GET /off" in request:
        off()
    elif "GET /on" in request:
        on()



# Main loop
while True:
    conn, addr = s.accept()
    print('Connected by:', addr)
    handle_request(conn)
    conn.close()

