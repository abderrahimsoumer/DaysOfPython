from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import os
from moviepy.editor import *
from PIL import Image

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
thumbnails_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails')
os.makedirs(thumbnails_dir)

clip = VideoFileClip(source_path)

print(clip.reader.fps) # frame per second
print(clip.reader.nframes)
print(clip.duration) # in second
duration = clip.duration
max_duration = int(duration) + 1
for i in range(0, max_duration):
    print(f"Frame i {i} second")
    frame = clip.get_frame(i) # np.array numpy array #inference
    #print(frame)
    new_image_filepath = os.path.join(thumbnails_dir, f"{i}.jpg")
    new_image = Image.fromarray(frame)
    new_image.save(new_image_filepath)