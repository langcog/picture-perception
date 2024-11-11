import cv2
import numpy as np
import os

def remove_text_and_shapes_from_img(image_path):
    image = cv2.imread(image_path)

    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # mask with upper and lower bound for gray intensity
    lower_grayscale_bound = 50  
    upper_grayscale_bound = 170
    mask = cv2.inRange(grayscale_image, lower_grayscale_bound, upper_grayscale_bound)

    # add dilation to fill small gaps within shapes / words
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)

    # process detected contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if 30 < area < 3000: # can change if shapes if too big/small for shapes
            cv2.drawContours(image, [contour], -1, (255, 255, 255), thickness=cv2.FILLED)

    return image


def process_images(image_dir, output_dir):
    for image_file in sorted(os.listdir(image_dir)):
        image_path = os.path.join(image_dir, image_file)
        image = remove_text_and_shapes_from_img(image_path)
        output_path = os.path.join(output_dir, image_file)
        cv2.imwrite(output_path, image)

        print(output_path)

if __name__ == "__main__":
    image_dir = "../drawing_images"
    output_dir = "../processed_drawing_images"
    process_images(image_dir, output_dir)