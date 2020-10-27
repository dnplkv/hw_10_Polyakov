import cv2


def face_casc():
    """Adding a cascade classifier
        """
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    return face_cascade