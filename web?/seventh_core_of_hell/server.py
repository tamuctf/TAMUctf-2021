from flask import Flask
from flask import request, Response, render_template, send_from_directory, send_file, session
import os
import tarfile, io
import json
import random
from string import digits, ascii_letters

app = Flask(__name__)
notes = []

def redirect(url):
    return """
    <head>
        <meta http-equiv="refresh" content="0; url={}"
    </head>
    """.format(url)

app.secret_key = ''.join([random.choice(digits+ascii_letters) for x in range(256)])


@app.before_request
def add_trailing():
    rp = request.path 
    if not rp.endswith('/'):
        return redirect(os.path.join(".", rp.lstrip("/") + "/"))


@app.route('/dump/')
def core_dump():
    """
    debug route so our testers can check out the memory
    MAKE SURE TO REMOVE THIS
    """
    os.system(f"sudo gcore {os.getpid()}")
    return send_file(f"core.{os.getpid()}")

@app.route('/get_file/')
def get_file():

    if not ("admin" in session and session['admin']):
        return redirect("./login/")

    file = os.path.join("files", request.args.get('file'))
    offset = request.args.get('offset')
    size = request.args.get('size')
    try:
        offset = int(offset)
    except:
        offset = 0
    try:
        size = int(size)
    except:
        size = -1

    if file == None:
        return "parameter 'file' must not be None"

    f = open(file,"rb")
    f.seek(offset)
    data = f.read(size)
    return Response(data, headers={'Content-Disposition': f"attachment;filename={os.path.basename(file)}"})

@app.route('/upload_single/', methods=['POST'])
def upload_single():
    if not ("admin" in session and session['admin']):
        return redirect("./login/")

    save_location = os.path.join(".", "files", request.form.get("current_path").replace("..",""),request.files['data'].filename)
    offset = request.form.get('offset')
    try:
        offset = int(offset)
    except:
        offset = 0
    upload = request.files['data'].read()
    f = open(save_location,"wb+")
    f.seek(int(offset))
    f.write(upload)
    return redirect(os.path.join("..", "browse",request.form.get("current_path").replace("..","")))

@app.route('/upload_tar/', methods=['POST'])
def upload_tar():
    if not ("admin" in session and session['admin']):
        return redirect("./login/")

    save_location = os.path.join(".", "files", request.form.get("current_path").replace("..",""))
    tar = tarfile.open(fileobj=io.BytesIO(request.files['data'].read()))
    tar.extractall(save_location)
    return redirect(os.path.join("..", "browse",request.form.get("current_path").replace("..","")))


@app.route('/add_note/', methods=['POST'])
def add_note():
    if not ("admin" in session and session['admin']):
        return redirect("./login/")

    message = request.form.get("message")
    app.logger.info(f"saving note {message}")
    global notes
    notes.append(message)

    return redirect(os.path.join("..", "browse",request.form.get("current_path").replace("..","")))

@app.route('/browse/', defaults={'urlFilePath': ""})
@app.route('/browse/<path:urlFilePath>/')
def browser(urlFilePath):

    if not ("admin" in session and session['admin']):
        return redirect("../login/")

    path =  os.path.join(".", "files", urlFilePath.replace("..",""))
    if os.path.isfile(path):
        return redirect(os.path.join(*[".." for x in range(os.path.normpath(urlFilePath).count("/")+2)], f"get_file/?file={urlFilePath.replace('..','')}&offset=0&size=-1"))
    else:
        return render_template("browse.html", files=[x for x in os.listdir(path)], current_path=urlFilePath + "/" if (urlFilePath != '' and not urlFilePath.endswith("/")) else urlFilePath)

@app.route('/')
def index():
    return redirect("./browse/")


@app.route('/login/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == ''.join([random.choice(digits+ascii_letters) for x in range(256)]):
            session['admin'] = True
        else:
            session['admin'] = False
        return redirect("../browse/")
    return render_template("login.html")

@app.route('/logout/')
def logout():
   session.pop('username', None)
   return redirect(".")


app.run(host="0.0.0.0")
