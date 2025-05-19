#!/usr/bin/python3

# Andrew Nyland, 5/19/25 inspired by chatGPT

from sceneobjects import Point, Line, Scene
import time

# Define points
A  = Point([   0,0.5,    0])
B  = Point([ 0.5,0.9, -0.7])
C1 = Point([ 0.6,  1,   -1])
C2 = Point([ 0.6,  1,    1])
D1 = Point([   1,  0,-0.25])
D2 = Point([   1,  0, 0.25])
E  = Point([-0.4,0.1,    0])
F  = Point([   0,1.6,    0])

#.... Kayak parts?
KN = Point([1.5, 0, 0])  # kayak knose
KT = Point([-1.5, 0, 0])  # kayak tail
BH1 = Point([.3, 0, 0])  # is it called a bulkhead?
BH2 = Point([.3, .2, 0])

# Define lines
AB   = Line(A, B)
BC1  = Line(B, C1)
CC   = Line(C1,C2)
ED1  = Line(E, D1)
ED2  = Line(E, D2)
AC1  = Line(A, C1)
AC2  = Line(A, C2)
AD1  = Line(A, D1)
AD2  = Line(A, D2)

EF   = Line(E, F)


# kayak partss
BHF = Line(BH1, BH2)


# Create scene and add elements
scene = Scene()

scene.add(A)
scene.add(B)
scene.add(C1)
scene.add(C2)
scene.add(D1)
scene.add(D2)
scene.add(E)

scene.add(AB)
scene.add(BC1)
scene.add(CC)
scene.add(ED1)
scene.add(ED2)
#scene.add(AC1)
scene.add(AC2)
scene.add(AD1)
scene.add(AD2)

scene.add(EF)

# kayak parts
scene.add(KN)
scene.add(KT)
scene.add(BHF)


# Show 3D visualization
scene.show()

