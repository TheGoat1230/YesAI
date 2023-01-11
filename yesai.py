import imghdr
from PIL import Image
import os
import glob
import msvcrt

def strip_metadata(img_path):
    # Opening the image
    img = Image.open(img_path)
    
    #Resizing image down
    width, height = img.size
    img = img.resize((int(width * 0.5), int(height * 0.5)))
    
    #Resizing back up
    width, height = img.size
    img = img.resize((int(width * 2.0), int(height * 2.0)))

    # Create an empty dictionary for the new image's metadata
    data = {}

    # Looking for the file type
    img_type = imghdr.what(img_path)

    # Rename the file, YES AI!
    new_name = os.path.splitext(img_path)[0] + '_yesai.' + img_type
    # Save the image with the new metadata
    if img_type == 'jpeg':
        img.save(new_name, "JPEG", exif=data)
    elif img_type == 'png':
        img.save(new_name, "PNG", pnginfo=data)
    else:
        raise ValueError(f"Unsupported image type: {img_type}")
    
    print(f"Metadata removed from {img_path} and saved as {new_name}")

# Look in the same directory as our .py file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Let's look for our .jpeg/.jpg/.png files
for file in glob.glob(current_dir + "/*.jpeg"):
    strip_metadata(file)
for file in glob.glob(current_dir + "/*.jpg"):
    strip_metadata(file)
for file in glob.glob(current_dir + "/*.png"):
    strip_metadata(file)

print("Thanks for using YesAI! Press 'Q' to quit.")
while True:
    if msvcrt.kbhit():
        if ord(msvcrt.getch()) == 113:
            break
