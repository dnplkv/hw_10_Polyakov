import cv2
import os
import pickle
import logging
from modules.parse_args import parse_args, args, folders
from modules.face_cascade import face_casc


def get_faces():
    """Finding faces on images in folder and
    adding faces coordinates of specified picture to dictionary
            """
    for file in os.listdir(folders):
        img = cv2.imread(os.path.join(folders, file))
    data = {}
    for file in os.listdir(folders):
        img = cv2.imread(os.path.join(folders, file))
        logging.info(f'{type(img)}')
        logging.info(f'{img.shape}')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        logging.info(f'{type(gray)}')
        logging.info(f'{gray.shape}')
        faces = face_casc().detectMultiScale(gray, 1.1, 4)
        logging.info(f'{type(faces)}')
        logging.info(f'{faces.shape}')
        data[file] = faces.tolist()
        for (x, y, w, h) in faces:  # ROI  - region of interest
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # with open('faces_dump.pickle', 'wb') as fl:
        #     """Sending dictionary to the pickle.dump
        #     """
        #     pickle.dump(data, fl)
        cv2.imshow("Image {}".format(file), img)
    cv2.waitKey()
    return data


# with open('faces_dump.pickle', 'wb') as fl:
#     """Sending dictionary to the pickle.dump
#     """
#     pickle.dump(get_faces(), fl)


