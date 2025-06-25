import cv2
import numpy as np

def warp_to_smile_shape(image, curvature=0.0005):
    h, w = image.shape[:2]
    map_y, map_x = np.indices((h, w), dtype=np.float32)

    # can't go beyond 2.1
    offset_param = 0.2
    offset_y = (np.square(map_x - w / 2) * curvature * 1).astype(np.float32)
    map_y -= offset_y * offset_param

    # disable x offset 
    # offset_x = (np.square(map_y - h / 2) * curvature * 2).astype(np.float32)
    # map_x += offset_x

    warped = cv2.remap(image, map_x, map_y, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    return warped

image = cv2.imread("C:/Users/uih32851/Desktop/Image1.png")
# image = cv2.imread("C:/Users/uih32851/Desktop/Image2.png")

# to debug 
if image is None:
    print("Image not loaded. Check the file path and name.")
    exit()

# to write out 
warped = warp_to_smile_shape(image)
cv2.imwrite("C:/Users/uih32851/Desktop/warped_smile_image_1.png", warped)
# cv2.imwrite("C:/Users/uih32851/Desktop/warped_smile_image_2.png", warped)
