import pickle
import logging


class Dump():

    def read_dump(self):
        with open('faces_dump.pickle', 'rb') as fl:
            data_new = pickle.load(fl)

        for key, value in data_new.items():
            logging.info(f'{key} : {value}')
            print(key, ' : ', value)

