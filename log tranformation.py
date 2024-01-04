# import cv2
# import numpy as np
# img_input=cv2.imread("girl.png",flags=0)
# img=50*np.log(1+img_input)
# img_output=img.astype(np.uint8)
# cv2.imshow(winname='input', mat=img_input)
# cv2.imshow(winname='log', mat=img_output)
# key=cv2.waitKey(0)
# if key==27:
#     cv2.destroyAllWindows()
# elif key==ord('s'):
#     cv2.imwrite(img_output, filename='negative_binary_images' )
#     cv2.destroyAllWindows()
# import cv2
# import numpy as np
#
# # Read the image in grayscale mode
# img_input = cv2.imread("girl.png", flags=0)
#
# # Apply an exponential transformation
# img = np.exp(0.04 * img_input)  # You can adjust the constant (0.04) as needed
#
# # Ensure the output is in the valid range (0-255)
# img_output = np.clip(img, 0, 255).astype(np.uint8)
#
# # Display the input and transformed images
# cv2.imshow(winname='input', mat=img_input)
# cv2.imshow(winname='exponential', mat=img_output)
#
# # Wait for a key press
# key = cv2.waitKey(0)
#
# # Close windows based on key press
# if key == 27:  # Esc key
#     cv2.destroyAllWindows()
from PIL import Image

# Open the image file
image_path = "your_image.jpg"  # Replace with your image path
img = Image.open(image_path)

# Get the dimensions of the image
width, height = img.size

# Create a new blank image with the same dimensions
flipped_img = Image.new("RGB", (width, height))

# Iterate through each pixel in the original image and copy it to the flipped image
for x in range(width):
    for y in range(height):
        pixel = img.getpixel((x, y))
        flipped_img.putpixel((width - x - 1, y), pixel)

# Save the flipped image
flipped_img.save("flipped_image.jpg")  # Change the output filename as needed

# Close the original image
img.close()
