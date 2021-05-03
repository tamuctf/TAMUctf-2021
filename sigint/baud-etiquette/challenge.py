from hacksport.operations import execute
from hacksport.problem import Challenge, File


class Problem(Challenge):
    def setup(self):
        self.files = [File("signal.bin.zip"), File("sound.gif"), File("sound.wav")]

    def generate_flag(self, random):
        return r"GIGEM(AMATEUR-PARTTY)"
