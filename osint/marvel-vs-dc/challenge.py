from hacksport.problem import Challenge, File


class Problem(Challenge):
    def setup(self):
        pass

    def generate_flag(self, random):
        return r"gigem{M42V3LisbetterthanDCC0M1C5}"
