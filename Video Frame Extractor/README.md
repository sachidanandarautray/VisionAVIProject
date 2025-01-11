#This Python script is a utility for extracting frames from videos at a specified frame rate (frames per second). It can process multiple video files within a folder and save the extracted frames to a specified output directory.

Features
Extracts frames from videos at a configurable frame rate (e.g., 1 frame per second).
Supports multiple video formats, including .mp4, .avi, .mkv, and .mov.
Automatically skips non-video files in the input folder.
Saves extracted frames as .jpg images with meaningful filenames.
Automatically creates the output directory if it does not exist.
How It Works
Initialization:
The VideoFrameExtractor class is initialized with:

Input folder: The folder containing the videos.
Output folder: Where extracted frames will be saved.
Frames per second (fps): The desired frame rate for extraction.
Frame Extraction:
The script processes each video in the input folder, calculates the interval based on the video’s frame rate and the desired fps, and extracts the corresponding frames.

Output:
Extracted frames are saved in the output folder with filenames that indicate the source video and frame number.

Requirements
Python 3.x
OpenCV (cv2)
A valid video file in one of the supported formats.
