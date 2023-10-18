# Ronchi

The Ronchi test is an optical test to qualitatively measure the shape of concave curved mirrors.
There are two types of Ronchi test: a test performed from the center of curvature and a test performed near the focal point. 
The test performed near the focus (e.g. at paraxial focus) is divided into two methods: single pass and double pass (autocollimation test). 
In order to analyze the shape of a concave mirror, we need a Ronchi screen in the form of parallel lines of the same width, a
lternately transparent and cutting off the light. For example, let's analyze the test performed from the center of curvature of the mirror, 
which is very similar to the Foucault test. At the point of the center of curvature on the optical axis of the mirror, 
we place a point light source illuminating the mirror. Then we observe the mirror from the same point (or its surroundings) through the Ronchi screen. 
From the shape of the observed lines we can determine whether we are dealing with a spherical, parabolic, hyperbolic or elliptical mirror. We can also identify mirror defects, such as turned edges and zones of different shapes within the mirror. 
Astigmatism and coma are also visible. However, the latter aberrations are less visible than spherical aberration. 
The test is qualitative, not quantitative. This means that we cannot use it to easily and clearly calculate/estimate the value of the wavefront error as peak to valey error, rms or Strehl coefficient. The author of this repository has created a program for comparative analysis of actual measurement and simulation, 
and thus an attempt to estimate the values described above.

The repository in the form of a python module allows you to generate Ronchi test simulation images in all mentioned systems. Below are sample images (ronchigrams) generated with this program. The description of the class parameters and methods are included in the program code as comments.

In order to expand your knowledge about the Ronchi test, I invite you to read the websites and materials listed in the references at the bottom of the page.

Ronchigram of the spherical mirror seen from the radius of curvature.

![Ronchigram of the spherical mirror seen from the radius of curvature](/images/Sphere_at_roc.png)

Ronchigram of the spherical mirror seen from the focus.

![Ronchigram of the spherical mirror seen from the focus](/images/Sphere_at_focus.png)

Ronchigram of the spherical mirror seen from the focus in autocollimation mode.

![Ronchigram of the spherical mirror seen from the focus in autocollimation mode](/images/Sphere_at_focus_autocollimation_mode.png)

Ronchi grating used as a knife edge in Foucault test at the radius of curvature - Parabolic mirror

![Ronchi grating used as a knife edge in Foucault test at the radius of curvature - Parabolic mirror](/images/Parabola_at_roc_ronchi_as_knife_edge.png)


## References
- [Wikipedia about Ronchi test](https://en.wikipedia.org/wiki/Ronchi_test)
- [A brilliant source of knowledge about telescope optics, chapter on the Ronchi test](https://www.telescope-optics.net/ronchi_test.htm)
- [Discussion about the Ronchi test in autocollimation mode symulation on the Cloudy Nights forum](https://www.cloudynights.com/topic/812098-dpac-test-simulation-comparison/?hl=aos)
- My Ronchi Test Simulator (AOS) written in C# - https://maciejczarnacki.github.io/AOS/
