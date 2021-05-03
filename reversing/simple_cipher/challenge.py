from hacksport.operations import execute
from hacksport.problem import Challenge, File, Compiled

class Problem(Compiled):
    files = [File("flag.enc")]
    compiler_sources = ["simple_cipher.c"]
    program_name = "simple_cipher"

    def generate_flag(self, random):
        return r"gigem{d0n7_wr173_y0ur_0wn_c1ph3r5}"
