from manimlib.imports import *
from math import *
import numpy as np
import random as r

def add_points(m,n,x):
	
	p=[m,n]
	d_coord1=[p[np.random.randint(2)]*np.random.random(),p[np.random.randint(2)]*np.random.random(),0]
	d_coord2=[p[np.random.randint(2)]*np.random.random(),p[np.random.randint(2)]*np.random.random(),0]
	d_coord3=[p[np.random.randint(2)]*np.random.random(),p[np.random.randint(2)]*np.random.random(),0]
	d_coord4=[p[np.random.randint(2)]*np.random.random(),p[np.random.randint(2)]*np.random.random(),0]
	d_coord5=[p[np.random.randint(2)]*np.random.random(),p[np.random.randint(2)]*np.random.random(),0]

	d1=Dot(np.array(d_coord1)).set_color(RED)
	d2=Dot(np.array(d_coord2)).set_color(RED)
	d3=Dot(np.array(d_coord3)).set_color(RED)
	d4=Dot(np.array(d_coord4)).set_color(RED)
	d5=Dot(np.array(d_coord5)).set_color(RED)
	point_group=VGroup(d1,d2,d3,d4,d5)
	if x==2:
		return VGroup(d1,d2)
	else:
		return point_group


def add_points_list(m,n):
	
	p=[m,n]
	d_coord1=[p[np.random.randint(2)]*np.random.random(),p[np.random.randint(2)]*np.random.random(),0]
	d_coord2=[p[np.random.randint(2)]*np.random.random(),p[np.random.randint(2)]*np.random.random(),0]
	d_coord3=[p[np.random.randint(2)]*np.random.random(),p[np.random.randint(2)]*np.random.random(),0]
	d_coord4=[p[np.random.randint(2)]*np.random.random(),p[np.random.randint(2)]*np.random.random(),0]
	d_coord5=[p[np.random.randint(2)]*np.random.random(),p[np.random.randint(2)]*np.random.random(),0]

	d1=Dot(np.array(d_coord1)).set_color(RED)
	d2=Dot(np.array(d_coord2)).set_color(RED)
	d3=Dot(np.array(d_coord3)).set_color(RED)
	d4=Dot(np.array(d_coord4)).set_color(RED)
	d5=Dot(np.array(d_coord5)).set_color(RED)
	point_group=[d1,d2,d3,d4,d5]
	return point_group

#python -m manim projects\1991_japan_mo\japan_1.py -p -r 1080 --video_dir projects\1991_japan_mo\
#python -m manim projects\1991_japan_mo\japan_1.py -pl --video_dir projects\1991_japan_mo\
class pigeonhole(Scene):

	def  construct(self):
		self.intro_1()
		self.example_1()
		self.concl_exp()
	def intro_1(self):
		title=TextMobject("Pigeonhole Principle").set_color_by_gradient(BLUE,PURPLE)
		title2=TextMobject("Box Principle").set_color_by_gradient(PURPLE,BLUE)
		self.play(Write(title),run_time=2)
		self.wait()
		self.play(Transform(title,title2),run_time=2)

		self.play(ApplyMethod(title.to_edge,UP))

		ball_1=Circle(color=BLUE,fill_opacity=.8).scale(0.3)
		ball_2=ball_1.copy().shift(RIGHT)
		ball_3=ball_1.copy().shift(LEFT)
		self.play(ShowCreation(ball_1))
		self.wait()
		self.play(ReplacementTransform(ball_1.copy(),ball_2),ReplacementTransform(ball_1.copy(),ball_3),run_time=2)
		self.wait()
		box1=Square().scale(2)
		box2=box1.copy()
		self.play(ShowCreation(box1.to_corner(DR)),ShowCreation(box2.to_corner(DL)))
		self.wait()

		#Transformations#

		self.play(ApplyMethod(ball_2.move_to,box1.get_center()),ApplyMethod(ball_3.move_to,box2.get_center()),run_time=3)
		self.wait(3)
		self.play(ApplyMethod(ball_1.move_to,box1.get_center()+UP))
		self.wait(3)
		self.play(ApplyMethod(ball_1.move_to,box2.get_center()+UP))
		self.wait(3)
		self.play(ApplyMethod(ball_1.move_to,box1.get_center()+UP),ApplyMethod(ball_3.move_to,box1.get_center()+DOWN),run_time=2)
		self.wait()

		ball_group=VGroup(ball_1,ball_2,ball_3)
		self.play(ApplyMethod(ball_group.move_to,box2.get_center()),run_time=2)
		self.wait()
		self.play(ApplyMethod(ball_group.move_to,ORIGIN),run_time=2)
		self.wait(2)		

		box_group=VGroup(box1,box2)
		self.play(FadeOut(ball_group),FadeOut(box_group))

		Principle=TexMobject("\\text{If we have m balls and n boxes, and }m>n\\text{ then,}\\\\ \\text{one of the boxes will contain at least 2 balls} ")
		self.play(Write(Principle),run_time=3)
		self.wait(2)
		self.play(FadeOut(Principle),FadeOut(title))
		self.wait(3)

	def example_1(self):
		question=TextMobject("Show that if you randomly draw 5 points inside a 2 by 2 square \\\\ you will always find 2 points such that they are at most 1.7 units apart.").scale(.7)
		self.play(Write(question))
		self.wait(5)
		self.play(FadeOut(question))
		square_1=Square().scale(2)
		#plane=NumberPlane()
		#self.play(ShowCreation(plane))
		self.wait(2)
		self.play(ShowCreation(square_1))
		self.wait(2)
		points=add_points(-2,2,5)
		self.play(ShowCreation(points),run_time=0.3)
		self.wait(5)

		square_2=Square(color=BLUE_B,fill_opacity=0.3).move_to(1*UP+1*RIGHT)
		square_3=Square(color=BLUE_B,fill_opacity=0.3).move_to(-1*UP+1*RIGHT)
		square_4=Square(color=BLUE_B,fill_opacity=0.3).move_to(-1*UP+-1*RIGHT)
		square_5=Square(color=BLUE_B,fill_opacity=0.3).move_to(1*UP+-1*RIGHT)
		squares=[square_5,square_2,square_3,square_4]
		squares_1=VGroup(square_5,square_2,square_3,square_4)
		for k in squares:
			k.set_color(BLUE_E)
			self.play(ShowCreation(k),run_time=0.5)
		self.wait(3)

		square_4_=Square(color=BLUE_B,fill_opacity=0.3).to_corner(DL)
		square_5_=Square(color=BLUE_B,fill_opacity=0.3).to_corner(UL)
		square_3_=Square(color=BLUE_B,fill_opacity=0.3).to_corner(DR)
		square_2_=Square(color=BLUE_B,fill_opacity=0.3).to_corner(UR)
		squares_=[square_5_,square_2_,square_3_,square_4_]
		squares_2=VGroup(square_5_,square_2_,square_3_,square_4_)
		o=0
		for i in squares:
			self.play(ReplacementTransform(i.copy(),squares_[o]),run_time=0.5)
			o+=1
		self.wait(2)

		d1_=Dot().move_to(square_2_.get_center())
		d2_=Dot().move_to(square_4_.get_center())
		d3_=Dot().next_to(d2_,0.5*RIGHT)
		d4_=Dot().move_to(square_5_.get_center())
		d5_=Dot().next_to(d4_,0.5*RIGHT)

		point__group=VGroup(d1_,d2_,d3_,d4_,d5_).set_color(RED)

		self.play(ReplacementTransform(points.copy(),point__group))
		self.wait()

		self.play(FadeOut(points),FadeOut(point__group))

		points2=add_points(-2,2,5)
		self.play(ShowCreation(points2),run_time=0.3)
		self.wait(2)

		d1_2=Dot().move_to(square_4_.get_center())
		d2_2=Dot().move_to(square_3_.get_center())
		d3_2=Dot().next_to(d2_2,0.5*RIGHT)
		d4_2=Dot().move_to(square_5_.get_center())
		d5_2=Dot().next_to(d4_2,0.5*RIGHT)

		point__group2=VGroup(d1_2,d2_2,d3_2,d4_2,d5_2).set_color(RED)

		self.play(ReplacementTransform(points2.copy(),point__group2))
		self.wait(3)

		self.play(
			FadeOut(point__group2),
			FadeOut(points2),
			FadeOut(square_1),
			FadeOut(squares_2),
			FadeOut(squares_1)
			)
		
	def concl_exp(self):

		square=Square().scale(2)
		self.play(ShowCreation(square.set_color_by_gradient(BLUE_E,PURPLE)))
		self.wait()

		self.play(ShowCreationThenFadeOut(add_points(-2,2,2)),run_time=1)
		self.wait(0.5)
		self.play(ShowCreationThenFadeOut(add_points(-2,2,2)),run_time=1)
		self.wait(0.5)
		self.play(ShowCreationThenFadeOut(add_points(-2,2,2)),run_time=1)
		self.wait(0.5)
		self.play(ShowCreationThenFadeOut(add_points(-2,2,2)),run_time=1)
		self.wait(0.5)
		self.play(ShowCreationThenFadeOut(add_points(-2,2,2)),run_time=1)
		self.wait(0.5)
		c1,c2=Dot(np.array([1,0.79,0])).set_color(RED),Dot(np.array([-1.23,0.99,0])).set_color(RED)
		self.play(ShowCreation(c1),ShowCreation(c2))
		self.wait()
		self.play(ApplyMethod(c1.move_to,[2,-2,0]),ApplyMethod(c2.move_to,[-2,2,0]))
		self.wait(3)
		group1=VGroup(square,c1,c2)
		self.play(ApplyMethod(group1.to_edge,LEFT))
		self.wait()
		line=Line(start=c1.get_center(),end=c2.get_center())
		self.play(ShowCreation(line))
		self.wait()
		x_txt,y_txt=TexMobject("1 "),TexMobject("1 ")
		x_txt.move_to(square.get_center()+3*RIGHT)		
		y_txt.move_to(square.get_center()+2.25*DOWN)
		self.play(Write(x_txt),Write(y_txt))
		self.wait()
		group2=VGroup(x_txt,y_txt)
		pyth_txt=TexMobject("\\sqrt{1+1}=","\\sqrt{2}","<1.7").scale(1.5)
		pyth_txt.to_edge(UP)
		self.play(ReplacementTransform(group2.copy(),pyth_txt[0]))
		self.wait()
		self.play(Write(pyth_txt[1]))
		self.wait(5)	
		self.play(Write(pyth_txt[2]))
		self.wait(3)

		self.play(FadeOut(group1),FadeOut(group2),FadeOut(line),FadeOut(pyth_txt))
		concl=TexMobject("\\text{Thus, we will always get 2 points such that}\\\\\\text{they are at least 1.7 units apart}")
		concl.set_color_by_gradient(BLUE_E,RED)

		self.play(Write(concl))
		self.wait(5)




