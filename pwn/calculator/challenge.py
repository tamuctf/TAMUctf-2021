from hacksport.operations import execute
from hacksport.problem import Challenge, File


class Problem(Challenge):
    def setup(self):
        self.files = []

    def generate_flag(self, random):
        return r"gigem{ju57_1n_71m3_f0r_4_5h3ll!}"
