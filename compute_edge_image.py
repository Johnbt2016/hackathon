import numpy as np
from scipy import signal, misc
from copy import deepcopy

def compute_deriv(image = None):
    '''
    Compute an edge image (the second derivative of a smoothed spline)

    Arguments:
    - image (2D Numpy array) : grayscale image

    Returns:
    - image (2D Numpy array) : the grayscale edge image
    '''

    if image is None:
        image = misc.face(gray=True).astype(np.float32)

    derfilt = np.array([1.0, -2, 1.0], dtype=np.float32)
    ck = signal.cspline2d(image, 8.0)
    deriv = (signal.sepfir2d(ck, derfilt, [1]) +
                signal.sepfir2d(ck, [1], derfilt))

    # Post processing the image
    final = deepcopy(deriv)
    final = 1 - final
    threshold = 0.1
    final[final > threshold] = 1
    final[final < threshold] = 0

    return final

if __name__ == "__main__":
    edge_image = compute_deriv()

    import matplotlib.pyplot as plt

    plt.imshow(edge_image)
    plt.show()