import cv2
import os
import pickle
import logging


class Face_finder():

    def face_casc(self):
        """Adding a cascade classifier
            """
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        return face_cascade

    def get_faces(self, folder_path):
        """Finding faces on images in folder and
        adding faces coordinates of specified picture to dictionary
                """
        for file in os.listdir(folder_path):
            img = cv2.imread(os.path.join(folder_path, file))
        data = {}
        for file in os.listdir(folder_path):
            img = cv2.imread(os.path.join(folder_path, file))
            logging.info(f'{type(img)}')
            logging.info(f'{img.shape}')
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            logging.info(f'{type(gray)}')
            logging.info(f'{gray.shape}')
            faces = self.face_casc().detectMultiScale(gray, 1.1, 4)
            logging.info(f'{type(faces)}')
            logging.info(f'{faces.shape}')
            data[file] = faces.tolist()
            for (x, y, w, h) in faces:  # ROI  - region of interest
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            with open('faces_dump.pickle', 'wb') as fl:
                """Sending dictionary to the pickle.dump
                """
                pickle.dump(data, fl)
            cv2.imshow("Image {}".format(file), img)
        cv2.waitKey()
        return data




