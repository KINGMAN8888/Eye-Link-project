import cv2
import mediapipe as mp
import math
import config

class EyeTracker:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6
        )
        
        self.LEFT_EYE = [362, 385, 387, 263, 373, 380]
        self.RIGHT_EYE = [33, 160, 158, 133, 153, 144]

    def get_eye_aspect_ratio(self, eye_points, landmarks):
        A = math.dist(landmarks[eye_points[1]], landmarks[eye_points[5]])
        B = math.dist(landmarks[eye_points[2]], landmarks[eye_points[4]])
        C = math.dist(landmarks[eye_points[0]], landmarks[eye_points[3]])
        
        if C == 0: return 0.0
        ear = (A + B) / (2.0 * C)
        return ear

    def process_frame(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(frame_rgb)
        
        is_blink = False
        avg_ear = 0.0
        mesh_points = None

        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark
            h, w, _ = frame.shape
            
            mesh_points = [(int(p.x * w), int(p.y * h)) for p in landmarks]

            left_ear = self.get_eye_aspect_ratio(self.LEFT_EYE, mesh_points)
            right_ear = self.get_eye_aspect_ratio(self.RIGHT_EYE, mesh_points)
            
            avg_ear = (left_ear + right_ear) / 2.0

            if avg_ear < config.BLINK_THRESHOLD:
                is_blink = True
            return is_blink, mesh_points, avg_ear
            
        return False, None, 0.0