
"""
Videophy is a small tool to easily convert single images to a video format
"""

"""
If you are using opencv-python version 4.6.0.66,
try to downgrade to 4.5.5.64 version,
you can do that by go to
File->Setting->Python Interpreter->
Double-click on opencv-python version->
check the specify version box, then choose older version(4.5.5.64).
"""


# We start by importing the necessary modules
import os
from videophy import Video, Stream
from PIL import Image, ImageDraw, ImageColor
import random as r

# For the sake of this tutorial we have some parameters to play with
fps = 60
videoLength = 3200
videoName = "exampleVideo"
outputFolder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
colorChangeSpeed = 5
size = (300, 300)

# Create the video object that is going to export to the desktop,
# the rest of the keyword arguments are optional
video = Video(outputFolder, name=videoName, fps=fps)
stream = Stream()

# Lastly a list that's going to represent the color we will be using during this example
color = [r.randint(0, 256) for i in range(3)]


# Multiplying the frames per second times the amount of seconds give us how many frames we should be rendering
lastPercentage = 0
for i in range(videoLength * fps):
    # Render a simple image

    # Print progress for longer renders
    percentage = int(i/(videoLength * fps)*100)
    if percentage > lastPercentage:
        lastPercentage = percentage
        print(f"{percentage}%")

    # First we randomly change our color a bit
    color = [channel + r.choice((-colorChangeSpeed, colorChangeSpeed)) for channel in color]

    # Make an image with our new color
    image = Image.new("RGB", size, tuple(color))

    # Add the image (frame) to the video
    video.addFrame(image)
    #stream.newFrame(image)

# Release the video
video.release()

# Now you'll find a video on your desktop of changing colors, i'm sure there are way more interesting applications
