'''Flight simulator. 
Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
The program should print out current orientation, and applied tilt correction. 
The program should run in infinite loop, until user breaks the loop. 
Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
With every simulation step the orentation should be corrected, applied and printed out.
Additional:
+ use format for strings
+ two classes
	- separate plane, simulation
	- use generator
+ use PEP8
+ CLI (command line interface)
+ use __name__ == "__main__"
-no semicolons
'''

import random


class Plane(object):
    def __init__(self, angle):
        self.angle = angle

    def adjust_tilt(self):
        self.angle -= self.angle

    def generate_tilt(self):
        self.angle = random.gauss(0, 1)


class Simulation(object):
    def __init__(self, plane):
        self.plane = plane

    def simulate(self):
		print "Current plane angle is: {} degrees\nCorrection needed: {}\n".format(self.plane.angle, -self.plane.angle)
		self.plane.adjust_tilt()
		print "Tilt correction was successful, psicion after adjustments: {}\n".format(self.plane.angle)
		self.plane.generate_tilt()
		print "*" * 60
        
    def end_simulation(self):
        print "Simulation is ended!"

if __name__ == "__main__":
    angle = random.gauss(0, 1)
    plane = Plane(angle)
    simulation = Simulation(plane)
    
    while True:
	print "Press 1 for tilt correction"
	print "Press 2 to exit"
	menu_option = input("Choose an option\n>>")
	if(menu_option == 1):
		simulation.simulate()
	elif(menu_option == 2): 
		simulation.end_simulation()
		break
