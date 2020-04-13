from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import os
from moviepy.editor import *
from PIL import Image
from moviepy.video.fx.all import crop

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
GIFS_DIR = os.path.join(SAMPLE_OUTPUTS, 'gifs')
os.makedirs(GIFS_DIR, exist_ok=True)

output_path1 = os.path.join(GIFS_DIR, 'sample1.gif')
output_path2 = os.path.join(GIFS_DIR, 'sample2.gif')

clip = VideoFileClip(source_path)
fps = clip.reader.fps # frame per second
"""
Resize the video and generate gif 
This gif it maybe pixelated and bigger in size 
"""
subclip = clip.subclip(10, 20)
subclip = subclip.resize(width=320)
subclip.write_gif(output_path1, fps=fps, program='ffmpeg')

"""
Crop the video and generate gif  
"""
w, h = clip.size
subclip2 = clip.subclip(10, 20)
square_cropped_clip = crop(subclip2, width=320, height=320, x_center= w/2, y_center= h/2)
square_cropped_clip.write_gif(output_path2, fps=fps, program='ffmpeg')