import cv2
import numpy as np
from scipy.linalg import svd

read_image = cv2.imread('sample_image.png')
svd_of_image = np.linalg.svd(read_image)
U, s, Vt = np.linalg.svd(a = read_image, full_matrices = True)
print(U.shape)
print(s.shape)
print(Vt.shape)
print("\n SVD of image: \n ", svd_of_image)

