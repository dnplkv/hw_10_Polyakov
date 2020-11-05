import logging
from modules.parse_args import Parser
from modules.get_faces import Face_finder
from modules.from_dump import Dump

logging.basicConfig(level=logging.DEBUG,
                    filename="main_py.log",
                    filemode="w")

logging.info("Start program \n")


def run():
    Face_finder().get_faces(Parser().parse_args().path)
    Dump().read_dump()


if __name__ == "__main__":
    run()

logging.info("End program")
