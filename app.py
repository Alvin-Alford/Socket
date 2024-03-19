from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app)


def searchuser(username):
    file_path = 'data.txt'

    with open(file_path, 'r') as file:
        data = file.read()
        


    lines = data.strip().split('\n')

    for line in lines:
        if username in line:
            # Get the last word from the line
            Devicename = line.split()[-1]
            state = True
        else:
            Devicename = "Null"
            state = False

    return Devicename,state

@app.route('/connectionpage',methods = ['POST','GET'])
def home():

    if request.method == "POST":
        name = request.form.get("User")

        Devicename,state = searchuser(name)

        if state == True:
            room = Devicename
            
        else:
            return render_template("connection.html",login = "no")

    return render_template('homepage.html')



if __name__ == "__main__":
    socketio.run(app, debug=False,port=5556)