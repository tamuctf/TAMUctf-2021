from hacksport.operations import execute
from hacksport.problem import Challenge, File


class Problem(Challenge):
    def setup(self):
        pass

    def generate_flag(self, random):
        return r"gigem{cryp706r4ph1c4lly_1n53cur3_prn65_DC6F9B}"
