from hacksport.operations import execute
from hacksport.problem import Challenge, File


class Problem(Challenge):
    def setup(self):
        pass

    def generate_flag(self, random):
        return r"gigem{4ud10-m4d3-v15u4L}"
