""" 
Ronchi test simulator for concave mirrors

Parameters description:
roc - radius of curvature in mm
diameter - mirror diameter in mm
conic - mirror conic constant / conicity
grating_lines - ronchi grating parameter - lines per mm
ronchi_phase - vertical shift of ronchi grating expressed as a phase shift of sine function 0 - Pi
delta - distance of ronchi grating from paraxial focus / radius of curvature in mm 
"""
import matplotlib.pyplot as plt
from ronchi import Ronchigram

roc = 1200
diameter = 150
conic = -1
grating_lines = 5
ronchi_phase = 0
delta = 5
wavelength = 550

def main():
    my_ronchigram = Ronchigram(ac_mode=False)
    #image_matrix = my_ronchigram.generate_ronchigram_at_focus(roc, diameter, conic, grating_lines, ronchi_phase, delta)
    image_matrix = my_ronchigram.generate_ronchigram_at_roc(roc, diameter, conic, grating_lines, ronchi_phase, delta)
    print("Wavefront error at focus: ", my_ronchigram.wavefront_error_calculation_at_focus(wavelength, roc, diameter, conic))
    print("Wavefront error at radius od curvature: ", my_ronchigram.wavefront_error_calculation_at_roc(wavelength, roc, diameter, conic))
    plt.imshow(image_matrix, cmap='Greys')
    plt.show()
    
if __name__ == "__main__":
    main()

