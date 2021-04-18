from manim import *

'''
Draws a plane from (-7, 2.8) to (7, -4), creates a title, draws a ring between 1 and 2.
Erases ring, draws 4 points
'''
class DrawingShapes(Scene):
    def construct(self):

        

        plane = NumberPlane(axis_config={"number_scale_val": 0.1,}, y_max=2.8)
        self.play(FadeIn(plane))

        title = Title("Drawing Shapes")
        self.play(Create(title))

        annulus = Annulus()
        annulus.set_fill(YELLOW, opacity=0.6)
        self.play(FadeIn(annulus))
        self.play(FadeOut(annulus))

        dots = []
        points = np.array([(1,2,0), (2,1,0), (3,2,0), (4,1,0)])
        for point in points:
        	dot = Dot(point=point)
        	self.play(FadeIn(dot))