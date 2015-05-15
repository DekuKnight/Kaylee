from bean.Door import Door
from bean.Light import Light

class Room:

    lights = []
    doors = []

    def __init__(self, lights = [], doors = []):
        self.lights = lights
        self.doors = doors

    def toString(self):
        print("Lights:")
        for light in self.lights:
            light.toString()
        print("Doors:")
        for door in self.doors:
            door.toString()
