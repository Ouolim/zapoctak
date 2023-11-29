import manim
from manim import *


class FindInWheat(Scene):
	def construct(self):
		with open("data.txt", "r") as f:
			try:
				jehla = f.readline().strip()
				seno = f.readline()
			except FileNotFoundError:
				print("Soubor data.txt neexistuje")
				exit(1)

		# Animace Vstupu - nakreslení koleček a šipek
		vstup_t = Text(seno)
		self.play(Write(vstup_t))
		self.wait(1)
		senoCircles = [Circle(color=WHITE, radius=0.4).shift(LEFT * 5 + RIGHT * 1.1 * i) for i in range(len(seno))]
		senoPismenka_tmp = [Text(seno[i]).move_to(senoCircles[i]) for i in range(len(seno))]
		senoPismenka = [Text(seno[i]).move_to(senoCircles[i]) for i in range(len(seno))]
		senoLines = [
			Arrow(buff=1, start=i.get_right(), end=senoCircles[j + 1].get_left())
			for j, i in enumerate(senoCircles[:-1])
		]

		gseno = VGroup(*senoCircles, *senoPismenka, *senoLines)
		# aby se pismenka posouvali na pismenka a ne na kruhy+pismenka,
		gsenopismenka = VGroup(*senoPismenka_tmp)

		self.play(Transform(vstup_t, gsenopismenka))
		self.play(FadeIn(gseno), FadeOut(vstup_t))
		self.wait(1)
		self.play(gseno.animate.shift(UP * 3))

		# Animace jehly
		jehla_t = Text(jehla)
		self.play(Write(jehla_t))
		self.wait(1)
		jehlaCircles = [Circle(color=WHITE, radius=0.4).shift(LEFT*5 + RIGHT*1.1*i) for i in range(len(jehla)+1)]
		jehlaPismenka_tmp = [Text(jehla[i]).move_to(jehlaCircles[i+1]) for i in range(len(jehla))]
		jehlaPismenka = [Text(jehla[i]).move_to(jehlaCircles[i+1]) for i in range(len(jehla))]

		epsilon = MathTex(r"\epsilon")
		epsilon.move_to(jehlaCircles[0])
		gjehla = VGroup(*jehlaCircles, *jehlaPismenka, epsilon)
		# aby se pismenka posouvali na pismenka a ne na kruhy+pismenka,
		gjehlapismenka = VGroup(*jehlaPismenka_tmp)
		self.play(Transform(jehla_t, gjehlapismenka))
		self.play(FadeIn(gjehla), FadeOut(jehla_t))
		self.wait(1)
		self.wait(5)

