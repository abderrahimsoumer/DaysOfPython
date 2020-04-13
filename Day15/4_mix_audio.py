from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import os
from moviepy.editor import *
from PIL import Image

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
source_audio_path = os.path.join(SAMPLE_INPUTS, 'audio.mp3')
mix_audios_dir = os.path.join(SAMPLE_OUTPUTS, 'mix-audios')
os.makedirs(mix_audios_dir, exist_ok=True)
og_audio_path = os.path.join(mix_audios_dir, 'og.mp3')
final_audio_path = os.path.join(mix_audios_dir, 'final-audio.mp3')
final_video_path = os.path.join(mix_audios_dir, 'final-video.mp4')

video_clip = VideoFileClip(source_path)
original_audio = video_clip.audio
#original_audio.write_audiofile(og_audio_path)

background_audio_clip = AudioFileClip(source_audio_path)
bg_music = background_audio_clip.subclip(0, video_clip.duration)
bg_music = bg_music.volumex(0.50)

final_audio = CompositeAudioClip([original_audio, bg_music])
final_audio.write_audiofile(final_audio_path, fps=original_audio.fps)

final_video = video_clip.set_audio(final_audio)
final_video.write_videofile(final_video_path, codec='libx264', audio_codec='aac')