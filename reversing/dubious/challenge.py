from hacksport.operations import execute
from hacksport.problem import Challenge, File

class Problem(Challenge):
    dont_template = ["constraintgen"]

    def setup(self):
        pass

    def generate_flag(self, random):
        return r"gigem{cu570m_t0Ol1nG_0r_5uFF3r_c3fa0b029bf26fa98bf4b936532893}"
