from flask import Flask, request, render_template, send_from_directory, redirect, url_for
from threading import Timer
import time
import subprocess

app = Flask(__name__)
player_score = 0
bot_score = 0
player = True
bot = True

@app.route("/")
def score_board():
    global player_score
    global bot_score
    return render_template(
        'index.html',
        player_score=player_score,
        bot_score=bot_score,
    )

@app.route("/babyAnD")
def babyAnD():
    return send_from_directory("/home/simulator", "babyAnD" , as_attachment=True)

@app.route("/submit/<check>")
def Submit(check):
    global player_score
    global bot_score
    global player
    global bot
    with open("/home/simulator/player/flag",'r') as f:
        flag = f.read()
        if check == flag and bot == True:
            bot_score += 1
            bot = False
            return "Success !!"
    with open("/home/simulator/bot/flag",'r') as f:
        flag = f.read()
        if check == flag and player == True:
            player_score += 1
            player = False
            return "Success !!"

    return "Wrong !!"

@app.route("/patch", methods=['POST'])
def upload_patch():
    f = request.files['file']
    f.save("/home/simulator/player/babyAnD")
    return redirect(url_for('score_board'))

def token():
    global player
    global bot
    command = []
    command.append("""echo -n "FLAG{`cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1`}" > /home/simulator/player/flag""")
    command.append("""echo -n "FLAG{`cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1`}" > /home/simulator/bot/flag""")
    for i in command:
        subprocess.Popen(i, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    player = True
    bot    = True

if __name__ == '__main__':
    Timer(5*60, token, ()).start()
    app.run(host='0.0.0.0', port=80, debug=True)
