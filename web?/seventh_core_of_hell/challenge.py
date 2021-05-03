from hacksport.docker import DockerChallenge

class Problem(DockerChallenge):
    def setup(self):
        self.ports = {5000: HTTP()}
        self.initialize_docker({'FLAG': r"gigem{wh0_541d_py7h0n_c4n7_b3_b1n4ry}"})

    def generate_flag(self, random):
        return r"gigem{wh0_541d_py7h0n_c4n7_b3_b1n4ry}"


class HTTP():
    def __init__(self):
    	pass

    def dict(self):

        url = "http://{host}/problem/{{port}}/"
        link = "<a href='{}' target='_blank'>{}</a>".format(url, url)
        return {"fmt": link, "desc": "challenge"}