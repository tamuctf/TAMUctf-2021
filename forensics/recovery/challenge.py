from hacksport.operations import execute
from hacksport.problem import Challenge, File


class Problem(Challenge):
    def setup(self):
        self.files = [File("floppy.img.zip")]

    def generate_flag(self, random):
        return r"gigem{0u7_0f_516h7_0u7_0f_m1nd}"
