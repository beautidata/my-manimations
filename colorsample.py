from manim import *


def define_ellipse(x, y, z, color, opacity):
    center = np.array((x, y, z))
    ellipse = Ellipse(arc_center=center, color=color, opacity=opacity)
    return ellipse

'''
Draws two ellipses with different fills
'''
class ColorSample(Scene):


    def construct(self):
        '''
        x_vals = [-5, -2.5, 0, 2.5, 5]
        blues = [BLUE, BLUE, "#006DAA", "#061A40", "#061A40"]
        opacities = [0, 0.25, 0.5, 0.75, 1.0]
        ellipses = []

        for x in range(0,len(x_vals)):
            ellipse = define_ellipse(x_vals[x], 0, 0, BLUE, opacities[x])
            ellipses.append(ellipse)

        for e in ellipses:
            self.play(FadeIn(e))
        '''
        left_center1 = np.array((-4.5, 1, 0))
        left_ellipse1 = Ellipse(arc_center=left_center1, height=2.0, color="#006DAA")
        self.play(FadeIn(left_ellipse1))
        
        
        left_center2 = np.array((-2, 1, 0))
        left_ellipse2 = Ellipse(arc_center=left_center2, height=2.0, color="#006DAA")
        left_ellipse2.set_fill("#006DAA", opacity=0.25)
        self.play(FadeIn(left_ellipse2))

        center_center = np.array((0.5, 1, 0))
        center_ellipse = Ellipse(arc_center=center_center, height=2.0, color="#006DAA")
        center_ellipse.set_fill("#006DAA", opacity=0.5)
        self.play(FadeIn(center_ellipse))

        right_center1 = np.array((3, 1, 0))
        right_ellipse1 = Ellipse(arc_center=right_center1, height=2.0, color="#006DAA")
        right_ellipse1.set_fill("#006DAA", opacity=0.75)
        self.play(FadeIn(right_ellipse1))
        
        right_center2 = np.array((5.5, 1, 0))
        right_ellipse2 = Ellipse(arc_center=right_center2, height=2.0, color="#006DAA")
        right_ellipse2.set_fill("#006DAA", opacity=1.0)
        self.play(FadeIn(right_ellipse2))

        left_center1_bot = np.array((-4.5, -2, 0))
        left_ellipse1_bot = Ellipse(arc_center=left_center1_bot, height=2.0, color="#061A40")
        self.play(FadeIn(left_ellipse1_bot))
        
        left_center2_bot = np.array((-2, -2, 0))
        left_ellipse2_bot = Ellipse(arc_center=left_center2_bot, height=2.0, color="#061A40")
        left_ellipse2_bot.set_fill("#061A40", opacity=0.25)
        self.play(FadeIn(left_ellipse2_bot))

        center_center_bot = np.array((0.5, -2, 0))
        center_ellipse_bot = Ellipse(arc_center=center_center_bot, height=2.0, color="#061A40")
        center_ellipse_bot.set_fill("#061A40", opacity=0.5)
        self.play(FadeIn(center_ellipse_bot))

        right_center1_bot = np.array((3, -2, 0))
        right_ellipse1_bot = Ellipse(arc_center=right_center1_bot, height=2.0, color="#061A40")
        right_ellipse1_bot.set_fill("#061A40", opacity=0.75)
        self.play(FadeIn(right_ellipse1_bot))
        
        right_center2_bot = np.array((5.5, -2, 0))
        right_ellipse2_bot = Ellipse(arc_center=right_center2_bot, height=2.0, color="#061A40")
        right_ellipse2_bot.set_fill("#061A40", opacity=1.0)
        self.play(FadeIn(right_ellipse2_bot))

        text1 = Text('no fill')
        text1.move_to(3*UP+4.5*LEFT)
        self.play(FadeIn(text1))
        
    
