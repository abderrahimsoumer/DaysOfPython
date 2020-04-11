from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import os
from moviepy.editor import *
from PIL import Image

thumbnails_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails')
thumbnails_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-frame')
thumbnails_per_half_second_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-half-second')
output_video = os.path.join(SAMPLE_OUTPUTS, 'thumbs.mp4')

#this_dir = os.listdir(thumbnails_per_half_second_dir)
#filepaths = [os.path.join(thumbnails_per_half_second_dir, fname) for fname in this_dir if fname.endswith('.jpg')]
#clip = ImageSequenceClip(filepaths, fps=4)
#clip.write_videofile(output_video)

directory = {}
for root, dirs, files in os.walk(thumbnails_per_half_second_dir):
    for name in files:
        filepath = os.path.join(root, name)
        try:
            key = float(name.replace('.jpg',''))
        except:
            key = None
        if key != None:
            directory[key] = filepath

new_paths = []
for k in sorted(directory.keys()):
    filepath = directory[k]
    new_paths.append(filepath)

clips = []
for path in new_paths:
    frame = ImageClip(path)
    clips.append(frame.img)


clip = ImageSequenceClip(clips, fps=22)
clip.write_videofile(output_video)

