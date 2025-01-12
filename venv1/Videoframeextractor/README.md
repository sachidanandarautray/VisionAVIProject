**Video Frame Extractor**
**This Python script is a utility for extracting frames from videos at a specified frame rate (frames per second). It can process multiple video files within a folder and save the extracted frames to a specified output directory.**

## Features
. Extracts frames from videos at a configurable frame rate (e.g., 1 frame per second).
## Supports multiple video formats, including .mp4, .avi, .mkv, and .mov.
. Automatically skips non-video files in the input folder.
. Saves extracted frames as .jpg images with meaningful filenames.
. Automatically creates the output directory if it does not exist.

## How It Works
#### Initialization: The VideoFrameExtractor class is initialized with the input folder (containing videos)
#### the output folder (where extracted frames will be saved), and the desired frames per second (fps) for extraction.
#### Frame Extraction: The script processes each video in the input folder , calculates the interval based on the video’s frame rate and the desired fps, and extracts the corresponding frames.
#### Output: Extracted frames are saved in the output folder with filenames that indicate the source video and frame number.

## Requirements
Python 3.x
OpenCV (cv2)
A valid video file in the supported formats.

### Supported Video Formats
##### .mp4
##### .avi
##### .mkv
##### .mov
Notes
Ensure that the input folder contains valid video files.
Modify the fps parameter as needed to extract more or fewer frames per second.



      +----------------------------+
      | Start                      |
      +----------------------------+
                |
                v
      +----------------------------+
      | Initialize VideoFrameExtractor |
      | input_folder, output_folder3, fps  |
      +----------------------------+
                |
                v
      +----------------------------+
      | Check if output folder exists |
      +----------------------------+
                |
                v
      +----------------------------+
      | Loop through videos in the folder |
      +----------------------------+
                |
                v
      +----------------------------+
      | Check if file is a video    |
      | (extensions: mp4, avi, mkv, mov) |
      +----------------------------+
                |
                v
      +----------------------------+
      | Call _process_video(video_path, video_file) |
      +----------------------------+
                |
                v
      +----------------------------+
      | Open video using cv2.VideoCapture |
      +----------------------------+
                |
                v
      +----------------------------+
      | Get the FPS of the video   |
      | Calculate frame interval   |
      +----------------------------+
                |
                v
      +----------------------------+
      | Loop through video frames |
      +----------------------------+
                |
                v
      +----------------------------+
      | If frame count is divisible by interval |
      +----------------------------+
                |
                v
      +----------------------------+
      | Save the extracted frame as an image |
      +----------------------------+
                |
                v
      +----------------------------+
      | Continue to next frame     |
      +----------------------------+
                |
                v
      +----------------------------+
      | Release video resources    |
      +----------------------------+
                |
                v
      +----------------------------+
      | Completed processing of video |
      +----------------------------+
                |
                v
      +----------------------------+
      | End                        |
      +----------------------------+

