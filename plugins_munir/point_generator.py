from manimlib.imports import *
import numpy as np
class rand_points():
    def generate_rand_points(m,n,x,color):
        points=[]
        p=[m,n]
        for i in range(0,x):
            p_=[p[np.random.randint(2)]*np.random.random(),p[np.random.randint(2)]*np.random.random(),0]
            p__=Dot(np.array(p_)).set_color(color)
            points.append(p__)
        return points
    def rand_dist_origin(points):
        dist=[]
        for i in points:
            x=i.get_center()[0]
            y=i.get_center()[1]

            r=(x**2+y**2)**(1/2)
            dist.append(r)
        return dist
            

       





