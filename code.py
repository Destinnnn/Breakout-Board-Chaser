import time
import time
import time
import time
import board
import digitalio
import pwmio

from adafruit_motor import motor #Imports a function from the adafruit_motor library

right_motor_forward = board.GP12 # Initializes the variable left_motor_forward and attaches it to GP12
right_motor_backward = board.GP13 #Initializes the variable left_motor_backward and attaches it to GP13
left_motor_forward = board.GP14
left_motor_backward = board.GP15

pwm_Ra = pwmio.PWMOut(right_motor_forward, frequency=10000) #Tells the controller that the motor is an input
pwm_Rb = pwmio.PWMOut(right_motor_backward, frequency=10000) #Tells the controller that the motor is an output
pwm_La = pwmio.PWMOut(left_motor_forward, frequency=10000)
pwm_Lb = pwmio.PWMOut(left_motor_backward, frequency=10000)


Right_Motor = motor.DCMotor(pwm_Ra, pwm_Rb) #Configuration line (it is required)
Right_Motor_speed = 0 #Initializes the variable left_motor_forward and starts it at 0
Left_Motor = motor.DCMotor(pwm_La, pwm_Lb)
Left_Motor_speed = 0

while True:

    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(2)
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(2)
    Right_Motor_speed = -1
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(2)
    Right_Motor_speed = 1
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(2)
