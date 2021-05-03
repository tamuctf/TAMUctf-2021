from hacksport.operations import execute
from hacksport.problem import Challenge, File


class Problem(Challenge):
    def setup(self):
        pass

    def generate_flag(self, random):
        return r"gigem{0oP5_al1_3xeCu7aB1e}"
