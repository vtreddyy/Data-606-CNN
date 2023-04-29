from PIL import Image
import os

# Set the desired image size
size = (256, 256)

# Set the path to the folder containing the categories
categories_path = "C:/Users/Tarun Reddy/Desktop/data 606 Final project/catagories"

# Loop through all the category folders
for category_folder in os.listdir(categories_path):
    # Construct the path to the category folder
    category_folder_path = os.path.join(categories_path, category_folder)

    # Check if the category folder exists and is a directory
    if os.path.isdir(category_folder_path):
        # Loop through all the files in the category folder
        for filename in os.listdir(category_folder_path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                # Load the image
                image_path = os.path.join(category_folder_path, filename)
                image = Image.open(image_path)

                # Resize the image
                resized_image = image.resize(size)

                # Save the resized image
                resized_image.save(os.path.join(category_folder_path, "resized_" + filename))
