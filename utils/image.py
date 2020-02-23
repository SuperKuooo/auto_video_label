import cv2
import numpy as np


class _ImageOI:
    """Image of interest"""

    def __init__(self, image, contour, cog):
        self.image = image
        self.contour = contour
        self.cog = cog

    def get_cog(self):
        return self.cog

    def get_image(self):
        return self.image

    def get_contour(self):
        return self.contour


class ImageSet:
    lower_red = np.array([150, 150, 180])
    upper_red = np.array([180, 255, 250])
    standard_size = 3000

    def __init__(self):
        self.image_set = list()

    def _insert(self, image, contours, cog):
        self.image_set.append(_ImageOI(image, contours, cog))

    def evaluate_image(self, img):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.lower_red, self.upper_red)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        j = 0
        while j < len(contours):
            area = cv2.contourArea(contours[j])
            if not 0.9 * self.standard_size < area < 1.1 * self.standard_size:
                contours.pop(j)
                continue
            j += 1
        if len(contours) == 1:
            m = cv2.moments(contours[0])
            cx = int(m['m10'] / m['m00'])
            cy = int(m['m01'] / m['m00'])
            self._insert(img, contours[0], (cx, cy))

    def save_set(self, path):
        for i, imageOI in enumerate(self.image_set):
            img = imageOI.get_image()
            cv2.circle(img, imageOI.get_cog(), 5, (0, 255, 0), 5)
            cv2.imwrite(path.folder.parsed_images + '/{}.jpg'.format(i), img)
