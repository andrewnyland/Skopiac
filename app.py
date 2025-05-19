#!/usr/bin/python3

# Andrew Nyland, 5/19/25 inspired by chatGPT

from sceneobjects import Point, Line, Scene
import time

# Define points
a = Point([0, 0, 2])

# Define lines
ab = Line(a, b)
bc = Line(b, c)
ca = Line(c, a)
cd = Line(c, d)

# Create scene and add elements
scene = Scene()
scene.add(a)
scene.add(b)
scene.add(c)
scene.add(ab)
scene.add(bc)
scene.add(ca)

scene.add(cd)

# Show 3D visualization
scene.show()

