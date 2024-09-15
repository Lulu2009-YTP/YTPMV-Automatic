import vlc

class VLCPlayer:
    def __init__(self, media_path):
        self.media = vlc.MediaPlayer(media_path)

    def play(self):
        self.media.play()

    def pause(self):
        self.media.pause()

    def stop(self):
        self.media.stop()
