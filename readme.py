
"""
Videophy is a small to to easily convert single images to a video format
"""

# we start by importing the necessary modules
import os

from videophy import Video
from PIL import Image, ImageDraw, ImageColor
import random as r

# For the sake of this tutorial we have some parameters to play with
fps = 30
videoLength = 30
videoName = "exampleVideo"
outputFolder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
colorChangeSpeed = 10
size = (300, 300)

# Create the video object that is going to export to the desktop,
# the rest of the keyword arguments are optional
video = Video(outputFolder, name=videoName, fps=fps)

# Lastly a list that's going to represent the color we will be using during this example
color = [r.randint(0, 256) for i in range(3)]


# Multiplying the frames per second times the amount of seconds give us how many frames we should be rendering
for i in range(videoLength * fps):
    # Render a simple image

    # first we randomly change our color a bit
    color = [channel + r.choice((-colorChangeSpeed, colorChangeSpeed)) for channel in color]

    # make an image with our new color
    image = Image.new("RGB", size, tuple(color))

    # add the image (frame) to the video
    video.addFrame(image)

# release the video
video.release()

# now you'll find a video on your screen of changing colors, i'm sure  there are way more interesting applications








