__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_MotorKit.git"

import board
import busio
from adafruit_pca9685 import PCA9685


class MotorKit:
    """Class representing an Adafruit DC & Stepper Motor FeatherWing, Shield or Pi Hat kit.

       Automatically uses the I2C bus on a Feather, Metro or Raspberry Pi."""
    def __init__(self, address=0x60):
        self._motor1 = None
        self._motor2 = None
        self._motor3 = None
        self._motor4 = None
        self._stepper1 = None
        self._stepper2 = None
        i2c = busio.I2C(board.SCL, board.SDA)
        self._pca = PCA9685(i2c, address=address)
        self._pca.frequency = 1600

    # We can save memory usage (~300 bytes) by deduplicating the construction of the objects for
    # each motor. This saves both code size and the number of raw strings (the error message)
    # stored. The same technique is a net loss for stepper because there is less duplication.
    def _motor(self, motor_name, channels, stepper_name):
        from adafruit_motor import motor
        motor_name = "_motor" + str(motor_name)
        stepper_name = "_stepper" + str(stepper_name)
        if not getattr(self, motor_name):
            if getattr(self, stepper_name):
                raise RuntimeError(
                    "Cannot use {} at the same time as {}.".format(motor_name[1:],
                                                                   stepper_name[1:]))
            self._pca.channels[channels[0]].duty_cycle = 0xffff
            setattr(self, motor_name, motor.DCMotor(self._pca.channels[channels[1]],
                                                    self._pca.channels[channels[2]]))
        return getattr(self, motor_name)

    @property
    def motor1(self):
        return self._motor(1, (8, 9, 10), 1)

    @property
    def motor2(self):
        return self._motor(2, (13, 11, 12), 1)

    @property
    def motor3(self):
        return self._motor(3, (2, 3, 4), 2)

    @property
    def motor4(self):
        return self._motor(4, (7, 5, 6), 2)

    @property
    def stepper1(self):
        if not self._stepper1:
            from adafruit_motor import stepper
            if self._motor1 or self._motor2:
                raise RuntimeError("Cannot use stepper1 at the same time as motor1 or motor2.")
            self._pca.channels[8].duty_cycle = 0xffff
            self._pca.channels[13].duty_cycle = 0xffff
            self._stepper1 = stepper.StepperMotor(self._pca.channels[10], self._pca.channels[9],
                                                  self._pca.channels[11], self._pca.channels[12])
        return self._stepper1

    @property
    def stepper2(self):
        if not self._stepper2:
            from adafruit_motor import stepper
            if self._motor3 or self._motor4:
                raise RuntimeError("Cannot use stepper2 at the same time as motor3 or motor4.")
            self._pca.channels[7].duty_cycle = 0xffff
            self._pca.channels[2].duty_cycle = 0xffff
            self._stepper2 = stepper.StepperMotor(self._pca.channels[4], self._pca.channels[3],
                                                  self._pca.channels[5], self._pca.channels[6])
        return self._stepper2
