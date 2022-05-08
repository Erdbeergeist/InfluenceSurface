import numpy as np

class PointObject():

    def __init__(self,
                 x = np.array([0,0,0]),
                 v = np.array([0,0,0]),
                 a = np.array([0,0,0]),
                 t = 0):

        self.x = x
        self.v = v
        self.a = a

        self.t = 0
        self.update_counter = 0 
        self.update_function = lambda ti, *kwargs: self

    def __repr__(self):
        return f'x : {self.x}\nv : {self.v}\na : {self.a}\nt : {self.t}\nc : {self.update_counter}'

    def update(self,
               ti,
               *kwargs):
        
        self.update_function(ti, self, *kwargs)
        self.update_counter += 1
        return self

    def register_update_function(self,
                                 update_function):

        self.update_function = update_function
        return update_function
    

class ObjectHandler():
    
    def __init__(self):
        self.objects = []


def postion_updater(ti, object):
    dt = (ti - object.t)
    object.x = object.x + object.v * dt + 0.5 * object.a * dt * dt
    object.v = object.v + object.a * dt
    object.t = object.t + dt
    return 0
     

p = PointObject(v = np.array([1,0,0]))

print(p)

p.register_update_function(postion_updater)

print(p.update(1).update(1))
