from hacksport.operations import execute
from hacksport.problem import Challenge, File


class Problem(Challenge):
    def setup(self):
        self.files = []

    def generate_flag(self, random):
        return r"gigem{s1t3_und3r_c0n57ruc710n}"