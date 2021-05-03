from hacksport.problem import Challenge, File

class Problem(Challenge):
    def setup(self):
        self.files = [File("BlackBox.hdl")]

    def generate_flag(self, random):
        return r"gigem{t0o_M4nY_s3cR3tS}"
