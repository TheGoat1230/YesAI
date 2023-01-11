# YesAI - The Friendly Metadata/Invisible Watermark Remover

YesAI is written in Python using the PIL (Pillow) library. It takes images (.png/.jpg/.jpeg) and removes the metadata, clearing out any AI related information from the header, it then resizes the image and gives you an output of the same resolution to remove any invisible watermarks. This was written with the sole intention of testing and is not meant to harm artists. If an artist does not want their work used, respect it!

# How do I use it?

It's pretty straight forward.

1) Install Python 3
2) Install the PIL (Pillow) library (https://pypi.org/project/Pillow/)
3) Place your images in the same directory as the .py file
4) Double click the .py file and your images will be saved as "filename_yesai.extension"

# Does it work?

See for yourself!

![YesAI](https://user-images.githubusercontent.com/122483158/211902821-7b792e18-35c4-44df-aebe-de05209de0c4.png)

This will remove all traces of prompts, samplers, seeds and more. It also reduces the image resolution, and bumps it back up to bypass the invisible watermark.

# Side-note

Again, this project is not meant to harm anyone. This can be used for the sole purpose of cleaning up metadata related to AI generated images for whatever reason, as well as getting rid of invisible watermarks. You can build on this, play with it, experiment with it. Use it at your own risk and I take NO responsibility for ill use of the code.

# Credits: (For Pillow and Python Imaging Library (PIL))

The Python Imaging Library (PIL) is

    Copyright © 1997-2011 by Secret Labs AB
    Copyright © 1995-2011 by Fredrik Lundh

Pillow is the friendly PIL fork. It is

    Copyright © 2010-2023 by Alex Clark and contributors

For more information, see https://github.com/python-pillow/Pillow/blob/main/LICENSE
