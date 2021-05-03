from hacksport.docker import DockerChallenge

class Problem(DockerChallenge):
    def setup(self):
        self.ports = {80: HTTP()}
        self.initialize_docker({'FLAG': r"gigem{R3vER5e_R3ver5e!}"})

    def generate_flag(self, random):
        return r"gigem{R3vER5e_R3ver5e!}"


class HTTP():
    def __init__(self):
    	pass

    def dict(self):

        url = "http://{host}/problem/{{port}}/"
        link = "<a href='{}' target='_blank'>{}</a>".format(url, url)
        return {"fmt": link, "desc": "challenge"}