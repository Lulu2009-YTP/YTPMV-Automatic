from moviepy.editor import AudioFileClip, concatenate_audioclips
from pydub import AudioSegment

class AudioProcessor:
    def __init__(self):
        self.audio_clips = []

    def add_audio(self, filepath, start_time, end_time):
        audio = AudioFileClip(filepath).subclip(start_time, end_time)
        self.audio_clips.append(audio)

    def apply_effects(self, audio_clip):
        # Applying pitch shift, speed change or reverb
        shifted = audio_clip.fx(audio.fx.all.audio_fadein, 3)
        return shifted

    def generate_audio_track(self, output_path="output_audio.mp3"):
        final_audio = concatenate_audioclips(self.audio_clips)
        final_audio.write_audiofile(output_path)

    def add_stutter_effect(self, audio_clip):
        # Example of a stutter effect
        stuttered = audio_clip.fx(audio.fx.all.speedx, 2)
        return stuttered
