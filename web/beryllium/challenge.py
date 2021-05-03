from hacksport.operations import execute
from hacksport.problem import Challenge, File


class Problem(Challenge):
    def setup(self):
        pass

    def generate_flag(self, random):
        return r"gigem{lmA0_N1c3_10c4t1oN_buddy}"
