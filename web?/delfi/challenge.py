from hacksport.operations import execute
from hacksport.problem import Challenge, File


class Problem(Challenge):
    def setup(self):
        pass

    def generate_flag(self, random):
        return r"gigem{d4ng3r0u5ly_3xfil7r47in6_l0c4l_fil3_includ35}"
