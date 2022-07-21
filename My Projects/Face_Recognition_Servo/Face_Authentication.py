import cv2
from simple_facerec import SimpleFacerec



class Face_Authentication:
    def __init__(self):
        self.sfr = SimpleFacerec()
        self.sfr.load_encoding_images("images/")
        self.cap = cv2.VideoCapture(0)

    def authenticate_face(self):
        while True:
            print('In While Loop')
            ret, frame = self.cap.read()

            # Detect Faces
            face_locations, face_names = self.sfr.detect_known_faces(frame)
            for face_loc, name in zip(face_locations, face_names):
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
                cv2.putText(frame, str(name),(x1, y1 -20 ), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 2)

                cv2.imshow("Frame", frame)
                cv2.waitKey(1)


if __name__ == "__main__":
    face_recognition = Face_Authentication()
    face_recognition.authenticate_face()
