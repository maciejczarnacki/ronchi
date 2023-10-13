""" 
Ronchi test simulator for concave mirrors and telescopes

Parameters description:
roc - radius of curvature in mm
diameter - mirror diameter in mm
conic - mirror conic constant / conisity
grating_lines - ronchi grating parameter - lines per mm
ronchi_phase - vertical shift of ronchi grating expressed as a phase shift of sine function 0 - Pi
delta - distant of ronchi grating from paraxial focus / radius of curvature in mm 
"""
import matplotlib.pyplot as plt
from ronchi import ronchi

roc = 1200
diameter = 150
conic = 0
grating_lines = 5
ronchi_phase = 0
delta = -5


def main():
    my_ronchigram = ronchi.Ronchigram(ac_mode=True, resolution=300)
    image_matrix = my_ronchigram.generate_ronchigram(roc, diameter, conic, grating_lines, ronchi_phase, delta)
    plt.imshow(image_matrix, cmap='Greys')
    plt.show()

    
if __name__ == "__main__":
    main()

