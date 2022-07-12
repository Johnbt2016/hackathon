# Edge detection as a web service

This Daisi is the deployment of an algorithm for edges
detection.

Edge detection includes a variety of mathematical methods that aim at identifying edges, curves in a digital image at which the image brightness changes sharply or, more formally, has discontinuities. The same problem of finding discontinuities in one-dimensional signals is known as step detection and the problem of finding signal discontinuities over time is known as change detection. Edge detection is a fundamental tool in image processing, machine vision and computer vision, particularly in the areas of feature detection and feature extraction.

See [the Wikipedia page](https://en.wikipedia.org/wiki/Edge_detection) for more info.

How to call it from Python:

```python
#Step 1 : Load the Daisi
import pydaisi as pyd
hackathon_edge_demo = pyd.Daisi("laiglejm/Hackathon Edge Demo")

#Step 2 : call the compute_deriv endpoint, passing in input a
#2D Numpy array representing a grayscale image
result = hackathon_edge_demo.compute_deriv().value
#returns a 2D Numpy array

#Step 3: visualize the result
import matplotlib.pyplot as plt

plt.imshow(result)
plt.show()
```
