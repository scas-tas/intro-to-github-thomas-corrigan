from microbit import *
import machine

# Servo on Pin 0 | Sonar Trig on Pin 1 | Sonar Echo on Pin 2
def get_distance():
    pin1.write_digital(1)
    sleep(0.01)
    pin1.write_digital(0)
    duration = time_pulse_us(pin2, 1)
    if duration < 0:
        return 0
    return int((duration * 0.0343) / 2)

uart.init(baudrate=115200)
angle = 0
step = 1  # 1-degree increment for a slower, smooth sweep

while True:
    # Set servo PWM duty cycle for 0-180 degrees
    duty = int(25 + (angle / 180.0) * 90)
    pin0.set_analog_period(20)
    pin0.write_analog(duty)
    
    dist = get_distance()
    uart.write(str(angle) + "," + str(dist) + "\n")
    
    angle += step
    if angle >= 180 or angle <= 0:
        step = -step
        
    sleep(100)  # 100ms delay per step slows down physical hardware sweep