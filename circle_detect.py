import cv2
import numpy as np
import argparse


# Construct arguments, --image is used as path to image arg.
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load image
image = cv2.imread(args["image"])
# Clone image for output
output = image.copy()
# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Detecting circles
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.5, 70)

# Ensure some circles were detected
if circles is not None:
    print("Circles found.")
    # Convert the (x, y) coords and radius of the circles to ints
    circles = np.round(circles[0, :]).astype("int")
    x1 = int
    y1 = int
    r1 = int
    x2 = int
    y2 = int
    r2 = int
    penny_d = 19.05

    # Math to calculate ratios
    r1 = circles[0, 2]
    r2 = circles[1, 2]

    if r1 < r2:
        ratio = penny_d / r1
        yolk_d = ratio * r2
        print("Diameter of bigger circle is " + str(yolk_d) + " mm.")

    else:
        ratio = penny_d / r2
        yolk_d = ratio * r1
        print("Diameter of bigger circle is " + str(yolk_d) + " mm.")

    for (x, y, r) in circles:
        # Draw the circle in the output image, then draw a rectangle
        # corresponding to the center of the circle
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        # cv2.putText(output, yolk_d, (x, y), )

    cv2.imshow("image", np.hstack([image, output]))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print()
print("No circles detected.")
