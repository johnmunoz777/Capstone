import cv2
import numpy as np
import matplotlib.pyplot as plt
## Read the image in, get the shape of the image, transform to RGB, plot the image
img = cv2.imread('image_one.jpg', 1)
img.shape
plt.imshow(img)
img_transform=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_transform)
# Image dimensions
height, width, _ = img.shape
# Bounding box in pixels
# in my image draw the object in this position
x_start = 130
x_end = 205
y_start = 63
y_end = 113
cv2.rectangle(img_transform, (x_start , y_start ), (x_end, y_end), (0, 255, 0), 2)
plt.imshow(img_transform)
plt.axis('off')
plt.show()
### calculate the normalized coordinates for YOLO:
img = cv2.imread('image_one.jpg', 1)
img.shape
height, width, _ = img.shape
x_start = 130
x_end = 205
y_start = 63
y_end = 113
# Calculate center (in pixels)
center_x = (x_start + x_end) / 2
center_y = (y_start + y_end) / 2
# Calculate width and height (in pixels)
bbox_width = x_end - x_start
bbox_height = y_end - y_start
# Normalize by image dimensions
normalized_center_x = center_x / width
normalized_center_y = center_y / height
normalized_bbox_width = bbox_width / width
normalized_bbox_height = bbox_height / height
# Create the YOLO format label (class ID 0, for example)
class_id = 0
label = f"{class_id} {normalized_center_x} {normalized_center_y} {normalized_bbox_width} {normalized_bbox_height}"
print(label)
img = cv2.imread('image_one.jpg', 1)
#Your YOLO-style annotation (example values)
class_id = 0  # Object class (just for reference)
normalized_x_center = normalized_center_x
normalized_y_center = normalized_center_y
normalized_width =    normalized_bbox_width
normalized_height = normalized_bbox_height 

# Image dimensions
image_height = img.shape[0]  # Height of the image (number of rows)
image_width = img.shape[1] # Width of the image (number of columns)

# Reverse the normalization process
x_center = normalized_x_center * image_width
y_center = normalized_y_center * image_height
box_width = normalized_width * image_width
box_height = normalized_height * image_height
# Calculate the top-left corner of the bounding box
top_left_x = int(x_center - (box_width / 2))
top_left_y = int(y_center - (box_height / 2))
# (top_left_x, top_left_y) is the top-left corner, and (box_width, box_height) is the size
bottom_right_x = top_left_x + int(box_width)
bottom_right_y = top_left_y + int(box_height)
bottom_right_x

print("The Original Points to plot were:")
print("x_start", x_start)
print("x_end", x_end)
print("y_start", y_start)
print("y_end", y_end)
print("Now comparing the transformed points:")
print("transformed_x_start", top_left_x)
print("transformed_x_end", bottom_right_x)
print("transformed_y_start", top_left_y)
print("transformed_y_end", bottom_right_y)

# Draw the rectangle on the image (BGR format, color is green (0, 255, 0))
cv2.rectangle(img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 2)
# Display the image with the bounding box
img_transform=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_transform)


