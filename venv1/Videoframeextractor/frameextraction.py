class VideoFrameExtractor:
    def __init__(self, input_folder, output_folder3, fps=1):
        """
        Initializes the VideoFrameExtractor class.

        Parameters:
            input_folder (str): Path to the folder containing videos.
            output_folder (str): Path to save extracted frames.
            fps (int): Frames per second to extract.
        """
        self.input_folder = input_folder
        self.output_folder3 = output_folder3
        self.fps = fps
        
        # Create the output folder if it doesn't exist
        if not os.path.exists(self.output_folder3):
            os.makedirs(self.output_folder3)

    def extract_frames(self):
        """
        Extracts frames from all videos in the input folder.
        """
        for video_file in os.listdir(self.input_folder):
            video_path = os.path.join(self.input_folder, video_file)
            
            # Check if the file is a video
            if not video_file.lower().endswith(('.mp4', '.avi', '.mkv', '.mov')):
                print(f"Skipping non-video file: {video_file}")
                continue
            
            self._process_video(video_path, video_file)
        
        print("All videos processed.")

    def _process_video(self, video_path, video_file):
        """
        Processes a single video to extract frames.

        Parameters:
            video_path (str): Path to the video file.
            video_file (str): Name of the video file.
        """
        cap = cv2.VideoCapture(video_path)
        video_name = os.path.splitext(video_file)[0]
        frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
        interval = frame_rate // self.fps

        print(f"Processing: {video_file}")
        frame_count = 0
        success, frame = cap.read()
        
        while success:
            if frame_count % interval == 0:
                frame_filename = f"{video_name}_frame{frame_count}.jpg"
                frame_output_path = os.path.join(self.output_folder3, frame_filename)
                cv2.imwrite(frame_output_path, frame)
            
            frame_count += 1
            success, frame = cap.read()
        
        cap.release()
        print(f"Completed: {video_file}")

# Example Usage
if __name__ == "__main__":
    input_folder = 'D:\Videos folder'
    output_folder3 = 'D:\Videos folder\output_folder3'
    fps = 1 # Change to 2 for 2 fps, etc.
    
    extractor = VideoFrameExtractor(input_folder, output_folder3, fps)
    extractor.extract_frames()