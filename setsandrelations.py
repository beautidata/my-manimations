from manim import *

'''
Draws two ellipses and a bijection between them
'''
class Bijection(Scene):
    def construct(self):

        left_center = np.array((-3, -1, 0))
        left_ellipse = Ellipse(arc_center=left_center, height=4.0, color=BLUE)
        left_ellipse_label = Text('B')
        left_ellipse_label.move_to(2*UP+3*LEFT)

        right_center = np.array((3, -1, 0))
        right_ellipse = Ellipse(arc_center=right_center, height=4.0)
        right_ellipse_label = Text('D')
        right_ellipse_label.move_to(2*UP+3*RIGHT)

        self.play(FadeIn(left_ellipse))
        self.play(FadeIn(right_ellipse))
        self.play(FadeIn(left_ellipse_label))
        self.play(FadeIn(right_ellipse_label))

        dots = []
        points = np.array([(-3, 0, 0),(-3,-1,0), (-3, -2, 0),(3,0,0), (3,-1,0), (3,-2,0)])
        for point in points:
            dot = Dot(point=point)
            self.play(FadeIn(dot))

        line1 = Arrow(start=points[0], end=points[3])
        line2 = Arrow(start=points[1], end=points[4])
        line3 = Arrow(start=points[2], end=points[5])

        self.play(FadeIn(line1))
        self.play(FadeIn(line2))
        self.play(FadeIn(line3))

        title = Text("BIJECTION betweeen B and D")
        title.move_to(3.1*UP)
        self.play(Create(title))