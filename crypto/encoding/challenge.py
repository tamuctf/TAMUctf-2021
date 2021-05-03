from hacksport.problem import Challenge, File

class Problem(Challenge):
    def setup(self):
        self.files = [File("data.txt")]

    def generate_flag(self, random):
        return r"gigem{3nc0ding_1s_n0t_crypt0_428427}"
