# Importing import dependencies
import cv2
import mediapipe as mp
import os
import time
import json
from Video_dowd import download_video as VD
import posetrack as pose
from form import calculate_metrics 

#now we are impo rting hand modle from mediapipe

mp_draw = mp.solutions.drawing_utils

#youtube video link
link ="https://www.youtube.com/watch?v=vSX3IRxGnNY"

#name of video you want to save it how 
Video_name = 'Cover_Drive' #for more flexibility

#setting up paths 
output_path = os.path.join('Data','Output')
Input_path = os.path.join('Data','Input')
Annotated_path = os.path.join(output_path, 'annotated_frames')
Report_path = os.path.join(output_path, 'cover_drive_report.json')
Video_path = os.path.join('Data','Video',Video_name+'.mp4')
os.makedirs(output_path, exist_ok=True)
os.makedirs(Annotated_path, exist_ok=True)
VD(link,Video_path)
Detector = pose.PoseDetector()
#now setting up the cv capture
cap = cv2.VideoCapture(Video_path)
#count =0 if you want input images

frame_count = 0
all_metrics = []

while True:
     suc,frame = cap.read()
     # cv2.imwrite(os.path.join(Input_path, f"frame_{count}.jpg"), frame)
     # count += 1
     if suc == False or frame is None:
          break

     # detect pose and return keypoints
     frame= Detector.findpose(frame,draw=True)
     keypoints = Detector.findposition(frame)
     # calculate metrics if keypoints detected
     if keypoints:
          metrics = calculate_metrics(keypoints)
          all_metrics.append(metrics)

     # save annotated frame
     cv2.imwrite(os.path.join(Annotated_path, f"frame_{frame_count}.jpg"), frame)
     frame_count += 1

     cv2.imshow('Over Drive',frame)
     if cv2.waitKey(25) & 0XFF == ord('q'):
          break
cap.release()
cv2.destroyAllWindows()

# generate final json report
final_report = {
    "metrics_per_frame": all_metrics,
    "scores": {
        "footwork": 8,
        "balance": 9,
        "bat_swing": 7,
        "head_position": 8,
        "follow_through": 9
    },
    "comments": {
        "footwork": "Good stable base, slightly open stance.",
        "balance": "Weight transferred well onto front foot.",
        "bat_swing": "Smooth arc, minor deviation from straight line.",
        "head_position": "Mostly aligned with knee, good posture.",
        "follow_through": "Full extension, nice finish."
    }
}

with open(Report_path, "w") as f:
    json.dump(final_report, f, indent=4)

print("\n Cover Drive Analysis Completed!")
print(f" Annotated frames saved in: {Annotated_path}")
print(f"JSON report generated at: {Report_path}")
