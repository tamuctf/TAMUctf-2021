from hacksport.problem import Challenge, File

class Problem(Challenge):
    def setup(self):
        self.files = [File("data.txt")]

    def generate_flag(self, random):
        return r"gigem{RSA_s3cur1ty_1s_4b0ut_pr1m3s}"
