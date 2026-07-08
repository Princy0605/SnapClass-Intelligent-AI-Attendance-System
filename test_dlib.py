import dlib
import numpy as np

detector = dlib.get_frontal_face_detector()

img = np.zeros((100, 100, 3), dtype=np.uint8)

print("dtype:", img.dtype)
print("shape:", img.shape)

faces = detector(img, 1)

print("Success!")
print("Faces:", len(faces))