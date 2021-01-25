from manimlib.imports import *
from manimlib.plugins_munir.point_generator import *

class pi(Scene):
    def construct(self):
        c=0
        L=1
        circ=Circle(color=PURPLE).scale(2)
        square=Square(color=BLUE_E).scale(2)
        self.play(ShowCreation(circ),ShowCreation(square))
        discrp=TextMobject("R= number of points inside circle divided by total number of points}").scale(0.7)
        discrp.set_color_by_gradient(BLUE_E,RED)
        self.play(Write(discrp.to_corner(DL)))
        points=rand_points.generate_rand_points(-2,2,111,RED)
        count=TexMobject("4R=",str(c)).to_edge(UP)
        count.add_updater(lambda u: u.become(TexMobject("4R=",str(4*c/L)).to_edge(UP)))
        self.add(count)
        self.play(Write(count))
        index=0
        
        for i in points:
            
            index+=1
            self.play(ShowCreation(i),run_time=0.2)
            if rand_points.rand_dist_origin(points)[index-1]<2:
               c+=1        
            else:
                c+=0
            if index>1:
                L+=1
            else:
                L+=0
            self.wait(0.8)
        self.wait(5)

class goodbye(Scene):
	def construct(self):
	      	bye_1=TexMobject("4\\cdot R=3.14563..","\\approx\\pi").scale(2)
	      	bye_1.set_color_by_gradient(BLUE_A,BLUE_E)
	      	self.play(Write(bye_1[0]))
	      	self.wait(0.8)
	      	self.play(Write(bye_1[1]))
	      	self.wait()

	      	quote=TextMobject("I know numbers are beautiful.\\\\ If they aren't then nothing is").scale(2)
	      	quote.set_color_by_gradient(BLUE_A,BLUE_E)
	      	erdos=TextMobject("Paul Erdos").scale(2)
	      	erdos.set_color_by_gradient(RED,PINK)  
	      	self.play(Transform(bye_1,quote))
	      	self.wait(0.5)
	      	self.play(Write(erdos.next_to(quote,DOWN)))
	      	self.wait(5)  


class s1_(Scene):
	"""docstring for s1_"""
	def construct(self):
	      	bye_1=TexMobject("\\text{Calulating }\\pi \\text{ with 100 randomly generated points}").scale(1.2)
	      	bye_1.set_color_by_gradient(BLUE_E,PINK)
	      	self.play(Write(bye_1))
	      	self.wait(3)