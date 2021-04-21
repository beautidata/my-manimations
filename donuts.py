from manim import *

class Donuts(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes()
        torus = Torus()
        self.set_camera_orientation(phi=180 * DEGREES, theta=30 * DEGREES)
        self.add(axes, torus)
        self.play(FadeIn(torus))