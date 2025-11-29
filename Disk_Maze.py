#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

brain=Brain()

# Robot configuration code
left_drive_smart = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
right_drive_smart = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 1)
Armmotor = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
Clawmotor = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)
# vex-vision-config:begin
vision_16__SIG_RED = Signature(1, 6865, 7229, 7047,249, 585, 417,5.7, 0)
vision_16__SIG_BLUE = Signature(2, -3897, -3589, -3743,6873, 7645, 7259,5.9, 0)
vision_16__SIG_GREEN = Signature(3, -3681, -3389, -3535,-3155, -2855, -3005,9.6, 0)
vision_16 = Vision(Ports.PORT16, 50, vision_16__SIG_RED, vision_16__SIG_BLUE, vision_16__SIG_GREEN)
# vex-vision-config:end

wait(30, MSEC)


def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

wait(200, MSEC)

print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# Project: VEXcode Project
#	Author:Barbara Ramirez       VEX
#	Created: 04/08/25
#	Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code


Armmotor.spin_for(FORWARD, 120, DEGREES)


while True:

    vision_object = vision_16.take_snapshot(vision_16__SIG_BLUE)
    vision_object1 = vision_16.take_snapshot(vision_16__SIG_RED)
    vision_object2 = vision_16.take_snapshot(vision_16__SIG_GREEN)
    
    drivetrain.drive(FORWARD)
    
    
    if vision_object is not None:
        brain.screen.clear_row(1)
        brain.screen.set_cursor(1, 1)
        width1 = vision_16.largest_object().width
        if width1 > 200:
            drivetrain.stop()
            wait(0.4, SECONDS)
            drivetrain.turn_for(LEFT, 90, DEGREES)
        wait(0.2, SECONDS)

    if vision_object1 is not None:
        brain.screen.clear_row(1)
        brain.screen.set_cursor(1, 1)
        width2 = vision_16.largest_object().width
        if width2 > 200:
            drivetrain.stop()
        wait(0.2, SECONDS)

    if vision_object2 is not None:
        brain.screen.clear_row(1)
        brain.screen.set_cursor(1, 1)
        width3 = vision_16.largest_object().width
        if width3 > 200:
            drivetrain.stop()
            wait(0.4, SECONDS)
            drivetrain.turn_for(RIGHT, 90, DEGREES)

            
        wait(0.2, SECONDS)

    
