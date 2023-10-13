# class generating ronchigram
import math
import numpy as np


EPSILON = 0.0001

class Ronchigram:
    def __init__(self, ac_mode = False, resolution = 300):
        self.resolution = resolution
        self.ac_mode = ac_mode
        
    def sagitta(self, r, radius_of_curvature, conicity):
        S = r**2/(radius_of_curvature * (1 + (1 - r**2/radius_of_curvature**2 * (conicity + 1))**0.5))
        return S

    def focus_and_radii(self, r, radius, conicity):
        S1 = self.sagitta(r, radius, conicity)
        S2 = self.sagitta(r + EPSILON, radius, conicity)
        aX = (S1 - S2)/EPSILON
        # bX = S2 - (S1 - S2)/EPSILON * r
        a_pX = 1 / aX
        b_pX = (S1 + S2)/2 - a_pX * (r + 0.5*EPSILON)
        angleX = math.atan(a_pX) - 2 * math.pi * 90/360
        angle_fX = math.atan(a_pX) + angleX
        a_fX = math.tan(angle_fX)
        b_fX = (S1 + S2)/2 - a_fX * (r + 0.5*EPSILON)
        return (round(b_pX,5)), (round(b_fX,5))
            
    def generate_ronchigram(self, roc, diameter, conicity, grating_lines, ronchi_phase, delta):
        if self.ac_mode:
            conicity = 2*conicity + 1
        ronchigram = np.ones((2*self.resolution, 2*self.resolution))
        # ronchigram = [[0]*(2*self.resolution)]*(2*self.resolution)
        W = 1 / (2 * grating_lines)
        for i in range(0, 2*self.resolution):
            for j in range(0, 2*self.resolution):
                X = (i - self.resolution) * diameter / (2*self.resolution)
                Y = (j - self.resolution) * diameter / (2*self.resolution)
                S2 = X*X + Y*Y
                if math.sqrt(S2) < diameter / 2:
                    SAG = self.sagitta(X, roc, conicity)
                    r_and_f = self.focus_and_radii(S2**0.5, roc, conicity)
                    actual_focus = r_and_f[1]
                    U = X * (delta + roc/2 - actual_focus)/(actual_focus - SAG)
                    FL = 0
                    si = (math.sin(math.pi * U * grating_lines - ronchi_phase))**2
                    if si <= 0.5:
                        FL = 1
                    if FL != 0:
                        ronchigram[j][i] = 0
        return ronchigram
        
          
    
    