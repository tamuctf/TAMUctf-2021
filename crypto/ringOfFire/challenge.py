from hacksport.problem import Challenge, File

class Problem(Challenge):
    def setup(self):
        self.files = [File("codeFile.txt")]

    def generate_flag(self, random):
        return r"gigem{x0r_is_c0mmuT4T1ve}"
