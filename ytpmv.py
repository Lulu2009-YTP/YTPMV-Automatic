from video_editor import VideoEditor
from audio_processor import AudioProcessor
from wx import App
from gui import MainFrame

def main():
    # Initialize the GUI app
    app = App(False)
    frame = MainFrame(None, title="YTPMV Generator 2012 Style")
    frame.Show()
    
    # Create instances of VideoEditor and AudioProcessor
    video_editor = VideoEditor()
    audio_processor = AudioProcessor()

    # Start the wxPython event loop
    app.MainLoop()

if __name__ == "__main__":
    main()
