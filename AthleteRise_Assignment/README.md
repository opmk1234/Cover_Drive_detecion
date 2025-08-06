Cover Drive Pose Analysis
This project analyzes a cricket cover drive shot from a YouTube video using computer vision and pose estimation.
It detects a player's body posture, calculates biomechanical angles, and generates annotated frames and a feedback report.

📂 Project Structure
graphql
Copy code
AthleteRise_Assignment/
│
├── analyze_youtube_shot.py      # Main script to run the analysis
├── form.py                      # Contains biomechanical metrics calculations
├── posetrack.py                 # Pose detection helper class (MediaPipe)
├── video_dowd.py                # Handles YouTube video download
│
├── Data/
│   ├── Input/                   # (Optional) extracted raw frames
│   ├── Video/                   # downloaded video file
│   ├── Output/
│   │    ├── annotated_frames/   # processed frames with pose skeleton overlay
│   │    └── cover_drive_report.json  # final feedback report
│
└── README.md                    # Project documentation
⚙️ Requirements
Python 3.8+

Install required packages:

bash
Copy code
pip install opencv-python mediapipe numpy yt-dlp
🚀 How to Run the Project
Clone or extract the project folder.

Ensure you have an active internet connection (for YouTube video download).

Open a terminal in the project folder.

Run the main script:


python analyze_youtube_shot.py


Processing Pipeline
Download Video:
The script fetches the YouTube video automatically and saves it in Data/Video/.

Pose Detection:
Uses MediaPipe Pose to detect body keypoints frame by frame.

Metrics Calculation:

Elbow extension angle

Spine lean

Foot placement angle

Head-to-knee alignment

Save Results:

Annotated frames → Data/Output/annotated_frames/

JSON feedback report → Data/Output/cover_drive_report.json

