import os


class Paths:
    path_file = os.path.dirname(os.path.abspath(__file__))
    path_input = os.path.join(path_file, "..", "..", "input")
    cred = os.path.join(path_input, "cred.yaml")
