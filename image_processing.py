import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

try:
    # Load the image
    image_path = image_path = input("Please paste the path to your image file: ")
    logo = np.array(Image.open(image_path).convert("RGB"))  
    arr = logo.astype(float)
    print(arr)
    
    logo_normalized = logo / 255.0  
    dark_logo = 1 - logo_normalized 
    dark_logo = (dark_logo * 255).astype(np.uint8)  

    # original image
    plt.figure(figsize=(12, 6))  
    plt.subplot(1, 2, 1)  
    plt.imshow(logo)
    plt.axis('off')
    plt.title('Original Image')
    plt.grid(False)
    
    # Darkened Image
    plt.subplot(1, 2, 2) 
    plt.imshow(dark_logo)
    plt.axis('off')
    plt.title('Darkened Image')
    plt.grid(False)

    # Display both images
    plt.show()

except FileNotFoundError:
    print("File not found.")
