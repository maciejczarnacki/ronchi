# class generating ronchigram
import math

EPSILON = 0.0001

class Ronchigram:
    # resolution - is a parameter defining size of the ronchigram, default value is 500, this give us image of 500x500 pixel size
    def __init__(self, ac_mode = False, resolution = 500):
        self.resolution = resolution
        self.ac_mode = ac_mode
    
    # sagitta function is used for concave mirror surface generation (conic section)     
    def sagitta(self, r, radius_of_curvature, conicity):
        S = r**2/(radius_of_curvature * (1 + (1 - r**2/radius_of_curvature**2 * (conicity + 1))**0.5))
        return S

    # focus_and radii methode calculates focal point and radius of curvatore for any given mirror surface point
    # it is necessary in raytracing and ronchigram generation
    def focus_and_radii_infinity(self, r, radius, conicity):
        S1 = self.sagitta(r, radius, conicity)
        S2 = self.sagitta(r + EPSILON, radius, conicity)
        aX = (S1 - S2)/EPSILON
        # bX = S2 - (S1 - S2)/EPSILON * r
        a_pX = 1 / aX
        b_pX = (S1 + S2)/2 - a_pX * (r + 0.5 * EPSILON)
        angleX = math.atan(a_pX) - 2 * math.pi * 90/360
        angle_fX = math.atan(a_pX) + angleX
        a_fX = math.tan(angle_fX)
        b_fX = (S1 + S2)/2 - a_fX * (r + 0.5 * EPSILON)
        return b_fX, b_pX
    
    # methode generating of the ronchigram in at focus Ronchi test        
    def generate_ronchigram_at_focus(self, roc, diameter, conicity, grating_lines, ronchi_phase, delta):
        if self.ac_mode:
            conicity = 2 * conicity + 1
        ronchigram = [[1 for x in range(self.resolution)] for y in range(self.resolution)]
        W = 1/(2 * grating_lines)
        for i in range(self.resolution):
            for j in range(self.resolution):
                X = (i - self.resolution / 2) * diameter / self.resolution
                Y = (j - self.resolution / 2) * diameter / self.resolution
                S2 = X*X + Y*Y
                if math.sqrt(S2) < diameter / 2:
                    SAG = self.sagitta(X, roc, conicity)
                    r_and_f = self.focus_and_radii_infinity(S2**0.5, roc, conicity)
                    actual_focus = r_and_f[0]
                    U = X * (delta + roc/2 - actual_focus)/(actual_focus - SAG)
                    FL = 0
                    si = (math.sin(math.pi * U * grating_lines - ronchi_phase))**2
                    if si <= 0.5:
                        FL = 1
                    if FL != 0:
                        ronchigram[j][i] = 0
        return ronchigram
    
    #methode generating of the ronchigram in at center of curvature (or "roc") Ronchi test
    def generate_ronchigram_at_roc(self, roc, diameter, conicity, grating_lines, ronchi_phase, delta):
        ronchigram = [[1 for x in range(self.resolution)] for y in range(self.resolution)]
        W = 1/(2 * grating_lines)
        for i in range(self.resolution):
            for j in range(self.resolution):
                X = (i - self.resolution / 2) * diameter / self.resolution
                Y = (j - self.resolution / 2) * diameter / self.resolution
                S2 = X*X + Y*Y
                if math.sqrt(S2) < diameter / 2:
                    Z = roc + S2/roc * (-1) * conicity
                    L = roc + 2 * delta - Z
                    U = L * X/Z
                    FL = 0
                    si = (math.sin(math.pi * U * grating_lines - ronchi_phase))**2
                    if si <= 0.5:
                        FL = 1
                    if FL != 0:
                        ronchigram[j][i] = 0
        return ronchigram
    
    # wavefront error calculation from OPD equation for at focus test      
    def wavefront_error_calculation_at_focus(self, wavelength, roc, diameter, conicity):
        p_v = abs(1 + conicity)*diameter**4 / 256 / roc**3 / (wavelength * 10**(-6))
        rms = p_v / 3.51
        strehl = (1 - 2 * math.pi**2 * rms * rms)**2
        return round(p_v, 3), round(rms, 3), round(strehl, 3)
    
    # wavefront error calculation from OPD equation for at "roc" test
    def wavefront_error_calculation_at_roc(self, wavelength, roc, diameter, conicity):
        p_v = abs(conicity) * diameter**4 / 256 / roc**3 / (wavelength * 10**(-6))
        rms = p_v / 3.51
        strehl = (1 - 2 * math.pi**2 * rms * rms)**2
        return round(p_v, 3), round(rms, 3), round(strehl, 3)    
        
          
    
    
