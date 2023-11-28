import manim
from manim import *

class FindInWheat(Scene):
	def construct(self):
		with open("data.txt", "r") as f:
			try:
				jehla = f.readline()
				seno = f.readline()
			except FileNotFoundError:
				print("Soubor data.txt neexistuje")
				exit(1)
		vstup = Text(seno)
		self.play(Write(vstup))
		self.wait(1)
		senoCircles = [Circle(color=WHITE, radius=0.5).shift(LEFT * 5 + RIGHT *1.3 *i) for i in range(len(seno))]
		senoPismenka_tmp = [Text(seno[i]).move_to(senoCircles[i]) for i in range(len(seno))]
		senoPismenka = [Text(seno[i]).move_to(senoCircles[i]) for i in range(len(seno))]
		Gseno = VGroup(*senoCircles, *senoPismenka)

		#aby se pismenka posouvali na pismenka a ne na kruhy+pismenka,
		Gpismenka = VGroup(*senoPismenka_tmp)
		self.play(Transform(vstup, Gpismenka))

		self.play(FadeIn(Gseno), FadeOut(vstup))
		self.wait(1)
		self.play(Gseno.animate.shift(UP*3))

