from hacksport.operations import execute
from hacksport.problem import Challenge, File


class Problem(Challenge):
    def setup(self):
        self.files = [File("crypto.php"), File("output.bin")]

    def generate_flag(self, random):
        return r"gigem{dont~roll~your~own~crypto}"
