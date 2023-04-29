from PIL import Image
import os

# Set the desired image size
size = (256, 256)

# Set the path to the folder containing the categories
categories_path = "C:/Users/Tarun Reddy/Desktop/data 606 Final project/catagories"

# Set the path to the output folder
output_folder_path = "C:/Users/Tarun Reddy/Desktop/data 606 Final project/processed_images"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.mkdir(output_folder_path)

# Loop through all the category folders
for category_folder_index, category_folder in enumerate(os.listdir(categories_path)):
    # Construct the path to the category folder
    category_folder_path = os.path.join(categories_path, category_folder)

    # Check if the category folder exists and is a directory
    if os.path.isdir(category_folder_path):
        # Create the output subfolder if it doesn't exist
        output_subfolder_path = os.path.join(output_folder_path, "Threat_Level_" + str(category_folder_index + 1))
        if not os.path.exists(output_subfolder_path):
            os.mkdir(output_subfolder_path)

        # Loop through all the files in the category folder
        for i, filename in enumerate(os.listdir(category_folder_path)):
            if filename.endswith(".jpg") or filename.endswith(".png"):
            # Load the image
                image_path = os.path.join(category_folder_path, filename)
                image = Image.open(image_path)

                # Convert the image to RGB mode
                image = image.convert("RGB")

                # Resize the image
                resized_image = image.resize(size)

                # Set the output filename
                output_filename = "{}.jpg".format(i)

                # Save the resized image
                resized_image.save(os.path.join(output_subfolder_path, output_filename))