from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
kit = MotorKit()
 
for i in range(1000):
    # kit.stepper2.onestep()
    kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
