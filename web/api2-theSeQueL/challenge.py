from hacksport.docker import DockerChallenge

class Problem(DockerChallenge):
    dont_template = ["templates"]

    def setup(self):
        self.ports = {1337: fmt()}
        self.initialize_docker({'FLAG': r"gigem{SQL_1nj3ct1ons_c4n_b3_fun}"})

    def generate_flag(self, random):
        return r"gigem{SQL_1nj3ct1ons_c4n_b3_fun}"


class fmt():
    def __init__(self):
    	pass

    def dict(self):

        url = "http://{host}/problem/{{port}}/?name=Cone"
        link = "<a href='{}' target='_blank'>{}</a>".format(url, url)
        return {"fmt": link, "desc": "Here's the link for my favorite one"}