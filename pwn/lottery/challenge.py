from hacksport.operations import execute
from hacksport.problem import Challenge, File


class Problem(Challenge):
    def setup(self):
        self.files = []

    def generate_flag(self, random):
        return r"gigem{3x3cu74bl3_rn6}"
