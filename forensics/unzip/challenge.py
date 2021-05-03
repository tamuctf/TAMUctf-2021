from hacksport.operations import execute
from hacksport.problem import Challenge, File


class Problem(Challenge):
    def setup(self):
        self.files = [File("chall.zip")]

    def generate_flag(self, random):
        return r"gigem{d0esnt_looK_lik3_5t4rs_t0_M3}"
