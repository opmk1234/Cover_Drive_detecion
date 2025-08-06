import numpy as np

def calculate_angle(p1, p2, p3):
    a = np.array(p1)
    b = np.array(p2)
    c = np.array(p3)

    ab = a - b
    cb = c - b
    cosine_angle = np.dot(ab, cb) / (np.linalg.norm(ab) * np.linalg.norm(cb))
    angle = np.degrees(np.arccos(cosine_angle))
    return angle

def calculate_metrics(keypoints):
    metrics = {}

    # Front elbow angle (Shoulder-Elbow-Wrist: 11,13,15)
    if len(keypoints) > 15:
        metrics['front_elbow_angle'] = calculate_angle(keypoints[11][:2], keypoints[13][:2], keypoints[15][:2])

    # Spine lean (Shoulder-Hip relative to vertical axis)
    if len(keypoints) > 23:
        spine = np.array(keypoints[23][:2]) - np.array(keypoints[11][:2])
        vertical = np.array([0, -1])
        cosine_angle = np.dot(spine, vertical) / (np.linalg.norm(spine))
        metrics['spine_lean'] = np.degrees(np.arccos(cosine_angle))

    # Foot placement angle (Hip-Knee-Ankle: 23,25,27)
    if len(keypoints) > 27:
        metrics['front_foot_angle'] = calculate_angle(keypoints[23][:2], keypoints[25][:2], keypoints[27][:2])

    # Head-Knee alignment (difference in x-axis)
    if len(keypoints) > 25:
        head_x = keypoints[0][0]  # Nose
        knee_x = keypoints[25][0]  # Left knee
        metrics['head_knee_alignment'] = abs(head_x - knee_x)

    return metrics
