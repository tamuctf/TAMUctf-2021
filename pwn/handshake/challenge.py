from hacksport.operations import execute
from hacksport.problem import Challenge, File


class Problem(Challenge):
    def setup(self):
        self.files = []

    def generate_flag(self, random):
        return r"gigem{r37urn_c0n7r0l1337}"
