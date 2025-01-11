
This Python script is a utility for extracting frames from videos at a specified frame rate (frames per second). It can process multiple video files within a folder and save the extracted frames to a specified output directory.

Features
Extracts frames from videos at a configurable frame rate (e.g., 1 frame per second).
Supports multiple video formats, including .mp4, .avi, .mkv, and .mov.
Automatically skips non-video files in the input folder.
Saves extracted frames as .jpg images with meaningful filenames.
Automatically creates the output directory if it does not exist.
How It Works
Initialization: The VideoFrameExtractor class is initialized with the input folder (containing videos), the output folder (where extracted frames will be saved), and the desired frames per second (fps) for extraction.
Frame Extraction: The script processes each video in the input folder, calculates the interval based on the video’s frame rate and the desired fps, and extracts the corresponding frames.
Output: Extracted frames are saved in the output folder with filenames that indicate the source video and frame number.
Requirements
Python 3.x
OpenCV (cv2)
A valid video file in the supported formats.
Usage
Clone this repository:
bash
Copy code
git clone https://github.com/yourusername/video-frame-extractor.git
Install the required libraries:
bash
Copy code
pip install opencv-python
Update the script with your input and output folder paths:
python
Copy code
input_folder = 'path/to/your/input/folder'
output_folder3 = 'path/to/your/output/folder'
fps = 1  # Specify desired frames per second for extraction.
Run the script:
bash
Copy code
python video_frame_extractor.py
Example
If the input folder contains a video named example.mp4 and the frame rate is set to 1 fps, the script will create an output folder (if not already present) and save extracted frames with filenames like:

python
Copy code
example_frame0.jpg
example_frame30.jpg
example_frame60.jpg
...
Supported Video Formats
.mp4
.avi
.mkv
.mov
Notes
Ensure that the input folder contains valid video files.
Modify the fps parameter as needed to extract more or fewer frames per second.
