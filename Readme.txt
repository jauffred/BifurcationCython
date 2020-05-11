Comparison of performance between Python and Cython using bifurcation maps taken from Metropolis et al. 1973.
Build:
cython –a BifurcationCy.pyx
python setup.py build_ext –if

Run:
python BifurcationTest.py (#points in x axis) (#iterations) (#points y axis)

Refecence:
Metropolis, Stein and Stein (1973) Journal of Combinatorial Theory A15, 25.
