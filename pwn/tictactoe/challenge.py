from hacksport.operations import execute
from hacksport.problem import Challenge, File


class Problem(Challenge):
    def setup(self):
        self.files = []

    def generate_flag(self, random):
        return r"gigem{h3y_7h47_d035n'7_l00k_l1k3_4_p1ckl3d_54v3}"
