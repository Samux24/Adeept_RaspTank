# File name: avoid.py
# Description: Detect obstacles and avoid collisions
# Author: Irving (irvi3nggasimov@gmail.com)
# Date: 2023/02/07

import time, ultra_ICEP, move
"Set speed"
speed_set_forward = 60
speed_set_turn = 80

"Create function to avoid obstacles"
def avoid():
    while True:
        distance = ultra_ICEP.checkdist()*100 # Measure distance
        time.sleep(0.1)

        if distance > 0 and distance > 25:   # Move forward as long as distance > 25cm
            move.move(speed_set_forward, 'forward', 'no', 0.8)
        elif distance > 0 and distance <= 25: # Stop when distance <= 25cm
            move.motorStop()
            time.sleep(0.3)
            while distance > 0 and distance <= 25:
                move.move(speed_set_turn, 'no', 'right', 0.8) # Move robot to the left 90deg
                time.sleep(1)
                move.motorStop()
                distance = ultra_ICEP.checkdist()*100 # Measure distance
                time.sleep(0.1)

if __name__ == '__main__':
    ultra_ICEP.setup()
    move.setup()
    time.sleep(20) # Delay time to disconect eth cable
    avoid()
