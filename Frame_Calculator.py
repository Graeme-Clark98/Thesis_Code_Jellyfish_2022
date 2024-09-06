# This program is designed to separate drone footage into frames
from moviepy.editor import VideoFileClip
import numpy as np
import os
from datetime import timedelta

# os.chdir("D:)

# Number of saved frames per second of run time
SFPS = 60

# Function to time stamp frames (00:00:00.00)


def format_timedelta(td):
    result = str(td)
    try:
        result, ms = result.split(".")
    except ValueError:
        return (result + ".00").replace(":", "-")
    ms = int(ms)
    ms = round(ms / 1e4)
    return f"{result}.{ms:02}".replace(":", "-")

# creating main function


def main(video_file):
    # loading file
    video_clip = VideoFileClip(video_file)
    # making a folder by the name of video file
    filename, _ = os.path.splitext(video_file)
    filename += "-moviepy"
    if not os.path.isdir(filename):
        os.mkdir(filename)
    # setting SFPS as max FPS
    sfps = min(video_clip.fps, SFPS)
    # If SFPS is set to 0, step is 1/fps, else 1/SFPS
    step = 1 / video_clip.fps if sfps == 0 else 1 / sfps
    # iterate over each frame
    for current_duration in np.arange(0, video_clip.duration, step):
        # format file name and save
        frame_duration_formatted = format_timedelta(
            timedelta(seconds=current_duration))
        frame_filename = os.path.join(
            filename, f"frame{frame_duration_formatted}.jpg")
        # now we save file with the current duration
        video_clip.save_frame(frame_filename, current_duration)


# functions done time for the main code
if __name__ == "__main__":
    import sys
    video_file = sys.argv[1]
    main(video_file)
