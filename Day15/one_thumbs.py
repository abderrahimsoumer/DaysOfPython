from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import os
from moviepy.editor import *
from PIL import Image

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
thumbnails_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails')
thumbnails_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-frame')
os.makedirs(thumbnails_dir, exist_ok=True)
os.makedirs(thumbnails_per_frame_dir, exist_ok=True)

clip = VideoFileClip(source_path)

print(clip.reader.fps) # frame per second
print(clip.reader.nframes)
print(clip.duration) # in second
# duration = clip.duration
# max_duration = int(duration) + 1

for i, frame in enumerate(clip.iter_frames()):
    #frame = clip.get_frame(i) # np.array numpy array #inference
    #print(frame)
    new_image_filepath = os.path.join(thumbnails_per_frame_dir, f"{i}.jpg")
    new_image = Image.fromarray(frame)
    new_image.save(new_image_filepath)