import logging
from modules.face_cascade import face_casc
from modules.parse_args import parse_args, args, folders
from modules.get_faces import get_faces
from modules.from_dump import read_dump

logging.basicConfig(level=logging.DEBUG,
                    filename="main_py.log",
                    filemode="w")

logging.info("Start program \n")


def run():
    parse_args()
    face_casc()
    get_faces()
    read_dump()


if __name__ == "__main__":
    run()

logging.info("End program")
