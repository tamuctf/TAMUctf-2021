from hacksport.problem import Challenge, File


class Problem(Challenge):
    def setup(self):
        self.files = [File("eowens flyer.pdf")]

    def generate_flag(self, random):
        return r"gigem{3_0W3N5}"
