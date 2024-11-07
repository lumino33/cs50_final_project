import numpy as np 

from config import G, COLLISION_THRESHOLD

class Object:
    def __init__(self, weight, v0, angle, initial_x, initial_y, is_movable, radius):
        self.weight = weight
        self.v0 = v0
        self.angle = self.degree2radian(angle)

        self.x = initial_x
        self.y = initial_y
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.is_movable = is_movable

        self.radius = radius

        self.trace = []

    def move(self, new_x, new_y):
        self.trace.append([int(self.x), int(self.y)])
        self.x = new_x
        self.y = new_y
    
    def get_distance(self, second_object):
        return np.linalg.norm(np.array([self.x, self.y]) - np.array([second_object.x, second_object.y]))
    
    def is_collided(self, second_object):
        
        distance = self.get_distance(second_object)
        if distance - (self.radius + second_object.radius) <= COLLISION_THRESHOLD:
            return True
        else:
            return False

    def get_position_at_t(self, t):
        if self.is_movable:
            new_x = self.initial_x + self.v0 * np.cos(self.angle) * t
            new_y = self.initial_y + self.v0 * np.sin(self.angle) * t - 0.5 * G * np.power(t, 2)
            return new_x, new_y
        else:
            return self.x, self.y
        
    def degree2radian(self, degree):
        return np.radians(degree)
    
    def radian2degree(self, radian):
        return np.rad2deg(radian)

class ArtilleryShell(Object):
    pass
        
class Objective(Object):
    pass